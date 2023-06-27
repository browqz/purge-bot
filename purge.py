import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

TOKEN = 'TON_TOKEN'
PREFIX = '+'  

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Salut je suis :  {bot.user.name}')

@bot.command()
async def nigga(ctx, nombre: int):

    await ctx.channel.purge(limit=nombre + 1)
    print(f'{nombre}  messages ont bien été supprimes dans le salon : {ctx.channel.name}')

bot.run(TOKEN)
