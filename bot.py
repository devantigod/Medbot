# imports

import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.message_content = True

# prefix

bot = commands.Bot(command_prefix='+', intents=intents)

# setup & status

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'meds22 made this')
    await bot.change_presence(activity=discord.Streaming(name="/supraK", url="https://www.twitch.tv/discord.gg/supraK"))

# Answer ping

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user.mentioned_in(message):
        response = [
            f'**My prefix is "+"**',
            '```If you would like to purchase with robux use "+buyrobux"',
            'If you would like to purchase using paypal use "+buypaypal"```'
        ]

        await message.channel.send('\n'.join(response))

    # Robux command

    if message.content.startswith('+buyrobux'):
        normal_message = "**Make sure to record your purchase and send it here once completed; failing to fulfill this will result in your order not being delivered.**"
        embed = discord.Embed(
            title='Purchase here.',
            description='```https://www.roblox.com/game-pass/244524779```',
            color=discord.Color.default()
        )
        embed.set_image(url="https://i.pinimg.com/564x/9d/80/17/9d80174c33c54989872fc3f12ee12bf6.jpg")
        await message.channel.send(normal_message)
        await message.channel.send(embed=embed)

    # Paypal command

    elif message.content.startswith('+buypaypal'):
        normal_message = "**Make sure to record your purchase and send it here once completed, use F&F. Failing to fulfill this will result in your order not being delivered.**"
        embed = discord.Embed(
            title='Purchase here.',
            description='```paypal.me/byfron```',
            color=discord.Color.default()
        )
        embed.set_image(url="https://i.pinimg.com/736x/a4/90/cc/a490ccb0cb51e20e0bbf1c1ec8a4b12a.jpg")
        await message.channel.send(normal_message)
        await message.channel.send(embed=embed)

    # Help command

    elif message.content.startswith('+help'):
        embed = discord.Embed(
            title='**Links below.**',
            description='''\
                **Commands:** ```https://commandlinkhere```
                **Invite link:** ```https://discord.gg/supraK```
                **Rules:** ```https://discord.com/channels/1138299323994611742/1138357029984022580```

            ''',
            color=discord.Color.default()
        )
        embed.set_image(url="https://i.pinimg.com/originals/a7/64/52/a7645233ebafcb23c2f3de9b538788d5.gif")
        await message.channel.send(embed=embed)

    # Clothing command

    elif message.content.startswith('+clothing'):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d")
        embed = discord.Embed(
            title=f'**All shirts below are onsale as of {current_time}**',
            description='''\
                ```ShirtID here```
                ```ShirtID here```
            ''',
        )
        embed.set_image(url="")
        await message.channel.send(embed=embed)

# Run Bot

bot.run('MTE1NDkwNTQ5NjY3NTk2MzEyMw.GnRSEa.Gialz1bdJhlFLHqK1jwb9klJlf6h3ECWzWvL04')
