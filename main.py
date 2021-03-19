# bot.py
import os
import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix="+")

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def test(ctx):
    await ctx.send('testing')

bot.run(TOKEN)

