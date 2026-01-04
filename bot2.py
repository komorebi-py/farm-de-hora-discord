import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("bot on fr")

bot.run(os.getenv("TOKEN"))
