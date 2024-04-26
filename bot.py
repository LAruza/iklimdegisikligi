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
    if message.content.startswith('Codename'):
        await message.channel.send("Response")
    elif message.content.startswith('Codename'):
        await message.channel.send("response")
    elif message.content.startswith('codename'):
        await message.channel.send("respone")
    elif message.content.startswith('mew'):
        await message.channel.send("https://tenor.com/view/cat-silly-silly-cat-silly-cats-mewing-gif-14812443053695024113")
    #must add this btw
    elif message.content.startswith('codetosendphoto'):
        dizi = os.listdir("foldername")
        filemaöe =random.choice(dizi)
        print(filename,"****")
        with open(f'foldername/{filename}', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

client.run("insert token here")
