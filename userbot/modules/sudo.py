from telethon import events

import asyncio
from userbot import SUDO_ID
from userbot.cmdhelp import CmdHelp
from userbot.events import register

@register(incoming=True, from_users=SUDO_ID, pattern="^.falives$")
async def _(q):
    await q.client.send_message(q.chat_id,"`[⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)ＳＵＤＯ ✨`")

CmdHelp('sudo').add_command(
    'falives', None, 'SUDOnun aktiv olub olmadığını yoxlayar.'
).add()
