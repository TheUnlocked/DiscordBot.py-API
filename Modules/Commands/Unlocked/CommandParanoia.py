from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client
import Modules.Commands.CommandPerms as CommandPerm


class CommandParanoia(CommandBase):
    def __init__(self):
        super(CommandParanoia, self).__init__()
        self.currently_playing = False
        self.beta = True
        self.command_names = ['paranoia']
        self.module_id = "0001_1003"

    def valid_usage(self, args: []):
        return True

    def get_usage_as_string(self):
        return '`paranoia <_players..._>'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    async def on_message(self, message: Message):
        await super(CommandParanoia, self).on_message(message)

    async def command_action(self, message: Message, args: []):
        raise NotImplementedError("This command has no action")

    def get_action_as_string(self):
        return "A game of paranoia and secret paranoia."
