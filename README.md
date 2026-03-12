# Discord-Server-Downloader
 Archive your entire server in minutes. Downloaded channels are rendered neatly into HTML documents. No external software required

 ![A channel overview](/doc/img/overview.png)
 
# Design
 Images, videos, audio messages and standard messages are downladed and embedded. There's no telemetry and the bot never sends a message to  your server, so you can use it as often as you want without it spamming your server.

 ![Show messages of a channel](/doc/img/channel.png)
 
# How to use
 The tool is very easy to set up and use. All you need is a [discord bot configured with the correct intents](https://discord.com/developers/applications). The bot will automatically detect every server it has access to and start downloading immediately.
 
 ## Step 1: Setting up your bot
  Navigate to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new bot.
  Now give it intents to:
   - Read Message History
   - View all Servers
   - View all channels

   Be sure your bot has access to every server you want to download.
   When you're done, grab your bot token and move on.
   

 ## Step 2: Installing dependencies
 Run ```pip install -r pip.txt``` to automatically install all dependencies
 of the project.
 
 ## Step 3: running
 Simply run the program using ```python main.py -t [YOUR TOKEN HERE]```

The server will now be downloaded to your downloads folder. Open the index.html file at the root of the new directory. Enjoy!
