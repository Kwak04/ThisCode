import discord
import json

with open("config.json") as config_file:
    config = json.load(config_file)

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    game = discord.Game("YEAH")
    await client.change_presence(activity=game)


client.run(config["token"])
