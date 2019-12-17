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

    if message.content.startswith('message_check '):
        msg = message.content.split(maxsplit=1)[1]
        print(msg)
        await message.channel.send(msg)

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
            await message.channel.send(error_message)
        else:
            try:
                await message.channel.send(result)
            except discord.errors.HTTPException:
                print('// null')
            else:
                print('// ' + result)


client.run(config['token'])
