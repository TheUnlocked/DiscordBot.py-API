from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client
import Modules.Commands.CommandPerms as CommandPerm
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

    def valid_usage(self, args: []):
        num_args = 0
        for arg in args:
            if is_int(arg) and int(arg) > 0:
                num_args += 1
            else:
                num_args = 3
        return num_args == 1 or (num_args == 2 and int(args[0]) < int(args[1]))

    def get_usage_as_string(self):
        return "`random|rand [start:1] <end>"

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    async def command_action(self, message: Message, args: []):
        start = int(args[0]) if len(args) == 2 else 0
        end = int(args[1]) if len(args) == 2 else int(args[0])
        await Ulb.send_message(message.channel, str(random.randrange(start, end) + 1), message.author)

    def get_action_as_string(self):
        return "Gets a random number from a start value to an end value. Positive values only."

    def __init__(self):
        super(CommandRandom, self).__init__()


class CommandRoll(CommandBase):
    command_names = ['diceroll', 'roll']

    def valid_usage(self, args: []):
        if len(args) == 1:
            parts = args[0].lower().split('d')
            if len(parts) == 2 and ((is_int(parts[0]) and int(parts[0]) > 0) or parts[0] == '') \
                    and (is_int(parts[1]) and int(parts[1]) > 0):
                return True
        return False

    def get_usage_as_string(self):
        return "`diceroll|roll <[Number of Dice: 1]D<Number of sides>"

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    async def command_action(self, message: Message, args: []):
        parts = args[0].lower().split('d')
        num_dice = int(parts[0]) if parts[0] != '' else 1
        size_dice = int(parts[1])
        int_dice = []
        str_dice = []
        for i in range(num_dice):
            int_dice.append(random.randrange(size_dice) + 1)
            str_dice.append(str(int_dice[-1]))

        printout = "You rolled " + " + ".join(str_dice) + " = " + str(sum(int_dice)) if num_dice > 1\
            else "You rolled " + str_dice[0]
        await Ulb.send_message(message.channel, printout, message.author)

    def get_action_as_string(self):
        return "Gets a random number from a start value to an end value. Start value defaults to 1."

    def __init__(self):
        super(CommandRoll, self).__init__()


class CommandCoinflip(CommandBase):
    command_names = ['coinflip', 'flip']

    def valid_usage(self, args: []):
        return len(args) == 0

    def get_usage_as_string(self):
        return "`coinflip|flip"

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    async def command_action(self, message: Message, args: []):
        values = ["heads", "tails"]
        await Ulb.send_message(message.channel, "You flipped " + values[random.randrange(2)], message.author)

    def get_action_as_string(self):
        return "Gets a random number from a start value to an end value. Start value defaults to 1."

    def __init__(self):
        super(CommandCoinflip, self).__init__()
