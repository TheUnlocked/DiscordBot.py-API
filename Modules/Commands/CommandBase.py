"""
While this is not an essential file, if you do not modify or remove any part of this file, except for parts specifically intended to be modified
"""

import traceback
from enum import Enum

from discord import Message, Forbidden

import DiscordBot as Bot
import Modules.Commands.CommandPerms as CommandPerm
from fml.InterfaceEvent import InterfaceOnMessage


class CommandTriggerType(Enum):
    Prefix = 0
    Mention = 1
    Either = 2


class CommandBase(InterfaceOnMessage):
    def __init__(self):
        super(CommandBase, self).__init__()
        self.command_names = []
        self.module_id = "0000_0001"
        config = dict()
        config["trigger"] = 2
        config["prefix"] = '`'
        config["print_errors"] = True
        Bot.add_default_config("commands", config)

    def valid_usage(self, args: []):
        raise NotImplementedError("This command has no valid usage")

    def get_usage_as_string(self):
        raise NotImplementedError("This command has no valid usage")

    def valid_perms(self):
        return CommandPerm.NONE

    async def on_message(self, message: Message):
        command_prefix = Bot.get_config()["commands"]["prefix"]
        command_trigger = CommandTriggerType(Bot.get_config()["commands"]["trigger"])

        try:
            if command_trigger == CommandTriggerType.Prefix or command_trigger == CommandTriggerType.Either:
                if message.content.startswith(command_prefix):
                    spliced = message.content[len(command_prefix):].split(' ')
                    spliced = list(filter(None, spliced))
                    cmd = spliced[0]
                    args = spliced[1:]
                    if cmd in self.command_names and self.valid_usage(args) \
                            and self.valid_perms().func(message):
                        await self.command_action(message, args)
                        return

            if command_trigger == CommandTriggerType.Mention or command_trigger == CommandTriggerType.Either:
                if Bot.client.user in message.mentions:
                    spliced = "".join(message.content.split(message.server.get_member(Bot.client.user.id).mention))\
                        .split(' ')
                    spliced = list(filter(None, spliced))
                    if len(spliced) >= 1:
                        cmd = spliced[0]
                        args = spliced[1:]
                        if cmd in self.command_names and self.valid_usage(args) \
                                and self.valid_perms().func(message):
                            await self.command_action(message, args)
                            return

        except NotImplementedError as e:
            if Bot.get_config()["commands"]["print_errors"]:
                await Bot.send_message(message.channel, str(e))
        except Forbidden:
            if Bot.get_config()["commands"]["print_errors"]:
                await Bot.send_message(message.channel, "This bot doesn't have the permission to do that.", message.author)
        except Exception as e:
            if Bot.get_config()["commands"]["print_errors"]:
                await Bot.send_message(message.channel, str(e), message.author)
            traceback.print_exc()

    async def command_action(self, message: Message, args: []):
        raise NotImplementedError("This command has no action")

    def get_action_as_string(self):
        raise NotImplementedError("This command has no action")
