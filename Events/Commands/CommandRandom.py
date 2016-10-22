from Events.Commands.CommandBase import CommandBase
from discord import Message, Client
import Events.Commands.CommandPerms as CommandPerm
import UnlockedBot as Ulb
import random


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class CommandRandom(CommandBase):
    command_names = ['random', 'rand']
    beta = True

    def valid_usage(self, args: []):
        num_args = 0
        for arg in args:
            if is_int(arg):
                num_args += 1
            else:
                num_args = 3
        return num_args == 1 or (num_args == 2 and int(args[0]) < int(args[1]))

    def get_usage_as_string(self):
        return "`random|rand [start] <end>"

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    async def command_action(self, message: Message, args: []):
        start = int(args[0]) if len(args) == 2 else 0
        end = int(args[1]) if len(args) == 2 else int(args[0])
        await Ulb.send_message(message.channel, str(random.randrange(start, end) + 1), message.author)

    def get_action_as_string(self):
        return "Gets a random number from a start value to an end value. Start value defaults to 1."

    def __init__(self, client: Client):
        super(CommandRandom, self).__init__(client)
