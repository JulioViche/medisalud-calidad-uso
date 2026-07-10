import { ArrowRight, CalendarCheck, ClipboardClock, FileHeart, FlaskConical, UserRoundCheck, UsersRound } from 'lucide-react'
import type { View } from '../components/Sidebar'
import { allowedViews, type SessionUser } from '../auth'

const appointments = [
  { time: '08:30', patient: 'Ana Torres', id: 'PAC-001', reason: 'Control de hipertensión', status: 'En espera', tone: 'waiting' },
  { time: '09:00', patient: 'Carlos Medina', id: 'PAC-184', reason: 'Revisión de resultados', status: 'En atención', tone: 'active' },
  { time: '09:40', patient: 'Elena Paredes', id: 'PAC-092', reason: 'Dolor abdominal', status: 'Confirmada', tone: 'confirmed' },
  { time: '10:20', patient: 'Jorge Almeida', id: 'PAC-227', reason: 'Seguimiento metabólico', status: 'Confirmada', tone: 'confirmed' },
]

const viewLabels: Partial<Record<View, string>> = {
  appointments: 'Citas y admisión', hce: 'Historia clínica', nursing: 'Enfermería',
  pharmacy: 'Farmacia', billing: 'Facturación', telemedicine: 'Telemedicina', quality: 'Reportes operativos',
}

export function Home({ user, onNavigate }: { user: SessionUser; onNavigate: (view: View) => void }) {
  if (user.role !== 'doctor') {
    const modules = allowedViews(user.role).filter((view) => view !== 'home')
    return (
      <>
        <header className="page-header home-header"><div><p className="eyebrow">SEDE {user.site.toUpperCase()}</p><h1>Buenos días, {user.name}</h1><span>Accesos habilitados para el perfil de {user.roleLabel.toLowerCase()}.</span></div></header>
        <section className="role-home" aria-label="Módulos habilitados">
          {modules.map((view) => <button key={view} onClick={() => onNavigate(view)}><span>{viewLabels[view]}</span><ArrowRight size={18} /></button>)}
        </section>
      </>
    )
  }
  return (
    <>
      <header className="page-header home-header">
        <div><p className="eyebrow">VIERNES, 14 DE NOVIEMBRE DE 2025</p><h1>Buenos días, Dra. Cárdenas</h1><span>Esta es la actividad clínica programada para la sede Quito.</span></div>
        <button className="primary-button compact" onClick={() => onNavigate('appointments')}><CalendarCheck size={17} /> Nueva cita</button>
      </header>

      <section className="operational-stats" aria-label="Resumen operativo">
        <article><span className="stat-icon teal"><UsersRound /></span><div><strong>14</strong><p>Citas programadas</p></div><small>12 confirmadas</small></article>
        <article><span className="stat-icon coral"><ClipboardClock /></span><div><strong>6</strong><p>Pacientes en espera</p></div><small>18 min promedio</small></article>
        <article><span className="stat-icon gold"><FlaskConical /></span><div><strong>4</strong><p>Resultados pendientes</p></div><small>2 prioritarios</small></article>
        <article><span className="stat-icon blue"><FileHeart /></span><div><strong>3</strong><p>Notas por firmar</p></div><small>De la jornada anterior</small></article>
      </section>

      <section className="home-grid">
        <article className="panel schedule-panel">
          <div className="panel-title"><div><h2>Agenda de hoy</h2><p>Consultorio 304 · Medicina interna</p></div><button className="text-button" onClick={() => onNavigate('appointments')}>Ver agenda <ArrowRight size={15} /></button></div>
          <div className="schedule-list">
            {appointments.map((appointment) => (
              <button className="schedule-row" key={appointment.time} onClick={() => onNavigate('hce')}>
                <time>{appointment.time}</time><div className="patient-avatar">{appointment.patient.split(' ').map((part) => part[0]).join('')}</div>
                <div className="patient-info"><b>{appointment.patient}</b><span>{appointment.id} · {appointment.reason}</span></div>
                <span className={`workflow-status ${appointment.tone}`}>{appointment.status}</span><ArrowRight size={16} />
              </button>
            ))}
          </div>
        </article>

        <aside className="home-side">
          <article className="panel attention-panel">
            <div className="panel-title"><div><h2>Atención en curso</h2><p>Iniciada a las 09:03</p></div><span className="live-pill">EN CURSO</span></div>
            <div className="current-patient"><div className="patient-avatar large">CM</div><div><b>Carlos Medina</b><span>PAC-184 · 58 años</span></div></div>
            <dl><div><dt>Motivo</dt><dd>Revisión de resultados</dd></div><div><dt>Alerta clínica</dt><dd className="clinical-alert">Alergia a penicilina</dd></div></dl>
            <button className="primary-button full" onClick={() => onNavigate('hce')}><UserRoundCheck size={17} /> Continuar atención</button>
          </article>
          <article className="panel pending-panel">
            <div className="panel-title"><div><h2>Pendientes clínicos</h2><p>Requieren revisión</p></div></div>
            <button><span className="task-mark urgent" /><div><b>Resultado crítico</b><small>Glucosa · Elena Paredes</small></div><strong>Ahora</strong></button>
            <button><span className="task-mark" /><div><b>Orden por validar</b><small>Farmacia · Carlos Medina</small></div><strong>12 min</strong></button>
            <button><span className="task-mark" /><div><b>Teleconsulta próxima</b><small>María López · 11:00</small></div><strong>38 min</strong></button>
          </article>
        </aside>
      </section>
    </>
  )
}
