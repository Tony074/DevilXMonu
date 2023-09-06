from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from Monu.config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from Monu.Mkg import get_command
from Monu import app
from Monu.core.call import Monu
from Monu.utils import bot_sys_stats
from Monu.utils.decorators.language import language
from Monu.utils.inline.play import close_keyboard

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Monu.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ),
        reply_markup=close_keyboard
    )
