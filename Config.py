import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","unbornedvillian")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","zeus_MUSIC_ROBOT")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME")
# ---------------------------------------------------------
