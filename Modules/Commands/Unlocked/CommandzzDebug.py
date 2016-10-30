from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client
import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Bot


class CommandDebug(CommandBase):
    def __init__(self):
        super(CommandDebug, self).__init__()
        self.command_names = ['debug']
        self.module_id = "0001_0000"


    def valid_usage(self, args: []):
        return True

    def get_usage_as_string(self):
        return 'debug [_args..._]'

    def valid_perms(self):
        return CommandPerm.ADMINISTRATOR

    def get_action_as_string(self):
        return 'UnlockedBot Debug Tools'

    async def command_action(self, message: Message, args: []):
        if args[0] == "ping" or args[0] == "test":
            await Bot.send_message(message.channel, "pong")
        if args[0] == "clear":
            msg = "‌"
            for i in range(200):
                msg += "\n"
            msg += "Channel Cleared."
            for i in range(30):
                msg += "\n"
            msg += "‌"  # Uses ‌ character
            await Bot.send_message(message.channel, msg)
        if args[0] == 'override':
            method = getattr(Bot.get_module_by_id(args[1]), args[2])
            await method(message, *args[3:])

        # DO NOT UNCOMMENT THIS UNLESS YOU ARE CURRENTLY BUGTESTING!
        # if args[0] == "exec":
        #     template = 'async def tmp():\n  {0}\n'
        #     d = dict(locals(), **globals())
        #     exec(template.format("  ".join(" ".join(args[1:]).split(".."))), d, d)
        #     await eval("tmp", d, d)()
