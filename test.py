import discord

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("ready")
    print("-----------------")
    game = discord.Game("-도움말")
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.event
async def on_message(message):
    if message.content.startswith("-도움말"):
        await message.channel.send("마떡 멍청이")
    if message.content.startswith("-마떡"):
        await message.channel.send("https://www.youtube.com/channel/UCv7LywcV784vgK-Pz2s5fZg")
    if "ㅅㅂ" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
    if "ㅄ" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
    if "ㅂㅅ" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
    if "ㅆㅂ" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
    if "ㅈㄹ" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
    if "시발" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
    if "병신" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
    if "븅신" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
    if "씨발" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
    if "지랄" in message.content:
        await message.delete()
        await message.channel.send("욕하지 마세요")
        
client.run('ODIwMTczNTY3NDUwMTUyOTkw.YExUKA.03f2Qt5ZGR5yW8TvMAY3YROtQ5o')
