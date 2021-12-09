import discord
from discord.ext import commands
import asyncio
import requests
from settings import status_api, discord_token, discord_play_game, minecraft_status_channel, minecraft_players_channel

client = commands.Bot(command_prefix='!', help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(discord_play_game))
    print('Bot is ready.')

async def background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            status = requests.get(status_api+'/status', timeout=5).json()['status']
            status_channel=client.get_channel(minecraft_status_channel)
            discord_channel_status = str(status_channel).split(': ')[1]
            if status != discord_channel_status:
                await status_channel.edit(name=f"Estado: {status}")
                status_channel=client.get_channel(minecraft_status_channel)
                discord_channel_status = str(status_channel).split(': ')[1]
                print(f"Cambiando estado de Discord a {status}")
            if status == "Online":
                players = requests.get(status_api+'/players').json()
                players_channel=client.get_channel(minecraft_players_channel)
                actual_players=(f"{players['players_online']}/{players['players_max']}")
                discord_channel_players = str(players_channel).split(': ')[1]
                if actual_players != discord_channel_players:
                    await players_channel.edit(name=f"Jugadores: {players['players_online']}/{players['players_max']}")
                    print(f"Cambiando número de jugadores en Discord a: {players['players_online']}/{players['players_max']}")
            if status == "Offline" and discord_channel_status == "Offline":
                players_channel=client.get_channel(minecraft_players_channel)
                discord_channel_players = str(players_channel).split(': ')[1]
                if discord_channel_players != "0/0":
                    await players_channel.edit(name=f"Jugadores: 0/0")
                    print(f"Reseteando número de jugadores en Discord a 0.")
        except:
            print ('Ha sucedido un error.')
        await asyncio.sleep(60)

client.loop.create_task(background_task())
client.run(discord_token)
