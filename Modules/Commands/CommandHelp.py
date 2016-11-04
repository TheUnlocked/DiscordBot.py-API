"""
While this is not an essential file, if you do not modify or remove any part of this file, except for parts specifically intended to be modified
"""

from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client
import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Bot


class CommandHelp(CommandBase):
    def __init__(self):
        super(CommandHelp, self).__init__()
        self.command_names = ['help', '?']
        self.module_id = "0000_0003"

    def valid_usage(self, args: []):
        return len(args) == 0 or len(args) == 1

    def get_usage_as_string(self):
        return 'help|? [_command name_]'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    def get_action_as_string(self):
        return 'Shows the commands along with additional details about each of them'

    padding = 40

    def format_spacing(self, string: str, padding: int = padding):
        return string.ljust(padding, '.')

    async def command_action(self, message: Message, args: []):
        commands = filter(lambda x: isinstance(x, CommandBase) and not x.beta and not
                          (message.server.id in Bot.server_rules and
                           x.module_id in Bot.server_rules[message.server.id]["list"]), Bot.get_modules())
        if len(args) == 0:
            printout = '\n`' + self.format_spacing("Command | alias") + \
                       self.format_spacing("Permissions", self.padding) + '`'
            printout += '\n`' + ''.join(['-'] * (self.padding + self.padding)) + '`'
            for command in commands:
                printout += '\n`' + self.format_spacing(' | '.join(command.command_names)) \
                            + self.format_spacing(command.valid_perms().name, self.padding) + '`'
            await Bot.send_message(message.channel, printout, message.author)
        if len(args) == 1:
            for command in commands:
                if args[0].lower() in command.command_names:
                    printout = "\n`Found help for '" + args[0] + "'`\nUsage: " + command.get_usage_as_string() + '\n' + \
                               command.get_action_as_string()
                    await Bot.send_message(message.channel, printout, message.author)
                    return
            await Bot.send_message(message.channel, "`Help for '" + args[0] + "' not found`", message.author)
