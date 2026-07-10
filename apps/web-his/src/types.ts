export type Metric = {
  code: string
  name: string
  characteristic: string
  value: string | number
  unit: string
  target: string
  status: 'VERDE' | 'AMARILLO' | 'ROJO'
  source: string
}

export type DashboardSummary = {
  period: string
  source: string
  incident_count: number
  metrics: Metric[]
  status_summary: Record<string, number>
  incidents_by_characteristic: Record<string, number>
  incidents_by_module: Record<string, number>
}

export type Incident = {
  id: string
  fecha: string
  modulo: string
  descripcion: string
  rol_usuario: string
  sede: string
  characteristic: string
}

