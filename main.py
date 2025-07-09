# Cookies on the clouds ☁️💤
# ==========================
# main.py

import discord
import datetime
from discord.ext import commands
from utils.handler import register_event
from utils.config import createconfig
from utils.logger import createlog
from utils.blacklist import createblacklist

start_time = datetime.datetime.utcnow()

usage_log_path, error_log_path = createlog()

config = createconfig()
if config:
    token = config['TOKEN']
    prefix = config['PREFIX']
    client_id = config['CLIENT_ID']
    botname = config['BOT_NAME']

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix = prefix,
    intents = intents,
    help_command=None
)

bot.botname = botname
bot.start_time = start_time
bot.prefix = prefix
bot.client_id = client_id

createblacklist()

register_event(bot, botname, prefix)

bot.run(token)