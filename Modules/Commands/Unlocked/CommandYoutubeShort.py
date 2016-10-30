from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client

import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Ulb


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def rev(l):
    new = l[:]
    new.reverse()
    return new


class CommandYoutubeShort(CommandBase):
    def __init__(self):
        super(CommandYoutubeShort, self).__init__()
        self.command_names = ['ytshort']
        self.module_id = "0001_1009"

    def valid_usage(self, args: []):
        return 0 < len(args) < 3 and \
               len(args[0].split("https://www.youtube.com/watch?v=")) > 0 and \
               (len(args) == 1 or (len(args) == 2 and len(args[1].split(':')) < 4 and is_int("".join(args[1].split(':')))))

    def get_usage_as_string(self):
        return 'ytshort <_https://youtube.com/watch?v= link_> [_time code in hh:mm:ss_]'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    def get_action_as_string(self):
        return 'Generates a shortened youtube video link'

    async def command_action(self, message: Message, args: []):
            code = args[0].split('https://www.youtube.com/watch?v=')[1].split('&')[0]\
                if args[0][0] == "h"\
                else args[0].split('https://www.youtube.com/watch?v=')[1].split('&')[0][:-1]
            h = 0
            m = 0
            s = 0
            if len(args) > 1:
                h = 0 if len(args[1].split(':')) != 3 else rev(args[1].split(':'))[2]
                m = 0 if len(args[1].split(':')) < 2 else rev(args[1].split(':'))[1]
                s = rev(args[1].split(':'))[0]
            await Ulb.send_message(message.channel, "https://youtu.be/{0}?t={1}h{2}m{3}s".format(code, h, m, s))
