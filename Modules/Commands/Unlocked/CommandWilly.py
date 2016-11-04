from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client
import time
import random

import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Bot


class CommandHelloWilly(CommandBase):
    def __init__(self):
        super(CommandHelloWilly, self).__init__()
        self.command_names = ['hello', 'hi', 'hey']
        self.module_id = "0001_1100"

    def valid_usage(self, args: []):
        return len(args) == 0

    def get_usage_as_string(self):
        return 'hello|hi|hey <_phrase_>'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    def get_action_as_string(self):
        return 'Says hello to Willy'

    async def command_action(self, message: Message, args: []):
        random.seed(int(time.time() / 800))
        available = random.choice([True, False])
        msg = "#######\n" \
              "##• # •##\n" \
              "#)-------(#\n" \
              "#######" if available else \
              "_WillyBot 4000 is out mining right now_"
        await Bot.send_message(message.channel, msg)
