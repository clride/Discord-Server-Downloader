# Discord-Server-Downloader
 A utility that archives an entire discord server using a bot.
 You can use it to archive your old servers in a nice format if you're leaving discord
 or if you just want a backup of your memories.

 ![A channel overview](/doc/img/overview.png)
 
# Design
 Messages are plainly downloaded and rendered into a document for each channel to allow viewing of the channel timeline, including images, videos and audio messages.
 The program is designed to interact with your filesystem instead of with a database. You do not need any external software to view and preserve downloaded files.

 ![Show messages of a channel](/doc/img/channel.png)

# How to use
 The Discord Server Downloader is very easy to set up and use. All you need is a Discord bot token stored in a .env file. The bot will automatically download every Guild and Channel into it's own subfolders.
 
 ## Step 1: Setting up your bot
  Navigate to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new bot.
  Now give it intents to:
   - Read Message History
   - View all Servers
   - View all channels
   Go to the bot tab and copy your token.

 ## Step 2: Installing dependencies
 Run ```pip install -r pip.txt``` to automatically install all dependencies
 of the project.
 
 ## Step 3: running
 Simply run the program using ```python main.py -t [YOUR TOKEN HERE]```

The server will now be downloaded to your downloads folder. Navigate into
the newly created directory and access it under index.html.