import { useState } from 'react'
import { AlertCircle, CheckCircle2, ClipboardPlus, Receipt } from 'lucide-react'
import { api } from '../services/api'
import type { View } from '../components/Sidebar'

const content: Record<Exclude<View, 'dashboard' | 'architecture'>, { title: string; role: string; action: string; normal: string; error: string }> = {
  hce: { title: 'Historia clinica electronica', role: 'Medico tratante', action: 'Guardar nota', normal: 'normal', error: 'slow' },
  appointments: { title: 'Citas y admision', role: 'Personal de admision', action: 'Simular agendamiento', normal: 'normal', error: 'extra_steps' },
  billing: { title: 'Facturacion', role: 'Personal de admision', action: 'Emitir factura', normal: 'normal', error: 'duplicate' },
  pharmacy: { title: 'Farmacia e inventario', role: 'Farmacia', action: 'Procesar prescripcion', normal: 'normal', error: 'dose_error' },
}

export function Workflow({ view }: { view: Exclude<View, 'dashboard' | 'architecture'> }) {
  const [scenario, setScenario] = useState('normal')
  const [result, setResult] = useState<Record<string, unknown> | null>(null)
  const [loading, setLoading] = useState(false)
  const item = content[view]
  async function run() {
    setLoading(true)
    try {
      const response = view === 'billing' ? await api.createInvoice(scenario) : view === 'hce' ? await api.saveNote(scenario) : { successful: scenario === 'normal', scenario, simulated: true }
      setResult(response)
    } catch {
      setResult({ successful: false, scenario, errorCode: 'API-NO-DISPONIBLE', simulated: true })
    } finally { setLoading(false) }
  }
  const ok = result?.successful !== false && result?.duplicate !== true
  return (
    <>
      <header className="page-header"><div><p className="eyebrow">{item.role.toUpperCase()}</p><h1>{item.title}</h1><span>Flujo reducido para generar evidencia de calidad en uso</span></div></header>
      <section className="workflow-layout">
        <article className="panel workflow-form">
          <div className="panel-title"><div><h2>Escenario controlado</h2><p>La regla seleccionada queda registrada en auditoria</p></div>{view === 'billing' ? <Receipt /> : <ClipboardPlus />}</div>
          <label>Paciente<input value="Ana Torres · PAC-001" readOnly /></label>
          <label>Sede<select defaultValue="Quito"><option>Quito</option><option>Guayaquil</option><option>Cuenca</option><option>Ambato</option><option>Manta</option></select></label>
          <label>Condicion de simulacion<select value={scenario} onChange={(event) => setScenario(event.target.value)}><option value={item.normal}>Operacion normal</option><option value={item.error}>Fallo intencional medible</option>{view === 'hce' && <option value="save_failure">Perdida al guardar</option>}</select></label>
          <button className="primary-button" onClick={run} disabled={loading}>{loading ? 'Procesando…' : item.action}</button>
        </article>
        <article className={`panel result-panel ${result ? (ok ? 'ok' : 'failure') : ''}`}>
          {!result ? <div className="empty-state"><AlertCircle /><h2>Sin ejecucion</h2><p>Seleccione una condicion y ejecute el flujo.</p></div> : <div><div className="result-icon">{ok ? <CheckCircle2 /> : <AlertCircle />}</div><h2>{ok ? 'Tarea completada' : 'Fallo reproducido'}</h2><p>Escenario: <b>{String(result.scenario)}</b></p><pre>{JSON.stringify(result, null, 2)}</pre></div>}
        </article>
      </section>
    </>
  )
}

