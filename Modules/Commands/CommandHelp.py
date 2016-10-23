from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client
import Modules.Commands.CommandPerms as CommandPerm
import UnlockedBot as Ulb


class CommandHelp(CommandBase):
    command_names = ['help', '?']

    def valid_usage(self, args: []):
        return len(args) == 0 or len(args) == 1

    def get_usage_as_string(self):
        return '`help|? [_command\\_name_]'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    def get_action_as_string(self):
        return 'Shows the commands along with additional details about each of them'

    padding = 40

    def format_spacing(self, string: str, padding: int = padding):
        return string.ljust(padding, '.')

    async def command_action(self, message: Message, args: []):
        if len(args) == 0:
            commands = filter(lambda x: isinstance(x, CommandBase) and not x.beta, Ulb.event_effectors)
            printout = '\n`' + self.format_spacing("Command | alias") +\
                       self.format_spacing("Permissions", self.padding) + '`'
            printout += '\n`' + ''.join(['-'] * (self.padding + self.padding)) + '`'
            for command in commands:
                printout += '\n`' + self.format_spacing(' | '.join(command.command_names))\
                            + self.format_spacing(command.valid_perms().name, self.padding) + '`'
            await Ulb.send_message(message.channel, printout, message.author)
        if len(args) == 1:
            commands = filter(lambda x: isinstance(x, CommandBase), Ulb.event_effectors)
            for command in commands:
                if args[0] in command.command_names:
                    printout = "\n`Found help for '" + args[0] + "'`\nUsage: " + command.get_usage_as_string() + '\n' +\
                               command.get_action_as_string()
                    await Ulb.send_message(message.channel, printout, message.author)
                    return
            await Ulb.send_message(message.channel, "`Help for '" + args[0] + "' not found`", message.author)

    def __init__(self):
        super(CommandHelp, self).__init__()
