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
import traceback

"""
Change this to the name of your bot.
"""
BOT_NAME = "WillyBot" if len(sys.argv) == 1 or not sys.argv[1].startswith("--name:") \
    else sys.argv[1].split("--name:")[1]

client = discord.Client()
loop = asyncio.get_event_loop()
watch_channels = []
shutdown_flag = False
bot_on = False
module_events = []
server_rules = {}


loc = os.environ['APPDATA'] + "\\" + BOT_NAME + "\\config.json"
if not os.path.exists(os.path.dirname(loc)) or not os.path.exists(loc):
    default = dict()
    default["modules"] = dict()
    default["modules"]["allon"] = True
    default["modules"]["include-system-mods"] = True
    default["modules"]["whitelist"] = []
    default["modules"]["blacklist"] = []
    default["commands"] = dict()
    default["commands"]["trigger"] = 2
    default["commands"]["prefix"] = '`'
    default["bot-info"] = ""
    os.makedirs(os.path.dirname(loc), exist_ok=True)
    f = open(loc, 'w')
    f.write(json.dumps(default, indent=4))
    f.close()
f = open(loc, 'r')
config = json.loads(f.read())
f.close()


def get_config():
    return config


def get_modules():
    return module_events


def get_module_by_id(identifier):
    for m in get_modules():
        if m.module_id == identifier:
            return m
    return None


def valid_module(mod_id, whitelist, blacklist):
    if mod_id in whitelist:
        return True
    if mod_id in blacklist:
        return False

    def match_wildcard(mod_id, wildcard_id):

        def expand_wildcard(wildcard_id):
            wc = wildcard_id.split("_")
            h1 = list(wc[0])
            h2 = wc[1]
            it = 0
            while len(h1) < 4:
                for i in range(len(h1)):
                    if h1[i] == '*':
                        h1.insert(i, '*')
                        break
                if it > 4:
                    return False
            it = 0
            while len(h2) < 4:
                for i in range(len(h1)):
                    if h2[i] == '*':
                        h2.insert(i, '*')
                        break
                if it > 4:
                    return False
            return "_".join(["".join(h1), "".join(h2)])

        wc_id = expand_wildcard(wildcard_id)
        for i in range(len(wc_id)):
            if wc_id[i] != '*' and wc_id[i] != mod_id[i]:
                return False, 0
        return True, wc_id.count('*')

    best_fit = False, 9
    for mid in whitelist:
        v = match_wildcard(mod_id, mid)
        if v[0] and v[1] < best_fit[1]:
            best_fit = True, v[1]
    for mid in blacklist:
        v = match_wildcard(mod_id, mid)
        if v[0] and v[1] < best_fit[1]:
            best_fit = False, v[1]
    return best_fit[0] if best_fit[1] != 9 else None


def get_client():
    return client


async def send_message(channel: Channel, msg: str, mention: Member = None):
    if mention is None:
        await client.send_message(channel, u'\u200B' + msg)
    else:
        await client.send_message(channel, u'\u200B' + mention.mention + ' ' + msg)


async def run_bot():
    filename = os.environ['APPDATA'] + "\\" + BOT_NAME + "\\token.txt"
    if not os.path.exists(filename):
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


INFO = get_config()["bot-info"]

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
                        event = obj()
                        verdict = valid_module(event.module_id, get_config()["modules"]["whitelist"], get_config()["modules"]["blacklist"])
                        if verdict is None:
                            if get_config()["modules"]["allon"] or \
                                (get_config()["modules"]["include-system-mods"] and
                                 event.module_id.split("_")[0] == "0000"):
                                module_events.append(event)
                        elif verdict:
                            module_events.append(event)
                    except:
                        pass

print(module_events)
fml.EventInstantiator.instantiate_events(client)

loop.run_until_complete(asyncio.gather(*[asyncio.ensure_future(run_bot()),
                                         asyncio.ensure_future(client_tick_start()),
                                         asyncio.ensure_future(other_tasks())]))
