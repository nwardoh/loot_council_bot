# bot.py
import os
import discord
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="+")

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

@bot.event
async def on_message(message):
	if message.content == 'test':
		await message.channel.send('Testing 1 2 3!')

bot.run(TOKEN)

