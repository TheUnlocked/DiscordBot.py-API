"""
While this is not an essential file, if you do not modify or remove any part of this file, except for parts specifically intended to be modified
"""


class CommandPerm:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def rename_perm(self, name):
        self.name = name


def not_perm(perm):
    return CommandPerm("[NOT " + perm.name + "]", lambda *args: not perm.func(*args))


def and_perm(perm1, perm2):
    return CommandPerm("[" + perm1.name + " AND " + perm2.name + "]",
                       lambda *args: perm1.func(*args) and perm2.func(*args))


def or_perm(perm1, perm2):
    return CommandPerm("[" + perm1.name + " OR " + perm2.name + "]",
                       lambda *args: perm1.func(*args) or perm2.func(*args))


NONE = CommandPerm("None",
                   lambda message: True)

SEND_MESSAGES = CommandPerm("Send Messages",
                            lambda message: message.channel.permissions_for(message.author).send_messages)
SEND_MESSAGES_GLOBAL = CommandPerm("Send Messages (global)",
                                   lambda message: len(list(filter(lambda role: role.permissions.send_messages,
                                                                   message.author.roles))) > 0)
CONNECT = CommandPerm("Connect to VC",
                      lambda message: len(list(filter(lambda role: role.permissions.connect,
                                                      message.author.roles))) > 0)
MANAGE_MESSAGES = CommandPerm("Manage Messages",
                              lambda message: message.channel.permissions_for(message.author).manage_messages)

MANAGE_MESSAGES_GLOBAL = CommandPerm("Manage Messages (global)",
                                     lambda message: len(list(filter(lambda role: role.permissions.manage_messages,
                                                                     message.author.roles))) > 0)
ADMINISTRATOR = CommandPerm("Administrator",
                            lambda message: len(list(filter(lambda role: role.permissions.administrator,
                                                            message.author.roles))) > 0)

