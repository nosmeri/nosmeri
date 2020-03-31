import discord
import os

client = discord.Client()
YYJ13cnftjr = 0
yellow0519cnftjr = 0
nosmericnftjr = 0

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("양씨는바보라고")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event

#if message.author.bot:
#   return None

async def on_message(message):
    if message.content.startswith("%머주명%"):
        await message.channel.send("/give boiled_pumpkin minecraft:player_head{SkullOwner:""닉네임""}")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
