import asyncio
import imp
import inspect
import os
from fnmatch import fnmatch

from discord import Member, Message, Channel, Client

from Events.InterfaceEvent import *

BOT_NAME = "UnlockedBot"
client = Client()
loop = asyncio.get_event_loop()
watch_channels = []
event_effectors = []
shutdown_flag = False
bot_on = False


@client.event
async def on_ready():
    global bot_on
    print("Bot: On")
    bot_on = True


async def send_message(channel: Channel, msg: str, mention: Member = None, nick: str = None):
    me = channel.server.get_member(client.user.id)
    old_nick = me.nick
    if nick is not None:
        await client.change_nickname(me, nick)
    if mention is None:
        await client.send_message(channel, msg)
    else:
        await client.send_message(channel, mention.mention + ' ' + msg)
    if nick is not None:
        await client.change_nickname(me, old_nick)


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


@client.event
async def on_message(message: Message):
    for message_event in event_effectors:
        if isinstance(message_event, InterfaceMessageEvent):
            try:
                await message_event.on_message(message)
            except:
                pass
                # traceback.print_exc()


@client.event
async def on_voice_state_update(before: Member, after: Member):
    for voice_event in event_effectors:
        if isinstance(voice_event, InterfaceVoiceEvent):
            try:
                await voice_event.on_voice_state_update(before, after)
            except:
                pass
                # traceback.print_exc()


async def client_tick_start():
    while not shutdown_flag:
        await asyncio.sleep(0)
        if bot_on:
            await client_tick()


async def client_tick():
    for tick_listeners in event_effectors:
        if isinstance(tick_listeners, InterfaceClientTick):
            try:
                await tick_listeners.on_client_tick()
            except:
                pass
                # traceback.print_exc()

async_tasks = []
async def other_tasks():
    while not shutdown_flag:
        await asyncio.sleep(0)
        for task in async_tasks:
            await task["func"](task["args"])
            async_tasks.remove(task)


dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\Events"
pattern = "*.py"

for path, subdirs, files in os.walk(dir_path):
    for name in files:
        if fnmatch(name, pattern):
            found_module = imp.find_module(name[:-3], [path])
            module = imp.load_module(name, found_module[0], found_module[1], found_module[2])
            for mem_name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and inspect.getmodule(obj) is module and issubclass(obj, InterfaceEvent):
                    try:
                        event_effectors.append(obj(client))
                    except:
                        pass

loop.run_until_complete(asyncio.gather(*[asyncio.ensure_future(run_bot()),
                                         asyncio.ensure_future(client_tick_start()),
                                         asyncio.ensure_future(other_tasks())]))
