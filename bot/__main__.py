# < (c) 2021 @kaif-00z >

from glob import glob
from importlib import import_module

from . import *

LOGS.info("Starting...")

try:
    user.start()
except Exception as erc:
    LOGS.info(erc)


plugins = glob("bot/plugins/*py")
for plugin in plugins:
    try:
        plugin = plugin.replace(".py", "").replace("/", ".")
        import_module(plugin)
    except Exception as er:
        print(er)

LOGS.info("Bot has started...")
user.run_until_disconnected()
