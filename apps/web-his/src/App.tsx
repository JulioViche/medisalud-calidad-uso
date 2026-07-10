import { useCallback, useEffect, useState } from 'react'
import { Bell, Search } from 'lucide-react'
import { Sidebar, type View } from './components/Sidebar'
import { fallbackIncidents, fallbackSummary } from './data/fallback'
import { Dashboard } from './pages/Dashboard'
import { Home } from './pages/Home'
import { Workflow } from './pages/Workflow'
import { api } from './services/api'
import type { DashboardSummary, Incident } from './types'
import { canAccess, type SessionUser } from './auth'
import { Login } from './pages/Login'
import './styles.css'

const SESSION_KEY = 'medisalud-his-session'

export default function App() {
  const [session, setSession] = useState<SessionUser | null>(() => {
    const stored = sessionStorage.getItem(SESSION_KEY)
    return stored ? JSON.parse(stored) as SessionUser : null
  })
  const [view, setView] = useState<View>('home')
  const [summary, setSummary] = useState<DashboardSummary>(fallbackSummary)
  const [incidents, setIncidents] = useState<Incident[]>(fallbackIncidents)
  const [demo, setDemo] = useState(true)
  const load = useCallback(async () => {
    try {
      const [dashboard, incidentPage] = await Promise.all([api.dashboard(), api.incidents()])
      setSummary(dashboard); setIncidents(incidentPage.items); setDemo(false)
    } catch { setSummary(fallbackSummary); setIncidents(fallbackIncidents); setDemo(true) }
  }, [])
  useEffect(() => { void load() }, [load])
  function login(user: SessionUser) {
    sessionStorage.setItem(SESSION_KEY, JSON.stringify(user))
    setSession(user)
    setView('home')
  }
  function logout() {
    sessionStorage.removeItem(SESSION_KEY)
    setSession(null)
    setView('home')
  }
  function navigate(nextView: View) {
    if (session && canAccess(session.role, nextView)) setView(nextView)
  }
  if (!session) return <Login onLogin={login} />
  return (
    <div className="app-shell">
      <Sidebar view={view} user={session} onChange={navigate} onLogout={logout} />
      <main>
        <div className="utility-bar"><div className="search"><Search size={16} /><span>Buscar paciente, cita o historia clínica</span></div><button className="icon-button notification-button" title="Notificaciones"><Bell size={18} /><i>3</i></button><div className="avatar">{session.initials}</div><div className="user"><b>{session.name}</b><small>{session.roleLabel} · {session.site}</small></div></div>
        <div className="page-content">
          {view === 'home' && <Home user={session} onNavigate={navigate} />}
          {view === 'quality' && <Dashboard summary={summary} incidents={incidents} demo={demo} onRefresh={() => void load()} />}
          {!['home', 'quality'].includes(view) && <Workflow view={view as Exclude<View, 'home' | 'quality'>} />}
        </div>
      </main>
    </div>
  )
}
