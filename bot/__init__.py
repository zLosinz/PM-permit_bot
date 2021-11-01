# < (c) 2021 @kaif-00z >

import sys
from logging import DEBUG, INFO, basicConfig, getLogger, warning

from redis import Redis
from telethon import TelegramClient
from telethon.sessions import StringSession

from .config import Var

try:
    redis_info = Var.REDIS_URI.split(":")
    dB = Redis(
        host=redis_info[0],
        port=redis_info[1],
        password=Var.REDIS_PASS,
        charset="utf-8",
        decode_responses=True,
    )
except Exception:
    sys.exit(Exception)

basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger(__name__)


try:
    user = TelegramClient(StringSession(Var.SESSION), Var.API_ID, Var.API_HASH)
except Exception as e:
    LOGS.info("Environment vars are missing! Kindly recheck.")
    LOGS.info("Bot is quiting...")
    LOGS.info(str(e))
    exit()
