import type { Metric } from '../types'

export function StatusBadge({ status }: Pick<Metric, 'status'>) {
  return <span className={`status-badge status-${status.toLowerCase()}`}>{status}</span>
}

