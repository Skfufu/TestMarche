import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # selon ce que tu veux faire

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

bot.run("TokenDiscord")
