import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

TOKEN = 'MON_TOKEN'
PREFIX = '+'  

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Salut, je suis :  {bot.user.name}')

@bot.command()
async def clear(ctx, nombre: int):
    if nombre > 0:
        await ctx.channel.purge(limit=nombre + 1)
        print(f'{nombre} messages ont été supprimés dans le salon : {ctx.channel.name}')
    else:
        await ctx.send("Le nombre doit être supérieur à zéro.")

bot.run(TOKEN)
