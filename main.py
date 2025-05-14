import os
import discord
from discord import Intents
import datetime
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve the bot token from the .env file
key = os.getenv("DISCORD_BOT_TOKEN")

# Check if key is available, otherwise terminate the program
if not key:
    print("Bot token not found in .env file. Exiting...")
    exit()

loggeduser = os.getlogin()

# Determine the correct download path based on the operating system
if os.name == 'nt':  # Windows
    path = f"C:\\Users\\{loggeduser}\\Downloads"
elif os.name == 'posix':  # Linux or macOS
    path = f"/home/{loggeduser}/Downloads"

# Set up intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Enable this to read the content of messages

# Initialize the client
client = discord.Client(intents=intents)

# Function to generate HTML
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

# Function to download attachments
async def download_attachment(attachment, channel_path, message_id):
    attachment_path = os.path.join(channel_path, f"{message_id}_{attachment.filename}")
    print(f"    Downloading attachment: {attachment.filename}")
    await attachment.save(attachment_path)

# Function to save individual messages
async def save_message(message, channel_path):
    message_file = os.path.join(channel_path, f"{message.id}.txt")
    with open(message_file, "w", encoding="utf-8") as f:
        f.write(f"{message.author}: {message.content}\n")
    print(f"    Saving message {message.id} from {message.author}")
    
    for attachment in message.attachments:
        await download_attachment(attachment, channel_path, message.id)

# Function to download a channel's history
async def download_channel(channel, guild_path):
    print(f"  Processing channel: {channel.name}")
    channel_path = os.path.join(guild_path, channel.name)
    os.makedirs(channel_path, exist_ok=True)
    
    existing_message_ids = set()
    if os.path.exists(channel_path):
        for file in os.listdir(channel_path):
            if file.endswith(".txt"):
                existing_message_ids.add(file.split(".")[0])
    
    messages = []
    async for message in channel.history(limit=None, oldest_first=True):
        if str(message.id) not in existing_message_ids:
            await save_message(message, channel_path)
        messages.append(message)
    
    generate_html(channel_path, messages)

# Function to download a server's data
async def download_server(guild):
    print(f"Processing server: {guild.name}")
    guild_path = os.path.join(path, guild.name)
    os.makedirs(guild_path, exist_ok=True)
    
    for channel in guild.text_channels:
        try:
            await download_channel(channel, guild_path)
        except discord.Forbidden:
            print(f"  No access to channel: {channel.name}, this may be intended")
        except Exception as e:
            print(f"  Error in channel {channel.name}: {e}")

# Function to download all media and messages from all servers
async def DownloadAllMediaAndMessages():
    for guild in client.guilds:
        await download_server(guild)

# Event handler when the bot is ready
@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")
    await DownloadAllMediaAndMessages()
    await client.close()

# Run the bot
client.run(key)

