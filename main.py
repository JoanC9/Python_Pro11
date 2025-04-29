import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')
    
@bot.command()
async def saludar(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        
        await ctx.send('Hola, ¿cómo estás?')
        
    elif mensaje == 'que onda':
        
        await ctx.send('Todo bien')
    
    elif mensaje == 'klk':
        
        await ctx.send('Todo bien')
        
token = ''

bot.run(token)
        
