""" 
Credit :- Unknown 
Just Kidding Credit To X-Tra Telegram For Base 
And A Noob @CyberProgram For This Fucking Waste Plugin
"""
from userbot import bot
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import command, remove_plugin, load_module, admin_cmd
from var import Var
from pathlib import Path
from userbot import LOAD_PLUG
import sys
import asyncio
import traceback
import os

@borg.on(admin_cmd("ipa (.*)"))
async def install(event):
    if event.fwd_from:
        return
    chat = event.pattern_match.group(1)
    await event.edit(f"Starting To Install Plugins From {chat} ! Check PRIVATE GROUP for More Info !")
    documentss = await borg.get_messages(chat, None , filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(await borg.get_messages(chat, ids=mxo), "userbot/plugins/")
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            sed = f"Installing Plugins From {chat}"
            logger.info(sed)
            await borg.send_message(event.chat_id, "Installed Plugin `{}` successfully.".format(os.path.basename(downloaded_file_name)))
        else:
            await borg.send_message(event.chat_id, "Plugin `{}` has been pre-installed and cannot be installed.".format(os.path.basename(downloaded_file_name)))
