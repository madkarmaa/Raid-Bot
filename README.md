# Discord Raid Bot
Just a bad made Discord bot for raids, built in [discord.py](https://discordpy.readthedocs.io/en/stable/index.html).
## Commands
### (callable by the prefix ">" or by mentioning the bot)
### ping
(_Example: >ping_)

Check the bot's latency.

### nuke [your Discord ID]
(_Example: >nuke 123456789_)

Deletes all roles and channels, changes the server name and creates random channels within mentioning **@everyone**.

### nukestop
(_Example: >nukestop_)

Stops the nuke command.
## Important
Remember to provide your [**Discord ID**](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) and your [**bot's token**](https://discord.com/developers/applications) before executing the script.
```py
allowed_users = "YOUR DISCORD ID HERE"
```
```py
bot.run('BOT TOKEN HERE')
```
Your Discord ID is required to prevent other users to interact with the bot.
