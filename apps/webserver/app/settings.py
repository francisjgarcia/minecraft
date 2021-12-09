import os
import time
from dotenv import load_dotenv
from datetime import datetime

# Set timezone
os.environ['TZ'] = 'Europe/Madrid'
time.tzset()

load_dotenv()
server_name = os.getenv('SERVER_NAME')
server_url = os.getenv('SERVER_URL')
server_port = os.getenv('SERVER_PORT')

date = datetime.today().strftime('%Y-%m-%d')
mods_folder = "/mnt/minecraft/mods"
