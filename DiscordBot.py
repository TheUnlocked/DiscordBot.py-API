"""
THIS IS AN ESSENTIAL FILE. DO NOT MODIFY OR REMOVE IT UNLESS SPECIFIED BY OTHER DOCUMENTATION.
"""

import asyncio
import imp
import inspect
import os
from fnmatch import fnmatch
from discord import Channel, Member
import fml.EventInstantiator
from fml.InterfaceEvent import *
import json
import sys

"""
Change this to the name of your bot.
"""
BOT_NAME = "UnlockedBot" if len(sys.argv) == 1 or not sys.argv[1].startswith("--name:") \
    else sys.argv[1].split("--name:")[1]


"""
This is the info used in the info command. Modify it for your bot.
"""
INFO = "`UnlockedBot m2 beta` by Unlocked\n" \
       "All modules written by Unlocked"

client = discord.Client()
loop = asyncio.get_event_loop()
watch_channels = []
shutdown_flag = False
bot_on = False
module_events = []
server_rules = {}


def get_modules():
    return module_events


def get_module_by_id(identifier):
    for m in get_modules():
        if m.module_id == identifier:
            return m
    return None


def get_client():
    return client


async def send_message(channel: Channel, msg: str, mention: Member = None):
    if mention is None:
        await client.send_message(channel, u'\u200B' + msg)
    else:
        await client.send_message(channel, u'\u200B' + mention.mention + ' ' + msg)


async def run_bot():
    filename = os.environ['APPDATA'] + "\\" + BOT_NAME + "\\token.txt"
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


async def on_client_tick():
    for event in get_modules():
        if isinstance(event, InterfaceOnClientTick):
            try:
                await event.on_client_tick()
            except:
                pass


async def client_tick_start():
    while not shutdown_flag:
        await asyncio.sleep(0)
        if bot_on:
            await on_client_tick()

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

print(module_events)
fml.EventInstantiator.instantiate_events(client)


def obtain_server_rules():
    server_rules_json = json.loads(
        open(os.path.dirname(os.path.realpath(__file__)) + "\\Modules\\server_rules.json", 'r+').read())
    # for key in list(server_rules_json.keys()):
    #     try:
    #         server_rules[int(key)] = server_rules_json[key]
    #         # newlist = []
    #         # for m in server_rules_json[key]["list"]:
    #         #     if get_module_by_id(m) is not None:
    #         #         newlist.append(get_module_by_id(m))
    #         # server_rules[int(key)]["list"] = newlist
    #     except:
    #         pass
    return server_rules_json

server_rules = obtain_server_rules()

loop.run_until_complete(asyncio.gather(*[asyncio.ensure_future(run_bot()),
                                         asyncio.ensure_future(client_tick_start()),
                                         asyncio.ensure_future(other_tasks())]))
