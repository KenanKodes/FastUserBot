import asyncio
from telethon import events
from userbot import BRAIN_CHECKER, WHITELIST
from userbot.events import register

@register(incoming=True, from_users=BRAIN_CHECKER, pattern="^.falive$")
@register(incoming=True, from_users=WHITELIST, pattern="^.falive$")
async def _(q):
    await q.client.send_message(q.chat_id,"`⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝💻 Oɴʟɪɴᴇ...`")
