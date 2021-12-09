import os
import time
from dotenv import load_dotenv

# Set timezone
os.environ['TZ'] = 'Europe/Madrid'
time.tzset()

load_dotenv()
status_api = os.getenv('STATUS_API')
discord_token = os.getenv('DISCORD_TOKEN')
discord_play_game = os.getenv('DISCORD_PLAY_GAME')
minecraft_status_channel = int(os.getenv('MINECRAFT_STATUS_CHANNEL'))
minecraft_players_channel = int(os.getenv('MINECRAFT_PLAYERS_CHANNEL'))
