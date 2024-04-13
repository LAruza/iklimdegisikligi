import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We woke up {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Selam'):
        await message.channel.send("Merhabalar! Ben iklim! iklim değişikliği hakkında bilgi veren bir robotum nasıl yardımcı olabilirim? ($help yazarak komutlara bakabilirsiniz :D)")
    elif message.content.startswith('$help'):
        await message.channel.send("$iklimfoto = iklim değişikliği ile ilgili fotoğraf $yapımcı = yapan kişi hakkında bilgi verir $iklimbilgi")
    elif message.content.startswith('$yapımcı'):
        await message.channel.send("Yapan kişi mamayda")
    elif message.content.startswith('$foto'):
        
        dizi = os.listdir("iklimfoto")
        dosyaadi =random.choice(dizi)
        print(dosyaadi,"****")
        with open(f'iklimfoto/{dosyaadi}', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

client.run("insert token here")
