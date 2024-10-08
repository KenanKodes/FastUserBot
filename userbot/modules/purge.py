

from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, SUDO_ID
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("purge")

# ████████████████████████████████ #

@register(incoming=True, from_users=SUDO_ID, pattern="^.spurge$")
@register(outgoing=True, pattern="^.purge$")
async def fastpurger(purg):
    """ .purge  """
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0

    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count = count + 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        await purg.edit(LANG['NEED_MSG'])
        return

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id, LANG['PURGED'].format(str(count)))

    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID,
            "Hədəflənən " + str(count) + " mesaj uğurla silindi.")
    await sleep(2)
    await done.delete()


@register(outgoing=True, pattern="^.purgeme")
@register(incoming=True, from_users=SUDO_ID, pattern="^.spurgeme$")
async def purgeme(delme):
    """ .purgeme """
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id,
                                                    from_user='me'):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        LANG['PURGED_ME'].format(str(count))
    )
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID,
            "Hədəflənən " + str(count) + " mesaj uğurla silindi.")
    await sleep(2)
    i = 1
    await smsg.delete()


@register(outgoing=True, pattern="^.del$")
@register(incoming=True, from_users=SUDO_ID, pattern="^.sdel$")
async def delete_it(delme):
    """ .del  """
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Hədəflənən mesajın silinməsi uğurla başa çatdı")
        except rpcbaseerrors.BadRequestError:
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Bu mesajı silə bilmirəm.")


@register(outgoing=True, pattern="^.edit")
async def editer(edit):
    """ .editme """
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id('me')
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if BOTLOG:
        await edit.client.send_message(BOTLOG_CHATID,
                                       "Mesaj düzəltmə sorğusu uğurla edildi")


@register(outgoing=True, pattern="^.sd")
async def selfdestruct(destroy):
    """ .sd  """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID,
                                          "sd sorğusu uğurla başa çatdı")

CmdHelp('purge').add_command(
    'purge', None, (LANG['PUR1'])
).add_command(
    'purgeme', (LANG['PURG1']), (LANG['PURG2'])
).add_command(
    'del', (LANG['DEL1']), (LANG['DEL2'])
).add_command(
    'edit', (LANG['ED1']), (LANG['ED2'])
).add_command(
    'sd', (LANG['SD1']), (LANG['SD2'])
).add()
