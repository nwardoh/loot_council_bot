# bot.py
import os
import discord
#from discord.ext.commands import Bot

bot = Bot(command_prefix="+")

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
client.run(TOKEN)

#@bot.event
#async def on_message(message):
#	if message.content == 'test':
#		await message.channel.send('Testing 1 2 3!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(TOKEN)

