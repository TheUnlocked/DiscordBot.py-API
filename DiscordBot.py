"""
THIS IS AN ESSENTIAL FILE. DO NOT MODIFY OR REMOVE IT UNLESS SPECIFIED BY OTHER DOCUMENTATION.
"""

import asyncio
import imp
import inspect
import os
from fnmatch import fnmatch
import datetime

from discord.calls import *
from discord.client import *
from discord.channel import *
from discord.colour import *
from discord.compat import *
from discord.emoji import *
from discord.enums import *
from discord.errors import *
from discord.game import *
from discord.gateway import *
from discord.http import *
from discord.invite import *
from discord.iterators import *
from discord.member import *
from discord.message import *
from discord.mixins import *
from discord.object import *
from discord.opus import *
from discord.permissions import *
from discord.role import *
from discord.server import *
from discord.state import *
from discord.user import *
from discord.utils import *
from discord.voice_client import *

from InterfaceEvent import *

"""
Change this to the name of your bot.
"""
BOT_NAME = "UnlockedBot"

"""
This is the info used in the info command. Modify it for your bot.
"""
INFO = "`UnlockedBot beta m1` by Unlocked\n" \
       "All modules written by Unlocked"

client = Client()
loop = asyncio.get_event_loop()
watch_channels = []
module_events = []
shutdown_flag = False
bot_on = False


# //<editor-fold desc="discord.py Events">


@client.event
async def on_ready():
    global bot_on
    bot_on = True

    for event in module_events:
        if isinstance(event, InterfaceOnReady):
            try:
                await event.on_ready()
            except:
                pass


@client.event
async def on_resumed():
    for event in module_events:
        if isinstance(event, InterfaceOnResumed):
            try:
                await event.on_resumed()
            except:
                pass


@client.event
async def on_error(event, *args, **kwargs):
    for event_ in module_events:
        if isinstance(event_, InterfaceOnError):
            try:
                await event.on_error(event_, *args, **kwargs)
            except:
                pass


@client.event
async def on_message(message: Message):
    for event in module_events:
        if isinstance(event, InterfaceOnMessage):
            try:
                await event.on_message(message)
            except:
                pass


@client.event
async def on_socket_raw_receive(msg):
    for event in module_events:
        if isinstance(event, InterfaceOnSocketRawReceive):
            try:
                await event.on_socket_raw_receive(msg)
            except:
                pass


@client.event
async def on_socket_raw_send(payload):
    for event in module_events:
        if isinstance(event, InterfaceOnSocketRawSend):
            try:
                await event.on_socket_raw_send(payload)
            except:
                pass


@client.event
async def on_message_delete(message: Message):
    for event in module_events:
        if isinstance(event, InterfaceOnMessageDelete):
            try:
                await event.on_message_delete(message)
            except:
                pass


@client.event
async def on_message_edit(before: Message, after: Message):
    for event in module_events:
        if isinstance(event, InterfaceOnMessageEdit):
            try:
                await event.on_message_edit(before, after)
            except:
                pass


@client.event
async def on_channel_delete(channel: Channel):
    for event in module_events:
        if isinstance(event, InterfaceOnChannelDelete):
            try:
                await event.on_channel_delete(channel)
            except:
                pass


@client.event
async def on_channel_create(channel: Channel):
    for event in module_events:
        if isinstance(event, InterfaceOnChannelCreate):
            try:
                await event.on_channel_create(channel)
            except:
                pass


@client.event
async def on_channel_update(before: Channel, after: Channel):
    for event in module_events:
        if isinstance(event, InterfaceOnChannelUpdate):
            try:
                await event.on_channel_update(before, after)
            except:
                pass


@client.event
async def on_member_join(member: Member):
    for event in module_events:
        if isinstance(event, InterfaceOnMemberJoin):
            try:
                await event.on_member_join(member)
            except:
                pass


@client.event
async def on_member_remove(member: Member):
    for event in module_events:
        if isinstance(event, InterfaceOnMemberRemove):
            try:
                await event.on_member_remove(member)
            except:
                pass


@client.event
async def on_member_update(before: Member, after: Member):
    for event in module_events:
        if isinstance(event, InterfaceOnMemberUpdate):
            try:
                await event.on_member_update(before, after)
            except:
                pass


@client.event
async def on_server_join(server: Server):
    for event in module_events:
        if isinstance(event, InterfaceOnServerJoin):
            try:
                await event.on_server_join(server)
            except:
                pass


@client.event
async def on_server_remove(server: Server):
    for event in module_events:
        if isinstance(event, InterfaceOnServerRemove):
            try:
                await event.on_server_remove(server)
            except:
                pass


@client.event
async def on_server_update(before: Server, after: Server):
    for event in module_events:
        if isinstance(event, InterfaceOnServerUpdate):
            try:
                await event.on_server_update(before, after)
            except:
                pass


