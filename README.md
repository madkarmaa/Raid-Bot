# Raid-Bot
Just a bad made Discord bot for raids, built in discord.py
## Commands
### (callable by the prefix ">" or by mentioning the bot)
### ping
Check the bot's latency

### nuke [your Discord ID]
_(Provide your Discord ID after the command)_
Deletes all roles and channels, changes the server name and creates random channels within mentioning @everyone

### nukestop
Stops the nuke command
## Important
Remember to provide your [**Discord ID**](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) and your [**bot's token**](https://discord.com/developers/applications) before executing the script.
```py
allowed_users = "YOUR DISCORD ID HERE"
```
```py
bot.run('BOT TOKEN HERE')
```
Your Discord ID is required to prevent other users to interact with the bot.
