import discord
import json
from subprocess import check_output
from subprocess import CalledProcessError

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

    if message.content.startswith('py '):
        print('---------------------------------------------')

        code = message.content.split(maxsplit=1)[1]
        print(code)
        with open('code.py', 'w') as f:
            f.write(code)

        try:
            result = check_output('python3 code.py', shell=True, universal_newlines=True)
        except CalledProcessError:
            error_message = "Oh, no! Your code was crashed!"
            embed = discord.Embed(title="Error occurred", description=error_message, color=0xff0000)
            await message.channel.send(embed=embed)
        else:
            if result != "":
                description = result
                print('// ' + result)
            else:
                description = "No result"
                print('// No result')

            embed = discord.Embed(title="Result", description=description, color=0xffff00)
            await message.channel.send(embed=embed)


client.run(config['token'])
