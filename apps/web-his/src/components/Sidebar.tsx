import { Activity, CalendarDays, ClipboardPlus, FileText, LayoutDashboard, Pill, Receipt, Settings2, Stethoscope } from 'lucide-react'

export type View = 'dashboard' | 'hce' | 'appointments' | 'billing' | 'pharmacy' | 'architecture'

const items: { id: View; label: string; icon: typeof Activity }[] = [
  { id: 'dashboard', label: 'Calidad en uso', icon: LayoutDashboard },
  { id: 'hce', label: 'Historia clinica', icon: ClipboardPlus },
  { id: 'appointments', label: 'Citas y admision', icon: CalendarDays },
  { id: 'billing', label: 'Facturacion', icon: Receipt },
  { id: 'pharmacy', label: 'Farmacia', icon: Pill },
  { id: 'architecture', label: 'Arquitectura', icon: Settings2 },
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
      <div className="sidebar-footer"><FileText size={16} /><span>ISO/IEC 25022</span></div>
    </aside>
  )
}

