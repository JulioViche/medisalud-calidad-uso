import type { DashboardSummary, Incident } from '../types'

const baseUrl = import.meta.env.VITE_API_URL ?? 'http://localhost:8080'

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${baseUrl}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options?.headers },
    ...options,
  })
  if (!response.ok) throw new Error(`HTTP ${response.status}`)
  return response.json() as Promise<T>
}

export const api = {
  dashboard: () => request<DashboardSummary>('/api/dashboard/resumen'),
  incidents: (limit = 8) => request<{ items: Incident[] }>(`/api/incidentes?limit=${limit}`),
  saveNote: (scenario: string) =>
    request<Record<string, unknown>>('/api/hce/notas', {
      method: 'POST',
      body: JSON.stringify({ patientId: 'PAC-001', doctorId: 'MED-104', site: 'Quito', text: 'Control de evolucion', scenario }),
    }),
  createInvoice: (scenario: string) =>
    request<Record<string, unknown>>('/api/facturacion', {
      method: 'POST',
      body: JSON.stringify({ transactionId: `TX-${Date.now()}`, patientId: 'PAC-001', amount: 148.5, site: 'Quito', scenario }),
    }),
}

