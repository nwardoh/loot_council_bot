# bot.py
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!'.format(client))

client.run(TOKEN)

#bot = commands.Bot(command_prefix="+")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '+ping':
        await message.channel.send('pong')
    await bot.process_commands(message)



