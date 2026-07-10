import { Activity, CalendarDays, ClipboardPlus, HeartPulse, Home, Pill, Receipt, Stethoscope, Video } from 'lucide-react'

export type View = 'home' | 'appointments' | 'hce' | 'nursing' | 'pharmacy' | 'billing' | 'telemedicine' | 'quality'

const items: { id: View; label: string; icon: typeof Activity }[] = [
  { id: 'home', label: 'Inicio', icon: Home },
  { id: 'appointments', label: 'Citas y admision', icon: CalendarDays },
  { id: 'hce', label: 'Historia clinica', icon: ClipboardPlus },
  { id: 'nursing', label: 'Enfermeria', icon: HeartPulse },
  { id: 'pharmacy', label: 'Farmacia', icon: Pill },
  { id: 'billing', label: 'Facturacion', icon: Receipt },
  { id: 'telemedicine', label: 'Telemedicina', icon: Video },
  { id: 'quality', label: 'Calidad y reportes', icon: Activity },
]

export function Sidebar({ view, onChange }: { view: View; onChange: (view: View) => void }) {
  return (
    <aside className="sidebar">
      <div className="brand"><span><Stethoscope size={23} /></span><div><b>MediSalud</b><small>HIS local</small></div></div>
      <nav aria-label="Modulos principales">
        {items.map(({ id, label, icon: Icon }) => (
          <button className={view === id ? 'active' : ''} key={id} onClick={() => onChange(id)} title={label}>
            <Icon size={18} /><span>{label}</span>
          </button>
        ))}
      </nav>
      <div className="sidebar-footer"><span className="status-dot" /><div><b>Sede Quito</b><small>Operación local</small></div></div>
    </aside>
  )
}
