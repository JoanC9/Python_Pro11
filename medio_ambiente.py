import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')


lista_contaminacion_colombia = [
    'La contaminacion en Colombia es un problema grave que afecta la salud de la población y el medio ambiente.',
    'La contaminación del aire en Bogotá es uno de los problemas más graves que enfrenta la ciudad.',
    'La contaminación del agua en Colombia es un problema que afecta a muchas comunidades rurales.',
    'La deforestación en la Amazonía colombiana es una de las principales causas de la contaminación del aire.',
    'La contaminación del suelo en Colombia es un problema que afecta la agricultura y la salud de las personas.',
    'La contaminación acústica en las ciudades colombianas es un problema que afecta la calidad de vida de los habitantes.',
    'La contaminación por plásticos en los océanos es un problema global que también afecta a Colombia.',
    'La contaminación por metales pesados en el agua es un problema que afecta la salud de las personas y los ecosistemas.',
]

lista_contaminacion_peru = [
    'La ciudad de Lima enfrenta altos niveles de contaminación del aire, especialmente durante la temporada de invierno.',
    'La contaminación del agua en Perú es un problema grave, especialmente en las zonas rurales donde el acceso a agua potable es limitado.',
    'La minería ilegal en Perú ha causado graves problemas de contaminación del suelo y del agua en varias regiones del país.',
    'La contaminación acústica en las ciudades peruanas es un problema que afecta la calidad de vida de los habitantes.',
]

lista_contaminacion_uruguay =[
    
    'La ciudad mas contaminada de Uruguay es Montevideo, donde la contaminación del aire es un problema importante.',
    'El año 2020, Uruguay implementó una ley para reducir la contaminación del aire y mejorar la calidad de vida de sus habitantes.',
    'Uruguay es conocido por su compromiso con la sostenibilidad y la protección del medio ambiente.',
    'La peor catastrofe ambiental en la historia de Uruguay fue el derrame de petróleo en la costa de Montevideo en 1972.',
]

lista_mejorar_medio_ambiente = [
    'Para ayudar a mejorar el medio ambiente en Colombia, puedes reducir el uso de plásticos y optar por productos reutilizables.',
    'Puedes participar en campañas de reforestación y limpieza de ríos y playas para ayudar a mejorar el medio ambiente en Colombia.',
    'Como adolescente, puedes involucrarte en grupos de jóvenes que promueven la conservación del medio ambiente y la sostenibilidad.',
    'Puedes aprender sobre energías renovables y promover su uso en tu comunidad para ayudar a mejorar el medio ambiente en Colombia.',
    'Puedes educar a tus amigos y familiares sobre la importancia de cuidar el medio ambiente y cómo pueden contribuir.',
    'Puedes participar en actividades de reciclaje y compostaje en tu hogar y comunidad para ayudar a reducir la contaminación.',
]
    
@bot.command()
async def contaminacion(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'colombia':
        
        mensaje = random.choice(lista_contaminacion_colombia)
        await ctx.send(mensaje)
        
    elif mensaje == 'peru':
        
        mensaje = random.choice(lista_contaminacion_peru)
        await ctx.send(mensaje)
        
    elif mensaje == 'uruguay':
        
        mensaje = random.choice(lista_contaminacion_uruguay)
        await ctx.send(mensaje)
        
    else:
        await ctx.send('No tengo información sobre la contaminación en ese país. Por favor, elige entre Colombia, Perú o Uruguay.')
    

@bot.command()
async def ayudar(ctx):
    
    mensaje = random.choice(lista_mejorar_medio_ambiente)
    await ctx.send(mensaje)
    
@bot.command()
async def imagen (ctx):
    
    nombre_imagen = random.choice(os.listdir('contaminacion'))
    
    with open(f'contaminacion/{nombre_imagen}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

token = ''
bot.run(token)