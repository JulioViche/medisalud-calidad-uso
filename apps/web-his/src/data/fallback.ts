import type { DashboardSummary, Incident } from '../types'

export const fallbackSummary: DashboardSummary = {
  period: '2025-01-01/2025-12-31',
  source: 'Simulacion academica local',
  incident_count: 3000,
  status_summary: { VERDE: 2, AMARILLO: 4, ROJO: 4 },
  incidents_by_characteristic: { Efectividad: 1380, Eficiencia: 490, Satisfaccion: 160, 'Libertad de Riesgo': 710, 'Cobertura de Contexto': 260 },
  incidents_by_module: { HCE: 769, 'Portal Citas': 545, Facturacion: 425, Telemedicina: 320, 'App Movil': 278, Farmacia: 258, Laboratorio: 166, Imagenologia: 151, Reportes: 88 },
  metrics: [
    { code: 'M-EFI-01', name: 'P90 registro HCE', characteristic: 'Eficiencia', value: 11.71, unit: 'segundos', target: '<= 8', status: 'AMARILLO', source: 'events:hce_save' },
    { code: 'M-EFE-01', name: 'Exito de agendamiento', characteristic: 'Efectividad', value: 87.86, unit: '%', target: '>= 95', status: 'AMARILLO', source: 'events:appointment' },
    { code: 'M-RIE-01', name: 'Errores de facturacion', characteristic: 'Libertad de Riesgo', value: 4.5, unit: '%', target: '< 1', status: 'ROJO', source: 'events:billing' },
    { code: 'M-CC-02', name: 'Caidas de teleconsulta', characteristic: 'Cobertura de Contexto', value: 9.4, unit: '%', target: '< 5', status: 'AMARILLO', source: 'events:teleconsultation' },
  ],
}

export const fallbackIncidents: Incident[] = [
  { id: '3846', fecha: '11/14/2025', modulo: 'HCE', descripcion: 'Datos de otro paciente visibles brevemente al abrir un expediente', rol_usuario: 'Medico', sede: 'Quito', characteristic: 'Libertad de Riesgo' },
  { id: '2091', fecha: '08/07/2025', modulo: 'Portal Citas', descripcion: 'Usuario no logra agendar tras tres intentos', rol_usuario: 'Paciente', sede: 'Guayaquil', characteristic: 'Efectividad' },
  { id: '2718', fecha: '10/12/2025', modulo: 'Facturacion', descripcion: 'Factura duplicada al reintentar pago', rol_usuario: 'Admision', sede: 'Cuenca', characteristic: 'Libertad de Riesgo' },
  { id: '3170', fecha: '12/02/2025', modulo: 'Telemedicina', descripcion: 'Videollamada se corta durante la consulta', rol_usuario: 'Paciente', sede: 'Manta', characteristic: 'Cobertura de Contexto' },
]

