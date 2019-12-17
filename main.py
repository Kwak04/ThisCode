import discord
import json
from subprocess import check_output

with open("config.json") as config_file:
    config = json.load(config_file)

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    game = discord.Game("YEAH")
    await client.change_presence(activity=game)


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('message_check '):
        msg = message.content.split(maxsplit=1)[1]
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith('py '):
        code = message.content.split(maxsplit=1)[1]
        print(code)
        with open('code.py', 'w') as f:
            f.write(code)

        result = check_output('python3 code.py', shell=True, universal_newlines=True)
        print(result)
        await message.channel.send(result)


client.run(config["token"])
