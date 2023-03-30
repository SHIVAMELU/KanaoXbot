import datetime
from datetime import datetime

import telegram
from pyrogram import __version__ as pyro
from telethon import Button, version

from SUMI import BOT_NAME, GROUP_ALIVE_PIC, OWNER_ID, OWNER_NAME
from SUMI import telethn as tbot
from SUMI.events import register

edit_time = 5

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    text2 = f"➢ **Mᴏsʜɪ Mᴏsʜɪ [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'ᴍ {BOT_NAME}**\n"
    text2 += f"➢ **My Uptime** - `{uptime}`\n"
    text2 += f"➢ **Telethon Version** - `{version.__version__}`\n"
    text2 += f"➢ **PTB Version** - `{telegram.__version__}`\n"
    text2 += f"➢ **Pyrogram Version** - `{pyro}`\n"
    text2 += f"➢ **MY MASTER** - [{OWNER_NAME}](tg://user?id={OWNER_ID})\n"
    text2 += f"➢ **MY DEVELOPER** - [𝓴𝓪𝓷𝓮𝓴𝓲](https://t.me/tobiix)"
    BUTTON = [
        [
            Button.url("Support Chat", "https://t.me/botsupportx"),
            Button.url("Updates", "https://t.me/hinatabotsupport"),
        ]
    ]
    on = await tbot.send_file(
        yes.chat_id, file=GROUP_ALIVE_PIC, caption=text2, buttons=BUTTON
    )
