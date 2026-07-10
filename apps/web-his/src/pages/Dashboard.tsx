import { AlertTriangle, Database, RefreshCw } from 'lucide-react'
import { Bar, BarChart, CartesianGrid, Cell, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'
import type { DashboardSummary, Incident } from '../types'
import { MetricPanel } from '../components/MetricPanel'

const chartColors = ['#0c695f', '#ca4b38', '#d59622', '#377c9d', '#755c8d', '#5c7c49', '#8c5a3c', '#3f6477', '#6c757d']

export function Dashboard({ summary, incidents, demo, onRefresh }: { summary: DashboardSummary; incidents: Incident[]; demo: boolean; onRefresh: () => void }) {
  const moduleData = Object.entries(summary.incidents_by_module).map(([name, value]) => ({ name: name.replace('Portal ', ''), value }))
  return (
    <>
      <header className="page-header">
        <div><p className="eyebrow">GERENCIA DE CALIDAD</p><h1>Calidad en uso</h1><span>Periodo {summary.period} · 3.000 incidentes auditados</span></div>
        <div className="header-actions"><span className={demo ? 'connection demo' : 'connection'}>{demo ? 'Datos locales' : 'API conectada'}</span><button className="icon-button" onClick={onRefresh} title="Actualizar datos"><RefreshCw size={18} /></button></div>
      </header>
      <section className="metrics-grid">{summary.metrics.slice(0, 4).map((metric, index) => <MetricPanel key={metric.code} metric={metric} index={index} />)}</section>
      <section className="dashboard-grid">
        <article className="panel chart-panel">
          <div className="panel-title"><div><h2>Incidentes por modulo</h2><p>Distribucion del dataset original</p></div><Database size={19} /></div>
          <ResponsiveContainer width="100%" height={280}>
            <BarChart data={moduleData} margin={{ top: 12, right: 8, left: -24, bottom: 28 }}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e9e8" />
              <XAxis dataKey="name" angle={-25} textAnchor="end" fontSize={11} interval={0} />
              <YAxis fontSize={11} /><Tooltip />
              <Bar dataKey="value" radius={[3, 3, 0, 0]}>{moduleData.map((_, i) => <Cell key={i} fill={chartColors[i % chartColors.length]} />)}</Bar>
            </BarChart>
          </ResponsiveContainer>
        </article>
        <article className="panel incident-panel">
          <div className="panel-title"><div><h2>Incidentes recientes</h2><p>Casos priorizados para revision</p></div><AlertTriangle size={19} /></div>
          <div className="incident-list">
            {incidents.slice(0, 5).map((incident) => <div className="incident-row" key={incident.id}><span className="incident-dot" /><div><b>{incident.modulo}</b><p>{incident.descripcion}</p><small>{incident.sede} · {incident.rol_usuario}</small></div><span className="incident-id">#{incident.id}</span></div>)}
          </div>
        </article>
      </section>
    </>
  )
}

