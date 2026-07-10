import { useCallback, useEffect, useState } from 'react'
import { Bell, Search } from 'lucide-react'
import { Sidebar, type View } from './components/Sidebar'
import { fallbackIncidents, fallbackSummary } from './data/fallback'
import { Dashboard } from './pages/Dashboard'
import { Home } from './pages/Home'
import { Workflow } from './pages/Workflow'
import { api } from './services/api'
import type { DashboardSummary, Incident } from './types'
import './styles.css'

export default function App() {
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
  return (
    <div className="app-shell">
      <Sidebar view={view} onChange={setView} />
      <main>
        <div className="utility-bar"><div className="search"><Search size={16} /><span>Buscar paciente, cita o historia clínica</span></div><button className="icon-button notification-button" title="Notificaciones"><Bell size={18} /><i>3</i></button><div className="avatar">MC</div><div className="user"><b>Dra. María Cárdenas</b><small>Medicina interna · Quito</small></div></div>
        <div className="page-content">
          {view === 'home' && <Home onNavigate={setView} />}
          {view === 'quality' && <Dashboard summary={summary} incidents={incidents} demo={demo} onRefresh={() => void load()} />}
          {!['home', 'quality'].includes(view) && <Workflow view={view as Exclude<View, 'home' | 'quality'>} />}
        </div>
      </main>
    </div>
  )
}
