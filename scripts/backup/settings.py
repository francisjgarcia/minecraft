from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()
hostname = os.getenv("HOSTNAME")
server = os.getenv("SERVER")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

date = datetime.today().strftime('%Y-%m-%d')
