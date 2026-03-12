import os
from src.styles import CSS, JS, INDEX_CSS


IMAGE_EXTENSIONS = ('png', 'jpg', 'jpeg', 'gif', 'webp')
AUDIO_EXTENSIONS = ('mp3', 'ogg')
VIDEO_EXTENSIONS = ('mp4',)


def generate_server_index(server_path, channel_names):
    """Generate a top-level index.html listing all channels."""
    html_path = os.path.join(server_path, "index.html")
    server_name = os.path.basename(server_path)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{server_name} — Channels</title>
  {INDEX_CSS}
</head>
<body>
  <div class="index-wrap">
    <h1><span></span> {server_name}</h1>
    <p class="subtitle">{len(channel_names)} channel{"s" if len(channel_names) != 1 else ""} archived</p>
    <div class="channel-list">
""")
        for i, name in enumerate(sorted(channel_names)):
            delay = f'animation-delay: {i * 40}ms'
            f.write(f'      <a class="channel-link" href="{name}/index.html" style="{delay}">\n')
            f.write(f'        <span class="hash">#</span>\n')
            f.write(f'        <span class="channel-name">{name}</span>\n')
            f.write(f'        <span class="arrow">→</span>\n')
            f.write(f'      </a>\n')

        f.write("    </div>\n  </div>\n</body>\n</html>")


def generate_html(channel_path, messages):
    channel_name = os.path.basename(channel_path)
    html_path = os.path.join(channel_path, "index.html")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{channel_name} — Timeline</title>
  {CSS}
</head>
<body>

  <header>
    <a class="back-link" href="../index.html">← all channels</a>
    <h1><span>#</span> {channel_name}</h1>
  </header>

  <!-- Lightbox -->
  <div id="lightbox" onclick="closeLightbox(event)">
    <img id="lightbox-img" src="" alt="Expanded attachment">
    <div class="lightbox-controls" onclick="event.stopPropagation()">
      <button class="lightbox-btn" onclick="rotateImage(-90)">↺ rotate left</button>
      <button class="lightbox-btn" onclick="rotateImage(90)">↻ rotate right</button>
      <button class="lightbox-btn" id="lightbox-close" onclick="document.getElementById('lightbox').classList.remove('active'); document.body.style.overflow=''">✕ close</button>
    </div>
    <span class="lightbox-hint">esc to close · ← → arrow keys to rotate</span>
  </div>

  <main class="feed">
""")

        for i, message in enumerate(messages):
            f.write(f'    <div class="message">\n')
            f.write(f'      <div class="message-header">\n')
            f.write(f'        <span class="author">{message.author}</span>\n')
            f.write(f'        <span class="timestamp">{message.created_at}</span>\n')
            f.write(f'      </div>\n')
            f.write(f'      <div class="content">{message.content}</div>\n')

            if message.attachments:
                f.write('      <div class="attachments">\n')
                for attachment in message.attachments:
                    local_path = os.path.join(channel_path, f"{message.id}_{attachment.filename}")
                    src = f"{message.id}_{attachment.filename}" if os.path.exists(local_path) else attachment.url
                    ext = attachment.filename.lower().rsplit('.', 1)[-1]
                    if ext in IMAGE_EXTENSIONS:
                        f.write(f'        <img src="{src}" loading="lazy" alt="{attachment.filename}">\n')
                    elif ext in AUDIO_EXTENSIONS:
                        mime = "audio/ogg" if ext == "ogg" else "audio/mpeg"
                        f.write(f'        <audio controls><source src="{src}" type="{mime}"></audio>\n')
                    elif ext in VIDEO_EXTENSIONS:
                        f.write(f'        <video controls><source src="{src}" type="video/mp4"></video>\n')
                f.write('      </div>\n')

            f.write('    </div>\n')

            if i < len(messages) - 1:
                f.write('    <div class="divider"></div>\n')

        f.write("  </main>\n")
        f.write(f"  {JS}\n")
        f.write("</body>\n</html>")