from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client
import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Ulb


class CommandDebug(CommandBase):
    command_names = ['debug']

    def valid_usage(self, args: []):
        return True

    def get_usage_as_string(self):
        return '`debug [_args..._]'

    def valid_perms(self):
        return CommandPerm.ADMINISTRATOR

    def get_action_as_string(self):
        return 'UnlockedBot Debug Tools'

    async def command_action(self, message: Message, args: []):
        if args[0] == "ping" or args[0] == "test":
            await Ulb.send_message(message.channel, "pong")
        if args[0] == "clear":
            msg = "‌"
            for i in range(200):
                msg += "\n"
            msg += "Channel Cleared."
            for i in range(30):
                msg += "\n"
            msg += "‌"  # Uses ‌ character
            await Ulb.send_message(message.channel, msg)

        # DO NOT UNCOMMENT THIS UNLESS YOU ARE CURRENTLY BUGTESTING!
        # if args[0] == "exec":
        #     template = 'async def tmp():\n  {0}\n'
        #     d = dict(locals(), **globals())
        #     exec(template.format("  ".join(" ".join(args[1:]).split(".."))), d, d)
        #     await eval("tmp", d, d)()

    def __init__(self):
        super(CommandDebug, self).__init__()
