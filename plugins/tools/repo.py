# Power By @Monu_Gupta_01
# Join @About_Info_Devil For More Update
# Join @About_Info_Devil For Information 
# Join Our Chats @About_In_Bot 

from pyrogram import Client, filters

from Monu import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/f73af9a4ffe130a83dd2.jpg",
        caption=f"""🥀 𝐍𝐨𝐰 𝐌𝐲 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐈𝐬 𝐏𝐮𝐛𝐥𝐢𝐜 🌺, 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐑𝐞𝐩𝐨 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐌𝐲 𝐂𝐨𝐝𝐞 ♕, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤, 𝐓𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 𝐁𝐮𝐭𝐭𝐨𝐧 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 𝐒𝐮𝐛𝐜𝐫𝐢𝐛𝐞 𝐎𝐮𝐫 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥  :
  [𝐘𝐨𝐮𝐭𝐮𝐛𝐞](https://www.youtube.com/@iamprabhakar09)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐑𝐞𝐩𝐨 🥀", url=f"https://github.com/Tony074/DevilXMonu")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 🥀", url=f"https://t.me/Monu_Gupta_01")
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

# Power By @Monu_Gupta_01
# Join @About_Info_Devil For More Update
# Join @About_Info_Devil For Information 
# Join Our Chats @About_In_Bot  
