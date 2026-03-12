import os

def generate_html(channel_path, messages):
    html_path = os.path.join(channel_path, "index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Channel Timeline</title></head><body>")
        f.write(f"<h1>Timeline for {os.path.basename(channel_path)}</h1>")
        for message in messages:
            f.write(f"<div><strong>{message.author}</strong>: {message.content}<br>")
            for attachment in message.attachments:
                attachment_path = f"{message.id}_{attachment.filename}"
                if attachment.filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
                    f.write(f'<img src="{attachment_path}" width="200"><br>')
                elif attachment.filename.lower().endswith('mp3') or attachment.filename.lower().endswith('ogg'):
                    f.write(f'<audio controls><source src="{attachment_path}" type="audio/mpeg">Your browser does not support the audio tag.</audio><br>')
                elif attachment.filename.lower().endswith('mp4'):
                    f.write(f'<video width="320" height="240" controls><source src="{attachment_path}" type="video/mp4">Your browser does not support the video tag.</video><br>')
            f.write(f"<small>{message.created_at}</small></div><hr>")
        f.write("</body></html>")