from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config

def start_panel(_, BOT_USERNAME, OWNER: bool = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs",
                callback_data="settings_helper"
            ),
        ],
    ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: bool = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴏᴜʀ ᴡᴏʀᴅ 💌",
                url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ 💕",
                callback_data="owner_callback"
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ 🛠",
                callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ ❣",
                url="https://t.me/rockhushh"
            ),
            InlineKeyboardButton(
                text="ꜱᴏᴜʀᴄᴇ 🔗",
                url="https://github.com/Rockhush237"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴀʙᴏᴜᴛ ʀᴏᴄᴋʜᴜꜱʜ 💕",
                url="https://t.me/about_Rockhush"
            ),
        ],
    ]
    return buttons
