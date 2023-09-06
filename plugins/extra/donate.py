from pyrogram import Client, filters

from Bikash import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("donate")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def donate(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4878eba458919fab40829.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 & 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐃𝐞𝐯𝐢𝐥 𝐇𝐞𝐚𝐯𝐞𝐧 𝐨𝐫 𝐃𝐞𝐯𝐚 𝐅𝐨𝐫 𝐐𝐫 𝐂𝐨𝐝𝐞, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤 𝐓𝐡𝐞𝐧 [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/Monu_Gupta_01) & 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 [𝐘𝐨𝐮𝐭𝐮𝐛𝐞](https://youtube.com/@motivationalforall9823?si=YZNPKGhePON-2j9k)..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐃𝐞𝐯𝐢𝐥 𝐇𝐞𝐚𝐯𝐞𝐧 🥀", url=f"https://t.me/Monu_Gupta_01")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝐃𝐞𝐯𝐚 🥀", url=f"https://t.me/deva_mandal")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/About_Info_Devil"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/About_Info_Devil")
                ]
            ]
        ),
    )
