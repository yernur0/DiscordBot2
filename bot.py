from settings import settings
from bot_logic import *
import discord


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send("https://tenor.com/view/hello-gif-26229478")
    elif message.content.startswith('!bye'):
        await message.channel.send("https://tenor.com/view/discord-banner-gif-21647267")

    elif message.content.startswith('!gpassword'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('!coin'):
        await message.channel.send(coin())
    elif message.content.startswith('!help'):
        await message.channel.send(help())

client.run(settings["TOKEN"])