import { useState } from 'react'
import { AlertCircle, CheckCircle2, ClipboardCheck, FlaskConical, ShieldAlert, UserRound } from 'lucide-react'
import { api } from '../services/api'
import type { View } from '../components/Sidebar'

type WorkflowView = Exclude<View, 'home' | 'quality'>
type Field = { label: string; value: string; multiline?: boolean }
type WorkflowContent = {
  eyebrow: string
  title: string
  description: string
  action: string
  error: string
  errorLabel: string
  fields: Field[]
  sideTitle: string
  sideItems: [string, string][]
}

const content: Record<WorkflowView, WorkflowContent> = {
  appointments: {
    eyebrow: 'ADMISIÓN Y AGENDA', title: 'Nueva cita', description: 'Registre al paciente y asigne una disponibilidad médica.', action: 'Confirmar cita',
    error: 'extra_steps', errorLabel: 'Flujo prolongado y abandono',
    fields: [{ label: 'Paciente', value: 'Ana Torres · PAC-001' }, { label: 'Especialidad', value: 'Medicina interna' }, { label: 'Fecha y hora', value: '17/11/2025 · 09:40' }, { label: 'Cobertura', value: 'Seguro privado · Plan Salud Plus' }],
    sideTitle: 'Disponibilidad', sideItems: [['Profesional', 'Dra. María Cárdenas'], ['Consultorio', '304'], ['Duración', '30 minutos']],
  },
  hce: {
    eyebrow: 'ATENCIÓN MÉDICA', title: 'Historia clínica electrónica', description: 'Atención activa de Carlos Medina · PAC-184.', action: 'Guardar y firmar nota',
    error: 'slow', errorLabel: 'Guardado superior a 8 segundos',
    fields: [{ label: 'Motivo de consulta', value: 'Revisión de resultados y seguimiento metabólico' }, { label: 'Evaluación clínica', value: 'Paciente estable. Refiere mejor adherencia al tratamiento y niega síntomas de alarma.', multiline: true }, { label: 'Diagnóstico', value: 'E11.9 · Diabetes mellitus tipo 2' }],
    sideTitle: 'Resumen del paciente', sideItems: [['Edad', '58 años'], ['Grupo sanguíneo', 'O+'], ['Alergias', 'Penicilina'], ['Última atención', '22/10/2025']],
  },
  nursing: {
    eyebrow: 'ENFERMERÍA', title: 'Registro de signos vitales', description: 'Preconsulta de Ana Torres · PAC-001.', action: 'Registrar signos vitales',
    error: 'missing_allergy', errorLabel: 'Alergia no disponible',
    fields: [{ label: 'Presión arterial', value: '138/86 mmHg' }, { label: 'Frecuencia cardíaca', value: '78 lpm' }, { label: 'Temperatura', value: '36.6 °C' }, { label: 'Saturación de oxígeno', value: '96 %' }],
    sideTitle: 'Protocolo', sideItems: [['Triage', 'Prioridad III'], ['Dolor', '2 / 10'], ['Observación', 'Sin signos de alarma']],
  },
  pharmacy: {
    eyebrow: 'FARMACIA', title: 'Validación de prescripción', description: 'Orden RX-2025-184 pendiente de dispensación.', action: 'Validar y dispensar',
    error: 'dose_error', errorLabel: 'Dosis incompatible sin alerta',
    fields: [{ label: 'Paciente', value: 'Carlos Medina · PAC-184' }, { label: 'Medicamento', value: 'Metformina 850 mg' }, { label: 'Posología', value: '1 tableta cada 12 horas · 30 días' }, { label: 'Cantidad', value: '60 tabletas' }],
    sideTitle: 'Control farmacéutico', sideItems: [['Disponibilidad', '124 unidades'], ['Interacciones', 'Sin interacción mayor'], ['Prescriptor', 'Dra. María Cárdenas']],
  },
  billing: {
    eyebrow: 'FACTURACIÓN', title: 'Cuenta de atención', description: 'Liquidación de consulta ambulatoria FAC-2025-0918.', action: 'Emitir factura',
    error: 'duplicate', errorLabel: 'Emisión duplicada',
    fields: [{ label: 'Paciente', value: 'Ana Torres · PAC-001' }, { label: 'Prestación', value: 'Consulta de medicina interna' }, { label: 'Aseguradora', value: 'Salud Plus' }, { label: 'Total', value: '$ 48,50' }],
    sideTitle: 'Resumen de cobertura', sideItems: [['Cobertura', '80 %'], ['Copago', '$ 9,70'], ['Autorización', 'AUT-88401']],
  },
  telemedicine: {
    eyebrow: 'TELEMEDICINA', title: 'Sala de teleconsulta', description: 'Sesión programada con María López · PAC-315.', action: 'Iniciar teleconsulta',
    error: 'disconnect', errorLabel: 'Interrupción de la sesión',
    fields: [{ label: 'Especialidad', value: 'Medicina interna' }, { label: 'Inicio programado', value: '14/11/2025 · 11:00' }, { label: 'Motivo', value: 'Control posterior al alta' }, { label: 'Canal alterno', value: '+593 99 000 1842' }],
    sideTitle: 'Prueba de conexión', sideItems: [['Audio', 'Disponible'], ['Video', 'Disponible'], ['Red del paciente', 'Estable']],
  },
}

