import type { View } from './components/Sidebar'

export type UserRole = 'doctor' | 'nursing' | 'admission' | 'pharmacy' | 'management'

export type SessionUser = {
  email: string
  name: string
  initials: string
  role: UserRole
  roleLabel: string
  site: string
}

export const DEMO_PASSWORD = 'Medisalud2025'

export const demoUsers: SessionUser[] = [
  { email: 'medico@medisalud.local', name: 'Dra. María Cárdenas', initials: 'MC', role: 'doctor', roleLabel: 'Medicina interna', site: 'Quito' },
  { email: 'enfermeria@medisalud.local', name: 'Lic. Elena Ruiz', initials: 'ER', role: 'nursing', roleLabel: 'Enfermería', site: 'Quito' },
  { email: 'admision@medisalud.local', name: 'Andrés Vega', initials: 'AV', role: 'admission', roleLabel: 'Admisión', site: 'Quito' },
  { email: 'farmacia@medisalud.local', name: 'Q.F. Lucía Mora', initials: 'LM', role: 'pharmacy', roleLabel: 'Farmacia', site: 'Quito' },
  { email: 'gerencia@medisalud.local', name: 'Ing. Daniel Paz', initials: 'DP', role: 'management', roleLabel: 'Gerencia', site: 'Matriz' },
]

const permissions: Record<UserRole, View[]> = {
  doctor: ['home', 'hce', 'appointments', 'telemedicine'],
  nursing: ['home', 'nursing', 'hce'],
  admission: ['home', 'appointments', 'billing'],
  pharmacy: ['home', 'pharmacy'],
  management: ['home', 'quality'],
}

export function authenticate(email: string, password: string): SessionUser | null {
  if (password !== DEMO_PASSWORD) return null
  return demoUsers.find((user) => user.email === email.trim().toLowerCase()) ?? null
}

export function allowedViews(role: UserRole): View[] {
  return permissions[role]
}

export function canAccess(role: UserRole, view: View): boolean {
  return permissions[role].includes(view)
}
