const data = window.dashboardData
const metrics = data.metrics
const incidents = data.incidents

const metricDetails = {
  'M-EFI-01': ['Duraciones de guardado HCE', 'Eventos HCE ordenados', 'Percentil 90'],
  'M-EFE-01': ['Citas completadas', 'Intentos de agendamiento', '(A / B) × 100'],
  'M-RIE-01': ['Facturaciones con error', 'Facturaciones procesadas', '(A / B) × 100'],
  'M-SAT-01': ['Encuestas abandonadas', 'Encuestas iniciadas', '(A / B) × 100'],
  'M-CC-01': ['Promedio HCE por sede', 'Cinco sedes evaluadas', 'Desviación estándar'],
  'M-RIE-02': ['Incidentes de privacidad', 'Dataset de incidentes', 'Conteo de casos'],
  'M-SAT-02': ['Suma de puntuaciones CSAT', 'Encuestas respondidas', 'A / B'],
  'M-EFE-02': ['Recetas correctas', 'Recetas generadas', '(A / B) × 100'],
  'M-EFI-02': ['Duraciones de carga', 'Eventos ordenados', 'Percentil 90'],
  'M-CC-02': ['Teleconsultas interrumpidas', 'Teleconsultas iniciadas', '(A / B) × 100']
}

const statusOrder = ['ROJO', 'AMARILLO', 'VERDE']
const statusColors = { ROJO: '#b94138', AMARILLO: '#ad7900', VERDE: '#28794f' }
const monthNames = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
const className = value => value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/\s+/g, '-')
const display = value => value.replaceAll('<=', '≤').replaceAll('>=', '≥')
const counts = (rows, key) => rows.reduce((result, row) => (result[row[key]] = (result[row[key]] || 0) + 1, result), {})
const orderedEntries = object => Object.entries(object).sort((a, b) => b[1] - a[1])

function setupTabs() {
  const activate = (name, updateHash = true) => {
    const selected = document.querySelector(`.tab[data-tab="${name}"]`) || document.querySelector('.tab[data-tab="overview"]')
    document.querySelectorAll('.tab').forEach(tab => { tab.classList.toggle('active', tab === selected); tab.setAttribute('aria-selected', tab === selected) })
    document.querySelectorAll('.tab-panel').forEach(panel => { const active = panel.id === `${selected.dataset.tab}-panel`; panel.classList.toggle('active', active); panel.hidden = !active })
    if (updateHash) history.replaceState(null, '', `#${selected.dataset.tab}`)
  }
  document.querySelectorAll('.tab').forEach(button => button.addEventListener('click', () => activate(button.dataset.tab)))
  activate(location.hash.slice(1) || 'overview', false)
}

function renderHeader() {
  document.querySelector('#summary-text').textContent = `${data.incidentCount.toLocaleString('es-EC')} incidentes clasificados y ${metrics.length} KPI calculados para el periodo ${data.dateRange.start} a ${data.dateRange.end}.`
  document.querySelector('#source-footer').textContent = `Datos generados desde ${data.generatedFrom.length} fuentes versionadas`
  document.querySelector('#status-summary').innerHTML = statusOrder.map(status => {
    const total = metrics.filter(metric => metric.status === status).length
    return `<article class="status-card ${className(status)}"><span>${status}</span><strong>${total}</strong><small>KPI</small></article>`
  }).join('')
}

function renderOverview() {
  const statusCounts = Object.fromEntries(statusOrder.map(status => [status, metrics.filter(metric => metric.status === status).length]))
  const redEnd = statusCounts.ROJO * 10
  const amberEnd = redEnd + statusCounts.AMARILLO * 10
  document.querySelector('#status-donut').style.background = `conic-gradient(${statusColors.ROJO} 0 ${redEnd}%, ${statusColors.AMARILLO} ${redEnd}% ${amberEnd}%, ${statusColors.VERDE} ${amberEnd}% 100%)`
  document.querySelector('#status-legend').innerHTML = statusOrder.map(status => `<div><i style="background:${statusColors[status]}"></i><span>${status.toLowerCase()}</span><strong>${statusCounts[status]}</strong><small>${statusCounts[status] * 10}%</small></div>`).join('')

  const characteristics = Array.from(new Set(metrics.map(metric => metric.characteristic)))
  document.querySelector('#characteristic-status-chart').innerHTML = characteristics.map(characteristic => {
    const group = metrics.filter(metric => metric.characteristic === characteristic)
    const segments = statusOrder.map(status => {
      const amount = group.filter(metric => metric.status === status).length
      return amount ? `<span style="--size:${amount};background:${statusColors[status]}" title="${amount} ${status.toLowerCase()}">${amount}</span>` : ''
    }).join('')
    return `<div class="bar-row"><b>${characteristic}</b><div>${segments}</div><strong>${group.length}</strong></div>`
  }).join('')

  document.querySelector('#metrics-grid').innerHTML = metrics.map(metric => {
    const details = metricDetails[metric.code]
    return `<article class="metric-card ${className(metric.status)}"><div class="metric-head"><span>${metric.code}</span><b>${metric.status}</b></div><p>${metric.characteristic}</p><h3>${metric.name}</h3><div class="metric-value">${metric.value}<small>${metric.unit}</small></div><div class="metric-meta"><span>Meta<strong>${display(metric.target)}</strong></span><span>Método<strong>${details[2]}</strong></span></div></article>`
  }).join('')

  const critical = metrics.filter(metric => metric.status === 'ROJO').map(metric => metric.name)
  document.querySelector('#decision-strip').innerHTML = `<strong>Prioridad de intervención</strong><p>${critical.join(' · ')}</p><span>${critical.length} KPI fuera del umbral crítico</span>`
}

