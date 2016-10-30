from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client

import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Ulb


class CommandAddrule(CommandBase):
    def __init__(self):
        super(CommandAddrule, self).__init__()
        self.command_names = ['addrule']
        self.module_id = "0000_1004"
        self.beta = True

    def valid_usage(self, args: []):
        return len(args) == 1

    def get_usage_as_string(self):
        return 'addrule <_module id_>'

    def valid_perms(self):
        return CommandPerm.ADMINISTRATOR

    def get_action_as_string(self):
        return 'Generates a LMGTFY (Let Me Google That For You) link'

    async def command_action(self, message: Message, args: []):
        await Ulb.send_message(message.channel, "http://lmgtfy.com/?q={0}".format('+'.join(args)), message.author)