export function Workflow({ view }: { view: WorkflowView }) {
  const [scenario, setScenario] = useState('normal')
  const [result, setResult] = useState<Record<string, unknown> | null>(null)
  const [loading, setLoading] = useState(false)
  const item = content[view]

  async function run() {
    setLoading(true)
    try {
      const response = view === 'billing'
        ? await api.createInvoice(scenario)
        : view === 'hce'
          ? await api.saveNote(scenario)
          : { successful: scenario === 'normal', scenario, simulated: true, auditId: `AUD-${Date.now().toString().slice(-6)}` }
      setResult(response)
    } catch {
      setResult({ successful: false, scenario, errorCode: 'API-NO-DISPONIBLE', simulated: true })
    } finally { setLoading(false) }
  }

  const ok = result?.successful !== false && result?.duplicate !== true
  return (
    <>
      <header className="page-header"><div><p className="eyebrow">{item.eyebrow}</p><h1>{item.title}</h1><span>{item.description}</span></div><span className="record-status"><span /> Borrador guardado</span></header>
      <section className="workflow-layout clinical-workflow">
        <article className="panel workflow-form">
          <div className="panel-title"><div><h2>Información de la atención</h2><p>Los campos obligatorios están completos</p></div><ClipboardCheck size={20} /></div>
          <div className="field-grid">
            {item.fields.map((field) => <label className={field.multiline ? 'wide' : ''} key={field.label}>{field.label}{field.multiline ? <textarea defaultValue={field.value} rows={4} /> : <input defaultValue={field.value} />}</label>)}
          </div>
          <details className="simulation-tools">
            <summary><FlaskConical size={16} /> Herramientas de simulación local</summary>
            <div><label>Comportamiento de esta ejecución<select value={scenario} onChange={(event) => setScenario(event.target.value)}><option value="normal">Operación normal</option><option value={item.error}>{item.errorLabel}</option>{view === 'hce' && <option value="save_failure">Pérdida durante el guardado</option>}</select></label><p>El modo seleccionado se registra con semilla y auditoría para producir evidencia reproducible.</p></div>
          </details>
          <div className="form-actions"><button className="secondary-button">Cancelar</button><button className="primary-button" onClick={run} disabled={loading}>{loading ? 'Procesando…' : item.action}</button></div>
        </article>

        <aside className="workflow-side">
          <article className="panel patient-summary">
            <div className="panel-title"><div><h2>{item.sideTitle}</h2><p>Información verificada</p></div><UserRound size={19} /></div>
            <dl>{item.sideItems.map(([label, value]) => <div key={label}><dt>{label}</dt><dd>{value}</dd></div>)}</dl>
          </article>
          {result && <article className={`panel execution-result ${ok ? 'ok' : 'failure'}`}><div className="result-heading">{ok ? <CheckCircle2 /> : <ShieldAlert />}<div><h2>{ok ? 'Operación completada' : 'Incidencia registrada'}</h2><p>{ok ? 'La información quedó disponible en el HIS.' : 'El fallo controlado generó evidencia para medición.'}</p></div></div><dl><div><dt>Escenario</dt><dd>{String(result.scenario)}</dd></div><div><dt>Resultado</dt><dd>{ok ? 'Exitoso' : 'No completado'}</dd></div></dl></article>}
          {!result && <article className="panel workflow-hint"><AlertCircle /><div><h2>Validación previa</h2><p>Revise los datos antes de completar la operación.</p></div></article>}
        </aside>
      </section>
    </>
  )
}
