export function Architecture() {
  return (
    <>
      <header className="page-header"><div><p className="eyebrow">CONTEXTO TECNOLOGICO</p><h1>Arquitectura MediSalud HIS</h1><span>Representacion local del sistema descrito en el Documento Padre</span></div></header>
      <section className="architecture-layout"><img src="/architecture.png" alt="Arquitectura simplificada de MediSalud HIS" /><div className="architecture-notes"><h2>Capas implementadas</h2><dl><dt>Experiencia</dt><dd>React y Flutter</dd><dt>Entrada</dt><dd>Spring Cloud Gateway</dd><dt>Dominio</dt><dd>HCE, citas, facturacion y medicion</dd><dt>Datos</dt><dd>PostgreSQL, SQL Server y RabbitMQ</dd></dl></div></section>
    </>
  )
}

