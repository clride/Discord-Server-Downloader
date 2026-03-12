# Discord-Server-Downloader
 A utility that archives an entire discord server using a bot.
 You can use it to archive your old servers in a nice format if you're leaving discord
 or if you just want a backup of your memories.

 ![A channel overview](/doc/img/overview.png)
 
# Design
 Messages are plainly downloaded and rendered into a document for each channel to allow viewing of the channel timeline, including images, videos and audio messages.
 The program is designed to interact with your filesystem instead of a database. You do not need any external software to view and preserve downloaded files.

 ![Show messages of a channel](/doc/img/channel.png)

# How to use
 The tool is very easy to set up and use. All you need is a [discord bot configured with the correct intents](https://discord.com/developers/applications). The bot will automatically detect every server it has access to and start downloading immediately.
 
 ## Step 1: Setting up your bot
  Navigate to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new bot.
  Now give it intents to:
   - Read Message History
   - View all Servers
   - View all channels
   Go to the bot tab and copy your token.
   Be sure your bot has access to every server you want to download.

 ## Step 2: Installing dependencies
 Run ```pip install -r pip.txt``` to automatically install all dependencies
 of the project.
 
 ## Step 3: running
 Simply run the program using ```python main.py -t [YOUR TOKEN HERE]```

The server will now be downloaded to your downloads folder. Navigate into
the newly created directory and access it under index.html.
