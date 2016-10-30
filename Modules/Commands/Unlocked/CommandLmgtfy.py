from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client

import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Bot


class CommandLmgtfy(CommandBase):
    def __init__(self):
        super(CommandLmgtfy, self).__init__()
        self.command_names = ['lmgtfy']
        self.module_id = "0001_1004"

    def valid_usage(self, args: []):
        return len(args) > 0

    def get_usage_as_string(self):
        return 'lmgtfy <_phrase_>'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    def get_action_as_string(self):
        return 'Generates a LMGTFY (Let Me Google That For You) link'

    async def command_action(self, message: Message, args: []):
        await Bot.send_message(message.channel, "http://lmgtfy.com/?q={0}".format('+'.join(args)), message.author)
