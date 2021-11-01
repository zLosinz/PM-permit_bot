# < (c) 2021 @kaif-00z >

from telethon.tl.functions.contacts import BlockRequest
from telethon.utils import get_display_name

from . import *

mwarn = {}


@user.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def _(e):
    if is_approved(e.sender_id):
        return
    sender = await e.get_sender()
    name = get_display_name(sender)
    owner = await e.client.get_me()
    owner_name = get_display_name(owner)
    if mwarn.get(e.sender_id):
        count = mwarn[e.sender_id] + 1
        mwarn[e.sender_id] = count
    else:
        count = 1
        mwarn[e.sender_id] = count
    id = e.sender_id
    warn = mwarn.get(id)
    if warn == 3:
        x = await user.send_message(
            e.chat_id,
            f"Hello `{name}`\nI am PM SECURITY BOT of **{owner_name}**.\nPlz Don't Spam the PM.\nWait for reply or `You Will Ban and Report.`\n`Warning` {warn}/3",
            file=None,
        )
        await e.client(BlockRequest(id))
        await x.edit("`Sorry you are Banned and Reported for spaming.`")
    elif warn < 3:
        await user.send_message(
            e.chat_id,
            f"Hello `{name}`\nI am PM SECURITY BOT of **{owner_name}**.\nPlz Don't Spam the PM.\nWait for reply or `You Will Ban and Report.`\n`Warning` {warn}/3",
            file=None,
        )
    else:
        return


@user.on(events.NewMessage(outgoing=True, func=lambda e: e.is_private))
async def _(e):
    user = e.chat_id
    add_approve(user)


@user.on(
    events.NewMessage(
        outgoing=True,
        pattern="\\.disapprove",
        func=lambda e: e.is_private,
    ),
)
async def _(e):
    user = e.chat_id
    rem_approve(user)
    await e.edit("`Disapproved`")