@client.event
async def on_server_role_create(role: Role):
    for event in module_events:
        if isinstance(event, InterfaceOnServerRoleCreate):
            try:
                await event.on_server_role_create(role)
            except:
                pass


@client.event
async def on_server_role_delete(role: Role):
    for event in module_events:
        if isinstance(event, InterfaceOnServerRoleDelete):
            try:
                await event.on_server_role_delete(role)
            except:
                pass


@client.event
async def on_server_role_update(before: Role, after: Role):
    for event in module_events:
        if isinstance(event, InterfaceOnServerRoleUpdate):
            try:
                await event.on_server_role_update(before, after)
            except:
                pass


@client.event
async def on_server_emojis_update(before: [], after: []):
    for event in module_events:
        if isinstance(event, InterfaceOnServerEmojisUpdate):
            try:
                await event.on_server_emojis_update(before, after)
            except:
                pass


@client.event
async def on_server_available(server: Server):
    for event in module_events:
        if isinstance(event, InterfaceOnServerAvailable):
            try:
                await event.on_server_available(server)
            except:
                pass


@client.event
async def on_server_unavailable(server: Server):
    for event in module_events:
        if isinstance(event, InterfaceOnServerUnavailable):
            try:
                await event.on_server_unavailable(server)
            except:
                pass


@client.event
async def on_voice_state_update(before: Member, after: Member):
    for event in module_events:
        if isinstance(event, OnVoiceStateUpdate):
            try:
                await event.on_voice_state_update(before, after)
            except:
                pass


@client.event
async def on_member_ban(member: Member):
    for event in module_events:
        if isinstance(event, InterfaceOnMemberBan):
            try:
                await event.on_member_ban(member)
            except:
                pass


@client.event
async def on_member_unban(server: Server, user: User):
    for event in module_events:
        if isinstance(event, InterfaceOnMemberUnban):
            try:
                await event.on_member_unban(server, user)
            except:
                pass


@client.event
async def on_typing(channel: Channel, user: User, when: datetime.datetime):
    for event in module_events:
        if isinstance(event, InterfaceOnTyping):
            try:
                await event.on_typing(channel, user, when)
            except:
                pass


@client.event
async def on_group_join(channel: Channel, user: User):
    for event in module_events:
        if isinstance(event, InterfaceOnGroupJoin):
            try:
                await event.on_group_join(channel, user)
            except:
                pass


@client.event
async def on_group_remove(channel: Channel, user: User):
    for event in module_events:
        if isinstance(event, InterfaceOnGroupRemove):
            try:
                await event.on_group_remove(channel, user)
            except:
                pass


async def on_client_tick():
    for event in module_events:
        if isinstance(event, InterfaceOnClientTick):
            try:
                await event.on_client_tick()
            except:
                pass

# //</editor-fold>


async def send_message(channel: Channel, msg: str, mention: Member = None):
    if mention is None:
        await client.send_message(channel, u'\u200B' + msg)
    else:
        await client.send_message(channel, u'\u200B' + mention.mention + ' ' + msg)


async def run_bot():
    global client
    filename = os.getenv('LOCALAPPDATA') + "\\" + BOT_NAME + "\\token.txt"
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        open(filename, 'w').close()
    file = open(filename, 'r+')
    token = file.read()
    if token == '':
        token = input("Please enter the bot token: ")
        file.write(token)
    try:
        file.close()
        await client.login(token)
        await client.connect()
    except:
        token = input("Authorization failed. Please enter the bot token: ")
        file = open(filename, 'r+')
        file.write(token)
        file.close()
        await client.login(token)
        await client.connect()


async def stop_bot():
    await client.logout()


async def client_tick_start():
    while not shutdown_flag:
        await asyncio.sleep(0)
        if bot_on:
            await on_client_tick()


async_tasks = []


def add_async_task(func, args):
    async_tasks.append((func, args))


async def other_tasks():
    while not shutdown_flag:
        await asyncio.sleep(0)
        for task in async_tasks:
            try:
                await task[0](task[1])
            except:
                pass
            async_tasks.remove(task)


dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\Modules"
pattern = "*.py"

for path, subdirs, files in os.walk(dir_path):
    for name in files:
        if fnmatch(name, pattern):
            found_module = imp.find_module(name[:-3], [path])
            module = imp.load_module(name, found_module[0], found_module[1], found_module[2])
            for mem_name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and inspect.getmodule(obj) is module and issubclass(obj, InterfaceEvent):
                    try:
                        module_events.append(obj())
                    except:
                        pass

loop.run_until_complete(asyncio.gather(*[asyncio.ensure_future(run_bot()),
                                         asyncio.ensure_future(client_tick_start()),
                                         asyncio.ensure_future(other_tasks())]))
