import os
import discord
import src.html_files as html

class DiscordDownloader:
    def __init__(self, token: str, download_path: str):
        self.token = token
        self.download_path = download_path
 
        intents = discord.Intents.default()
        intents.messages = True
        intents.guilds = True
        intents.message_content = True
 
        self.client = discord.Client(intents=intents)
        self.client.event(self.on_ready)
 
    async def download_attachment(self, attachment, channel_path, message_id):
        attachment_path = os.path.join(channel_path, f"{message_id}_{attachment.filename}")
        print(f"    Downloading attachment: {attachment.filename}")
        await attachment.save(attachment_path)
 
    async def save_message(self, message, channel_path):
        message_file = os.path.join(channel_path, f"{message.id}.txt")
        with open(message_file, "w", encoding="utf-8") as f:
            f.write(f"{message.author}: {message.content}\n")
        print(f"    Saving message {message.id} from {message.author}")
 
        for attachment in message.attachments:
            await self.download_attachment(attachment, channel_path, message.id)
 
    async def download_channel(self, channel, guild_path):
        print(f"  Processing channel: {channel.name}")
        channel_path = os.path.join(guild_path, channel.name)
        os.makedirs(channel_path, exist_ok=True)
 
        existing_message_ids = set()
        for file in os.listdir(channel_path):
            if file.endswith(".txt"):
                existing_message_ids.add(file.split(".")[0])
 
        messages = []
        async for message in channel.history(limit=None, oldest_first=True):
            if str(message.id) not in existing_message_ids:
                await self.save_message(message, channel_path)
            messages.append(message)
 
        html.generate_html(channel_path, messages)
 
    async def download_server(self, guild):
        print(f"Processing server: {guild.name}")
        guild_path = os.path.join(self.download_path, guild.name)
        os.makedirs(guild_path, exist_ok=True)
 
        for channel in guild.text_channels:
            try:
                await self.download_channel(channel, guild_path)
            except discord.Forbidden:
                print(f"  [WARN] No access to channel: {channel.name}, this may be intended")
            except Exception as e:
                print(f"  [ERROR] while downloading channel {channel.name}: {e}")
            finally:
                channels = [c.name for c in guild.text_channels]
                html.generate_server_index(guild_path, channels)

    async def download_all(self):
        for guild in self.client.guilds:
            await self.download_server(guild)
 
    async def on_ready(self):
        print(f"Successfully logged in as {self.client.user}")
        await self.download_all()
        await self.client.close()
 
    def run(self):
        self.client.run(self.token)