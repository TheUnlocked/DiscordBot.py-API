from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client
import Modules.Commands.CommandPerms as CommandPerm


class CommandParanoia(CommandBase):
    currently_playing = False

    beta = True
    command_names = ['paranoia', 'sparanoia']

    def valid_usage(self, args: []):
        return True

    def get_usage_as_string(self):
        return '`paranoia|sparanoia <_players..._>'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    async def on_message(self, message: Message):
        await super(CommandParanoia, self).on_message(message)

    async def command_action(self, message: Message, args: []):
        raise NotImplementedError("This command has no action")

    def get_action_as_string(self):
        return "A game of paranoia and secret paranoia."

    def __init__(self):
        super(CommandParanoia, self).__init__()
