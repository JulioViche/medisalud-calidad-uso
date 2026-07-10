import { Activity, CalendarDays, ClipboardPlus, HeartPulse, Home, LogOut, Pill, Receipt, Stethoscope, Video } from 'lucide-react'
import { allowedViews, type SessionUser } from '../auth'

export type View = 'home' | 'appointments' | 'hce' | 'nursing' | 'pharmacy' | 'billing' | 'telemedicine' | 'quality'

const items: { id: View; label: string; icon: typeof Activity }[] = [
  { id: 'home', label: 'Inicio', icon: Home },
  { id: 'appointments', label: 'Citas y admision', icon: CalendarDays },
  { id: 'hce', label: 'Historia clinica', icon: ClipboardPlus },
  { id: 'nursing', label: 'Enfermeria', icon: HeartPulse },
  { id: 'pharmacy', label: 'Farmacia', icon: Pill },
  { id: 'billing', label: 'Facturacion', icon: Receipt },
  { id: 'telemedicine', label: 'Telemedicina', icon: Video },
  { id: 'quality', label: 'Reportes operativos', icon: Activity },
]

export function Sidebar({ view, user, onChange, onLogout }: { view: View; user: SessionUser; onChange: (view: View) => void; onLogout: () => void }) {
  const visibleItems = items.filter((item) => allowedViews(user.role).includes(item.id))
  return (
    <aside className="sidebar">
      <div className="brand"><span><Stethoscope size={23} /></span><div><b>MediSalud</b><small>HIS local</small></div></div>
      <nav aria-label="Modulos principales">
        {visibleItems.map(({ id, label, icon: Icon }) => (
          <button className={view === id ? 'active' : ''} key={id} onClick={() => onChange(id)} title={label}>
            <Icon size={18} /><span>{label}</span>
          </button>
        ))}
      </nav>
      <div className="sidebar-footer"><span className="status-dot" /><div><b>Sede {user.site}</b><small>Operación local</small></div><button onClick={onLogout} title="Cerrar sesión"><LogOut size={17} /></button></div>
    </aside>
  )
}