function populateSelect(id, values) {
  const select = document.querySelector(id)
  Array.from(new Set(values)).sort().forEach(value => select.add(new Option(value, value)))
}

function filteredIncidents() {
  const selections = {
    site: document.querySelector('#site-filter').value,
    module: document.querySelector('#module-filter').value,
    role: document.querySelector('#role-filter').value,
    characteristic: document.querySelector('#incident-characteristic-filter').value
  }
  const query = document.querySelector('#incident-search').value.trim().toLowerCase()
  return incidents.filter(row => Object.entries(selections).every(([key, value]) => value === 'all' || row[key] === value) && (!query || `${row.id} ${row.description}`.toLowerCase().includes(query)))
}

function rankingBars(rows, key, target, limit = 9) {
  const entries = orderedEntries(counts(rows, key)).slice(0, limit)
  const max = entries[0]?.[1] || 1
  document.querySelector(target).innerHTML = entries.length ? entries.map(([label, value]) => `<div class="rank-row"><span title="${label}">${label}</span><div><i style="width:${value * 100 / max}%"></i></div><strong>${value.toLocaleString('es-EC')}</strong></div>`).join('') : '<p class="empty-state">No existen registros para los filtros seleccionados.</p>'
}

function renderMonthlyChart(rows) {
  const totals = counts(rows, 'month')
  const months = Array.from({ length: 12 }, (_, index) => `2025-${String(index + 1).padStart(2, '0')}`)
  const values = months.map(month => totals[month] || 0)
  const max = Math.max(...values, 1)
  const width = 900, height = 230, left = 42, right = 18, top = 18, bottom = 35
  const x = index => left + index * (width - left - right) / 11
  const y = value => top + (max - value) * (height - top - bottom) / max
  const points = values.map((value, index) => `${x(index)},${y(value)}`).join(' ')
  const area = `${left},${height - bottom} ${points} ${width - right},${height - bottom}`
  const grid = [0, .5, 1].map(ratio => { const value = Math.round(max * ratio); return `<line x1="${left}" y1="${y(value)}" x2="${width - right}" y2="${y(value)}"/><text x="${left - 8}" y="${y(value) + 4}" text-anchor="end">${value}</text>` }).join('')
  const labels = months.map((_, index) => `<text x="${x(index)}" y="${height - 9}" text-anchor="middle">${monthNames[index]}</text>`).join('')
  const dots = values.map((value, index) => `<circle cx="${x(index)}" cy="${y(value)}" r="4"><title>${monthNames[index]}: ${value}</title></circle>`).join('')
  document.querySelector('#monthly-chart').innerHTML = `<svg viewBox="0 0 ${width} ${height}" preserveAspectRatio="none"><g class="grid-lines">${grid}${labels}</g><polygon points="${area}"/><polyline points="${points}"/>${dots}</svg>`
  document.querySelector('#trend-total').textContent = `${rows.length.toLocaleString('es-EC')} incidentes filtrados`
}

function renderIncidentTable(rows) {
  document.querySelector('#incident-result-count').textContent = `${rows.length.toLocaleString('es-EC')} resultados`
  document.querySelector('#incident-table').innerHTML = rows.slice(0, 50).map(row => `<tr><td><strong>${row.id}</strong></td><td>${row.date}</td><td>${row.module}</td><td>${row.description}</td><td>${row.role}</td><td>${row.site}</td><td><span class="classification">${row.characteristic}</span></td></tr>`).join('')
}

function renderIncidentStats(rows) {
  const risk = rows.filter(row => row.characteristic === 'Libertad de Riesgo').length
  const sites = new Set(rows.map(row => row.site)).size
  const modules = new Set(rows.map(row => row.module)).size
  document.querySelector('#incident-stats').innerHTML = `<article><span>Registros filtrados</span><strong>${rows.length.toLocaleString('es-EC')}</strong></article><article><span>Libertad de riesgo</span><strong>${risk.toLocaleString('es-EC')}</strong></article><article><span>Sedes representadas</span><strong>${sites}</strong></article><article><span>Módulos representados</span><strong>${modules}</strong></article>`
}

function updateIncidentView() {
  const rows = filteredIncidents()
  renderIncidentStats(rows)
  renderMonthlyChart(rows)
  rankingBars(rows, 'module', '#module-chart')
  rankingBars(rows, 'characteristic', '#incident-characteristic-chart', 5)
  renderIncidentTable(rows)
}

function setupIncidentView() {
  populateSelect('#site-filter', incidents.map(row => row.site))
  populateSelect('#module-filter', incidents.map(row => row.module))
  populateSelect('#role-filter', incidents.map(row => row.role))
  populateSelect('#incident-characteristic-filter', incidents.map(row => row.characteristic))
  document.querySelectorAll('.filters select').forEach(select => select.addEventListener('change', updateIncidentView))
  document.querySelector('#incident-search').addEventListener('input', updateIncidentView)
  document.querySelector('#reset-filters').addEventListener('click', () => {
    document.querySelectorAll('.filters select').forEach(select => { select.value = 'all' })
    document.querySelector('#incident-search').value = ''
    updateIncidentView()
  })
  updateIncidentView()
}

function renderMethod() {
  document.querySelector('#formula-table').innerHTML = metrics.map(metric => {
    const [a, b, formula] = metricDetails[metric.code]
    return `<tr><td><strong>${metric.code}</strong></td><td>${metric.name}<small>${metric.value} ${metric.unit} · meta ${display(metric.target)}</small></td><td>${metric.characteristic}</td><td>${a}</td><td>${b}</td><td><code>${formula}</code></td><td><code>${metric.source}</code></td></tr>`
  }).join('')
}

setupTabs()
renderHeader()
renderOverview()
setupIncidentView()
renderMethod()
