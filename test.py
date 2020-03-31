import discord

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

client.run("Njk0Mzg2ODQ0Njg2NjE0NTY5.XoLG0g.otBQ3LkZQJro5ERg8gQ9DqikSi4")