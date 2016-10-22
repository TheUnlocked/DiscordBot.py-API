from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client

import Modules.Commands.CommandPerms as CommandPerm
import UnlockedBot as Ulb


class CommandLmgtfy(CommandBase):
    command_names = ['lmgtfy']

    def valid_usage(self, args: []):
        return len(args) > 0

    def get_usage_as_string(self):
        return '`lmgtfy <_phrase_>'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    def get_action_as_string(self):
        return 'Generates a LMGTFY (Let Me Google That For You) link'

    async def command_action(self, message: Message, args: []):
        await Ulb.send_message(message.channel, "http://lmgtfy.com/?q={0}".format('+'.join(args)), message.author)

    def __init__(self, client: Client):
        super(CommandLmgtfy, self).__init__(client)
