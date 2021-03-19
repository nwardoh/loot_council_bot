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

bot = commands.Bot(command_prefix="+")

@bot.command()
async def ping(ctx):
   await ctx.channel.send('pong')

