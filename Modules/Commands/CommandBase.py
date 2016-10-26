import traceback
from enum import Enum

from discord import Message, Forbidden

import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Ulb
from InterfaceEvent import InterfaceOnMessage


class CommandTriggerType(Enum):
    Prefix = 1
    Mention = 2
    Either = 3


# feel free to change these!
command_prefix = '`'
command_trigger = CommandTriggerType.Either


class CommandBase(InterfaceOnMessage):
    command_names = []

    def valid_usage(self, args: []):
        raise NotImplementedError("This command has no valid usage")

    def get_usage_as_string(self):
        raise NotImplementedError("This command has no valid usage")

    def valid_perms(self):
        return CommandPerm.NONE

    async def on_message(self, message: Message):
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
                if Ulb.client.user in message.mentions:
                    spliced = "".join(message.content.split(message.server.get_member(Ulb.client.user.id).mention))\
                        .split(' ')
                    spliced = list(filter(None, spliced))
                    cmd = spliced[0]
                    args = spliced[1:]
                    if cmd in self.command_names and self.valid_usage(args) \
                            and self.valid_perms().func(message):
                        await self.command_action(message, args)
                        return

        except NotImplementedError as e:
            await Ulb.send_message(message.channel, str(e))
        except Forbidden:
            await Ulb.send_message(message.channel, "This bot doesn't have the permission to do that.", message.author)
        except Exception as e:
            await Ulb.send_message(message.channel, str(e), message.author)
            traceback.print_exc()

    async def command_action(self, message: Message, args: []):
        raise NotImplementedError("This command has no action")

    def get_action_as_string(self):
        raise NotImplementedError("This command has no action")

    def __init__(self):
        super(CommandBase, self).__init__()
