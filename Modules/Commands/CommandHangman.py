import os
import random
import time

from discord import Message, Channel

import Modules.Commands.CommandPerms as CommandPerm
import UnlockedBot as Ulb
from InterfaceEvent import InterfaceOnClientTick
from Modules.Commands.CommandBase import CommandBase


class CommandHangman(CommandBase, InterfaceOnClientTick):
    command_names = ['hangman', 'hg']

    def valid_usage(self, args: []):
        return (not len(args) == 0) and (((args[0] == "start" or args[0] == 's') and (len(args) == 1 or
                                                                                      (len(args) == 2 and
                                                                                       args[1].isdigit() and
                                                                                       4 >= int(args[1]) >= 1))) or
                                         ((args[0] == "guess" or args[0] == 'g') and len(args) == 2
                                          and args[1].isalpha()) or
                                         ((args[0] == "reset" or args[0] == "r") and
                                          time.time() >= self.last_interact_time + 120 and len(args) == 1))

    def get_usage_as_string(self):
        return '`hangman|hg <guess|g/start|s/reset|r> [_word_/_letter_/_difficulty_(1-4)]'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    def get_action_as_string(self):
        return 'A game of hangman that you can play in discord. Fun for the whole family'

    last_interact_time = time.time()
    hangman_fails = 0
    hangman_field = "Γヿ\n|  {0}\n|  {2}{1}{3}\n| {4}{5}   {6}\n Guessed letters: {7}"
    hangman_characters = ['◯', '|', '/', '\\', '/', '\\']
    hangman_word = ''
    hangman_guesses = []
    hangman_channel = None

    def hangman_format_blanks(self):
        new_word = ''
        for letter in self.hangman_word:
            if letter in self.hangman_guesses:
                new_word += ' ' + letter
            else:
                new_word += ' \\_'
        return new_word

    def hangman_format_guesses(self):
        return ', '.join(self.hangman_guesses)

    async def send_current_hangman(self, channel: Channel):
        await Ulb.send_message(channel, self.hangman_field.format('◯' if self.hangman_fails >= 1 else '  ',
                                                                  '|' if self.hangman_fails >= 2 else '  ',
                                                                  '/' if self.hangman_fails >= 3 else '  ',
                                                                  '\\' if self.hangman_fails >= 4 else '  ',
                                                                  '/' if self.hangman_fails >= 5 else '  ',
                                                                  '\\' if self.hangman_fails >= 6 else '  ',
                                                                  self.hangman_format_blanks(),
                                                                  self.hangman_format_guesses()))

    def hangman_reset(self):
        self.hangman_fails = 0
        self.hangman_word = ''
        self.hangman_guesses = []

    async def command_action(self, message: Message, args: []):
        self.last_interact_time = time.time()
        self.hangman_channel = message.channel
        if (args[0] == "start" or args[0] == 's') and self.hangman_word == '':
            file_name = 'dict'
            if len(args) == 1:
                file_name += '2'
            else:
                if args[1] != '4':
                    file_name += args[1]
                else:
                    file_name += '3'
            with open(os.path.dirname(os.path.realpath(__file__)) + "\\" + file_name + ".txt", 'r') as myfile:
                dictionary = myfile.read().split('\n')
            if len(args) != 1 and args[1] == '4':
                dictionary = [word for word in dictionary if len(word) >= 6]
            elif file_name is not 'dict1':
                dictionary = [word for word in dictionary if 8 >= len(word) >= 5]
            else:
                dictionary = [word for word in dictionary if 8 >= len(word) >= 3]
            self.hangman_word = random.choice(dictionary)
            await Ulb.send_message(message.channel, "Starting Hangman...", message.author)
            await self.send_current_hangman(message.channel)
        if (args[0] == "guess" or args[0] == 'g') and not self.hangman_word == '':
            args[1] = args[1].lower()
            if len(args[1]) == 1:
                if args[1] in self.hangman_guesses:
                    await Ulb.send_message(message.channel, "That's already been guessed!", message.author)
                else:
                    self.hangman_guesses.append(args[1])
                    self.hangman_guesses = sorted(self.hangman_guesses)
                    if not args[1] in self.hangman_word:
                        self.hangman_fails += 1
                        await Ulb.send_message(message.channel,
                                               "There weren't any {1}'s!".format(self.hangman_word.count(args[1]),
                                                                                 args[1]), message.author)
                    else:
                        await Ulb.send_message(message.channel,
                                               "There {0} {1} {2}{3}!".format(
                                                   'was' if self.hangman_word.count(args[1]) == 1 else 'were',
                                                   self.hangman_word.count(args[1]), args[1],
                                                   '' if self.hangman_word.count(args[1]) == 1 else "'s"),
                                               message.author)
                    await self.send_current_hangman(message.channel)
                    if '_' not in self.hangman_format_blanks():
                        await Ulb.send_message(message.channel,
                                               'You managed to win with only {0} fails! Nice job!'
                                               .format(self.hangman_fails))
                        self.hangman_reset()
                    if self.hangman_fails >= 6:
                        await Ulb.send_message(message.channel,
                                               'You took too many tries! The word was {0}.'.format(self.hangman_word))
                        self.hangman_reset()
            else:
                if args[1] == self.hangman_word:
                    await Ulb.send_message(message.channel, "You guessed the word correctly!", message.author)
                    await Ulb.send_message(message.channel,
                                           'You managed to win with only {0} fails! Nice job!'
                                           .format(self.hangman_fails))
                    self.hangman_reset()
                else:
                    await self.send_current_hangman(message.channel)
                    self.hangman_fails += 1
                    await Ulb.send_message(message.channel, "{0} wasn't the correct word.".format(args[1]),
                                           message.author)
                    if self.hangman_fails >= 6:
                        await Ulb.send_message(message.channel,
                                               'You took too many tries! The word was {0}.'.format(self.hangman_word))
                        self.hangman_reset()
        if args[0] == "reset":
            await Ulb.send_message(message.channel, 'The game of hangman has been prematurely stopped!', message.author)
            self.hangman_reset()

    async def on_client_tick(self):
        if self.hangman_word != '' and self.last_interact_time + 300 < time.time():
            await Ulb.send_message(self.hangman_channel,
                                   "No one has done anything for a while so the game of hangman has reset.")
            self.hangman_reset()

    def __init__(self):
        super(CommandHangman, self).__init__()
