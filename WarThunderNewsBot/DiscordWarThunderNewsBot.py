import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    client.move_member(client,"bots")
    print("on_ready() is working.. sorta")
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command()
async def shutdown():
    await client.say("Disconnecting...")
    await client.close()

@client.command()
async def test():
    await client.say("Connected!")

@client.command()
async def getNews():
    await client.say("Command currently under construction...\nhttps://WarThunder.com/en/news")

@client.command()
async def postNews():
    await client.say("Obtaining latest news from War Thunder...")
    await client.say("!getNews")
    await client.delete_message(2)


client.run("MzUyOTI5NTg0MzY4NDUxNTg1.DJCCSg.E3JTWtKNCSsIZldR229KY5IIN2M")