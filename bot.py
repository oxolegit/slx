import discord
from discord.ext import commands

TOKEN = 'paste your token here'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready', client.user)

client.run(TOKEN)
