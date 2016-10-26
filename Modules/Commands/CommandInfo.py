"""
While this is not an essential file, if you do not modify or remove any part of this file, except for parts specifically intended to be modified
"""

from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client

import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Ulb


class CommandInfo(CommandBase):
    command_names = ['info']

    def valid_usage(self, args: []):
        return len(args) == 0

    def get_usage_as_string(self):
        return '`info'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    def get_action_as_string(self):
        return 'Bot info command'

    async def command_action(self, message: Message, args: []):
        msg = Ulb.INFO + \
                  "\n\n" \
                  "`discord.py v0.13.0`\n" \
                  "`DiscordBot.py-API beta m1`\n" \
                  "This bot is running on DiscordBot.py-API by Unlocked, which uses Rapptz's discord.py API wrapper. " \
                  "Both are open source and can be found on GitHub."
        await Ulb.send_message(message.channel, msg)

    def __init__(self):
        super(CommandInfo, self).__init__()
