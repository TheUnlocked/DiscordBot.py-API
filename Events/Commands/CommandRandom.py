from Events.Commands.CommandBase import CommandBase
from discord import Message, Client

import Events.Commands.CommandPerms as CommandPerm


class CommandRandom(CommandBase):
    command_names = ['random']
    beta = True

    def valid_usage(self, args: []):
        raise NotImplementedError("This command has no valid usage")

    def get_usage_as_string(self):
        raise NotImplementedError("This command has no valid usage")

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    async def command_action(self, message: Message, args: []):
        raise NotImplementedError("This command has no action")

    def get_action_as_string(self):
        raise NotImplementedError("This command has no action")

    def __init__(self, client: Client):
        super(CommandRandom, self).__init__(client)
