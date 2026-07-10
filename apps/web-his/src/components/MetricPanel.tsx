import { Activity, Clock3, ShieldAlert, Video } from 'lucide-react'
import type { Metric } from '../types'
import { StatusBadge } from './StatusBadge'

const icons = [Clock3, Activity, ShieldAlert, Video]

export function MetricPanel({ metric, index }: { metric: Metric; index: number }) {
  const Icon = icons[index % icons.length]
  return (
    <article className="metric-panel">
      <div className="metric-heading"><span className="metric-icon"><Icon size={18} /></span><StatusBadge status={metric.status} /></div>
      <strong>{metric.value}<small>{metric.unit}</small></strong>
      <p>{metric.name}</p>
      <div className="metric-target"><span>Meta</span><b>{metric.target}</b></div>
    </article>
  )
}

