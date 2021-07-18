import discord
from discord.ext import commands

# Variables - customize your bot here
prefix = '+'
filtered_words = {'YourWords', 'GoHere'}

# Non customizable variables
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():                                   # Shows if your bot is ready
    print('{0.user} is ready! ✔️'.format(bot))


@bot.event
async def on_member_join(member):
    welcome_message = f'{member} joined the server!'    # Change your welcome message here
    channel = bot.get_channel(847949897445408821)
    await channel.send(welcome_message)


@bot.event
async def on_message(message, limit=1):
    if message.author.id == bot.user.id:
        return

    for word in filtered_words:
        if word in message.content:
            await message.delete()
    await bot.process_commands(message)


bot.run('Your token goes here')
