const features = [
  { number: "01", title: "Find the moments", description: "Identify promising segments from long-form recordings." },
  { number: "02", title: "Shape every clip", description: "Prepare vertical, square, and landscape formats." },
  { number: "03", title: "Make it accessible", description: "Create accurate captions and editable subtitles." },
];

export default function Home() {
  return (
    <main className="shell">
      <nav className="nav">
        <a className="brand" href="#"><span className="brand-mark">C</span> clipforge<span className="brand-ai">AI</span></a>
        <span className="phase">EARLY ACCESS · PHASE 1</span>
      </nav>

      <section className="hero">
        <div className="eyebrow"><span className="pulse" /> YOUR VIDEO WORKSPACE</div>
        <h1>One video.<br /><span>Many great moments.</span></h1>
        <p className="intro">A thoughtful workspace for turning long-form video into short, shareable stories. Bring your footage; choose how it gets processed.</p>
        <div className="actions">
          <a className="primary" href="#workflow">Explore the workflow <span>↗</span></a>
          <span className="local-note"><span className="dot" /> Local-first · Cloud when you choose</span>
        </div>
        <div className="preview">
          <div className="preview-top"><span>CLIPFORGE / WORKSPACE</span><span className="status">● SYSTEM READY</span></div>
          <div className="preview-content">
            <div className="preview-copy"><span className="mini-label">YOUR NEXT EDIT STARTS HERE</span><h2>Make more<br />from every minute.</h2><p>Import a video to begin building your clip library.</p></div>
            <div className="video-card"><div className="play">▶</div><span>VIDEO INPUT</span><strong>Upload · URL · Cloud</strong><small>Ingestion interface coming next</small></div>
          </div>
          <div className="preview-bottom"><span>01 / INGEST</span><span>02 / DISCOVER</span><span>03 / CREATE</span><span>04 / EXPORT</span></div>
        </div>
      </section>

      <section className="workflow" id="workflow">
        <div className="section-heading"><span>THE WORKFLOW</span><p>Built around your creative process.</p></div>
        <div className="feature-grid">{features.map((feature) => <article className="feature" key={feature.number}><span>{feature.number}</span><h3>{feature.title}</h3><p>{feature.description}</p></article>)}</div>
      </section>
      <footer><span>CLIPFORGE AI</span><span>CREATE WITH INTENTION.</span></footer>
    </main>
  );
}
