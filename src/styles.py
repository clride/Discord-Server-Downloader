CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Instrument+Serif:ital@0;1&display=swap');

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #1a1c22;
    --surface: #22252d;
    --surface-hover: #282b35;
    --border: #353a45;
    --accent: #6e7ff5;
    --accent-dim: #3a4080;
    --text: #e2e4ea;
    --muted: #8b93a5;
    --author: #b8c4ff;
    --timestamp: #606878;
    --img-radius: 8px;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
    line-height: 1.6;
    min-height: 100vh;
  }

  header {
    position: sticky;
    top: 0;
    z-index: 10;
    background: rgba(26, 28, 34, 0.88);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border);
    padding: 18px 32px;
  }

  header h1 {
    font-family: 'Instrument Serif', serif;
    font-style: italic;
    font-size: 22px;
    font-weight: 400;
    color: #fff;
    letter-spacing: -0.3px;
  }

  header h1 span { color: var(--accent); font-style: normal; }

  .feed {
    max-width: 760px;
    margin: 0 auto;
    padding: 32px 24px 80px;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .message {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 14px 18px;
    transition: border-color 0.15s, background 0.15s;
    animation: fadeUp 0.3s ease both;
  }

  .message:hover {
    border-color: var(--accent-dim);
    background: var(--surface-hover);
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .message-header {
    display: flex;
    align-items: baseline;
    gap: 10px;
    margin-bottom: 6px;
  }

  .author {
    font-weight: 600;
    color: var(--author);
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }

  .timestamp { font-size: 11px; color: var(--timestamp); }
  .content { color: var(--text); word-break: break-word; }

  .attachments {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 10px;
  }

  .attachments img {
    width: 200px;
    height: auto;
    border-radius: var(--img-radius);
    border: 1px solid var(--border);
    object-fit: cover;
    cursor: zoom-in;
    transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
  }

  .attachments img:hover {
    transform: scale(1.03);
    border-color: var(--accent);
    box-shadow: 0 4px 20px rgba(110, 127, 245, 0.25);
  }

  audio, video {
    display: block;
    margin-top: 8px;
    border-radius: 6px;
    width: 100%;
    max-width: 420px;
    accent-color: var(--accent);
  }

  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border) 30%, var(--border) 70%, transparent);
    margin: 2px 0;
    opacity: 0.5;
  }

  /* Lightbox */
  #lightbox {
    display: none;
    position: fixed;
    inset: 0;
    z-index: 1000;
    background: rgba(10, 11, 14, 0.92);
    backdrop-filter: blur(8px);
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 18px;
    cursor: zoom-out;
  }

  #lightbox.active { display: flex; }

  #lightbox img {
    max-width: 90vw;
    max-height: 80vh;
    border-radius: 10px;
    border: 1px solid var(--border);
    box-shadow: 0 24px 80px rgba(0,0,0,0.7);
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    transform-origin: center;
    user-select: none;
  }

  .lightbox-controls {
    display: flex;
    gap: 12px;
    cursor: default;
  }

  .lightbox-btn {
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    transition: background 0.15s, border-color 0.15s, color 0.15s;
    letter-spacing: 0.04em;
  }

  .lightbox-btn:hover {
    background: var(--surface-hover);
    border-color: var(--accent);
    color: var(--author);
  }

  .lightbox-hint {
    font-size: 11px;
    color: var(--timestamp);
    letter-spacing: 0.05em;
  }
</style>
"""

INDEX_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Instrument+Serif:ital@0;1&display=swap');

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #1a1c22;
    --surface: #22252d;
    --surface-hover: #282b35;
    --border: #353a45;
    --accent: #6e7ff5;
    --accent-dim: #3a4080;
    --text: #e2e4ea;
    --muted: #8b93a5;
    --author: #b8c4ff;
    --timestamp: #606878;
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
    line-height: 1.6;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 48px 24px;
  }

  .index-wrap {
    width: 100%;
    max-width: 520px;
  }

  h1 {
    font-family: 'Instrument Serif', serif;
    font-style: italic;
    font-size: 28px;
    font-weight: 400;
    color: #fff;
    margin-bottom: 6px;
  }

  h1 span { color: var(--accent); font-style: normal; }

  .subtitle {
    font-size: 11px;
    color: var(--timestamp);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 32px;
  }

  .channel-list {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .channel-link {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px 16px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    text-decoration: none;
    color: var(--text);
    transition: background 0.15s, border-color 0.15s, color 0.15s;
    animation: fadeUp 0.3s ease both;
  }

  .channel-link:hover {
    background: var(--surface-hover);
    border-color: var(--accent);
    color: #fff;
  }

  .channel-link:hover .hash { color: var(--accent); }

  .hash {
    color: var(--muted);
    font-size: 15px;
    transition: color 0.15s;
    user-select: none;
  }

  .channel-name { flex: 1; }

  .arrow {
    color: var(--timestamp);
    font-size: 11px;
    transition: color 0.15s, transform 0.15s;
  }

  .channel-link:hover .arrow {
    color: var(--accent);
    transform: translateX(3px);
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
  }
</style>
"""

JS = """
<script>
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  let currentRotation = 0;

  function openLightbox(src) {
    currentRotation = 0;
    lightboxImg.src = src;
    lightboxImg.style.transform = 'rotate(0deg)';
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox(e) {
    if (e.target === lightbox || e.target.id === 'lightbox-close') {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  function rotateImage(deg) {
    currentRotation = (currentRotation + deg + 360) % 360;
    lightboxImg.style.transform = `rotate(${currentRotation}deg)`;
  }

  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    if (e.key === 'Escape') {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
    }
    if (e.key === 'ArrowLeft')  rotateImage(-90);
    if (e.key === 'ArrowRight') rotateImage(90);
  });

  document.querySelectorAll('.attachments img').forEach(img => {
    img.addEventListener('click', () => openLightbox(img.src));
  });
</script>
"""