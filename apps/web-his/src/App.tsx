import { useCallback, useEffect, useState } from 'react'
import { Bell, Search } from 'lucide-react'
import { Sidebar, type View } from './components/Sidebar'
import { fallbackIncidents, fallbackSummary } from './data/fallback'
import { Dashboard } from './pages/Dashboard'
import { Architecture } from './pages/Architecture'
import { Workflow } from './pages/Workflow'
import { api } from './services/api'
import type { DashboardSummary, Incident } from './types'
import './styles.css'

export default function App() {
  const [view, setView] = useState<View>('dashboard')
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
        <div className="utility-bar"><div className="search"><Search size={16} /><span>Buscar paciente, incidente o modulo</span></div><button className="icon-button" title="Notificaciones"><Bell size={18} /></button><div className="avatar">MC</div><div className="user"><b>Maria Cardenas</b><small>Calidad · Quito</small></div></div>
        <div className="page-content">
          {view === 'dashboard' && <Dashboard summary={summary} incidents={incidents} demo={demo} onRefresh={() => void load()} />}
          {view === 'architecture' && <Architecture />}
          {!['dashboard', 'architecture'].includes(view) && <Workflow view={view as Exclude<View, 'dashboard' | 'architecture'>} />}
        </div>
      </main>
    </div>
  )
}

