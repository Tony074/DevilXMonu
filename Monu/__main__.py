import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from Monu import config
from Monu.config import BANNED_USERS
from Monu import LOGGER, app, userbot
from Monu.core.call import Monu
from plugins import ALL_MODULES
from Monu.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Monu").error(
            "No Assistant Clients Vars Defined!.. Exiting Process.."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Monu").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("plugins" + all_module)
    LOGGER("plugins").info(
        "Successfully Imported Modules."
    )
    await userbot.start()
    await Monu.start()
    try:
        await Monu.stream_decall("https://telegra.ph/file/4878eba458919fab40829.jpg")
    except:
        pass
    try:
        await Monu.stream_call(
            "https://telegra.ph/file/4878eba458919fab40829.jpg"
        )
    except NoActiveGroupCall:
        LOGGER("Monu").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Monu.decorators()
    LOGGER("Monu").info("Monu Player Started")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Monu").info("Stopping Music Bot...")
