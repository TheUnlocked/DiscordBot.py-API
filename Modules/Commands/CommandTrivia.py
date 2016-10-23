import json
import os
import random
import time
from enum import Enum

from discord import Message, Client, Server, Member

import Modules.Commands.CommandPerms as CommandPerm
import UnlockedBot as Ulb
from Modules.Commands.CommandBase import CommandBase
from Modules.InterfaceEvent import InterfaceOnClientTick
from Helper import TempTextChannel

games = []


class CommandTrivia(CommandBase, InterfaceOnClientTick):
    command_names = ['trivia']

    def __init__(self):
        super(CommandTrivia, self).__init__()

    def valid_usage(self, args: []):
        return (len(args) == 1 and args[0] == "tt") or \
               (len(args) > 1 and (args[0] == "sync" or args[0] == "async"))

    def get_usage_as_string(self):
        return '`trivia <tt/sync/async/spectate> [_competitors..._/_game\\_id_]'

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    def get_action_as_string(self):
        return 'A fun trivia game! Includes solo time trials as well as synchronous and asynchronous competitive!'

    async def command_action(self, message: Message, args: []):
        if args[0] == "tt":
            games.append(TriviaGame(message.channel.server, [message.author],
                                    GameType.TimeTrial, games[-1].game_id + 1 if len(games) > 0 else 0))
        if args[0] == "sync":
            if len(message.mentions) == len(args) - 1 and message.author not in message.mentions:
                games.append(TriviaGame(message.channel.server, message.mentions + [message.author],
                                        GameType.SyncMP, games[-1].game_id + 1 if len(games) > 0 else 0))
            else:
                await Ulb.send_message(message.channel, "Not all arguments were players", message.author)
        if args[0] == "async":
            if len(message.mentions) == len(args) - 1 and message.author not in message.mentions:
                games.append(TriviaGame(message.channel.server, message.mentions + [message.author],
                                        GameType.AsyncMP, games[-1].game_id + 1 if len(games) > 0 else 0))
            else:
                await Ulb.send_message(message.channel, "Not all arguments were players", message.author)

    async def on_client_tick(self):
        for game in games:
            if getattr(game, 'channel', 'None') != '':
                await game.on_client_tick()
            else:
                games.remove(game)

    async def on_message(self, message: Message):
        for game in games:
            await game.on_message(message)
        await super(CommandTrivia, self).on_message(message)


class GameType(Enum):
    TimeTrial = 1
    SyncMP = 2
    AsyncMP = 3


class TriviaGame:
    players = {}
    spectators = []
    answers = []

    def __init__(self, server: Server, users: [], mode: GameType, game_id: int):
        for player in users:
            self.players[player.name] = {}
            self.players[player.name]["points"] = 0
            self.players[player.name]["last_question"] = 0
            self.players[player.name]["answers"] = []
            self.players[player.name]["member"] = player
        self.game_mode = mode
        self.game_id = game_id
        Ulb.async_tasks.append({'func': self.set_channel, 'args': [server, users]})

    async def set_channel(self, args: []):
        self.channel = await TempTextChannel.new_text_channel(args[0], "trivia" + str(self.game_id), args[1])
        await Ulb.send_message(self.channel, "@here Game starting in 10 seconds...")

    async def on_message(self, message: Message):
        if getattr(self, 'channel', 'None') != '' and message.channel == self.channel and self.end_countdown == 0:
            if self.game_mode != GameType.AsyncMP and message.content.lower() in self.answers:
                await self.point(message.author)
            elif self.game_mode == GameType.AsyncMP and message.author.name in self.players and \
                            message.content.lower() in self.players[message.author.name]["answers"]:
                await self.point(message.author)

    last_question = 0
    time_left = 0
    start_countdown = 0
    end_countdown = 0

    GAME_LENGTH = 60

    async def on_client_tick(self):
        if self.start_countdown == 0:
            self.start_countdown = time.time()
        if self.start_countdown + 10 < time.time():
            if self.game_mode != GameType.AsyncMP:
                if self.last_question + 15 < time.time() and self.end_countdown == 0:
                    if self.time_left == 0:
                        self.time_left = time.time() + self.GAME_LENGTH
                    else:
                        await Ulb.send_message(self.channel,
                                               "You're taking too long. Hey, let's just skip this one for now.")
                    await self.new_question()
            else:
                for player in self.players.keys():
                    if self.players[player]["last_question"] + 15 < time.time() and self.end_countdown == 0:
                        if self.time_left == 0:
                            pass
                        else:
                            await Ulb.send_message(self.channel,
                                                   "You're taking too long. Hey, let's just skip this one for now.",
                                                   self.players[player]["member"])
                        await self.new_question(self.players[player]["member"])
                if self.time_left == 0:
                    self.time_left = time.time() + self.GAME_LENGTH
            if self.time_left - time.time() < 0 and not self.end_countdown > 0:
                winners = []
                for player in self.players.keys():
                    if len(winners) == 0:
                        winners.append(player)
                    elif self.players[player]["points"] > self.players[winners[0]]["points"]:
                        del winners[:]
                        winners.append(player)
                    elif self.players[player]["points"] == self.players[winners[0]]["points"]:
                        winners.append(player)
                if self.game_mode == GameType.TimeTrial:
                    await Ulb.send_message(self.channel,
                                           "@here You managed to get {0} {1}! Game ending in 10 seconds..."
                                           .format(str(self.players[winners[0]]["points"]),
                                                   "point" if self.players[winners[0]]["points"] == 1 else "points"))
                else:
                    winner_format = ', '.join(winners[:-1]) + (" and " if len(winners) > 1 else "") + winners[-1]
                    win_word = "won" if len(winners) == 1 else "tied"
                    await Ulb.send_message(self.channel, "@here {0} {1} with {2} {3}! Game ending in 15 seconds..."
                                           .format(winner_format, win_word, str(self.players[winners[0]]["points"]),
                                                   "point" if self.players[winners[0]]["points"] == 1 else "points"))
                self.end_countdown = time.time()
            if self.end_countdown > 0 and self.end_countdown + 15 < time.time():
                await TempTextChannel.close_channel(self.channel.server, "trivia" + str(self.game_id))
                self.channel = ""

    async def point(self, player: Member):
        if player.name in self.players:
            self.players[player.name]["points"] += 1
            if self.game_mode == GameType.TimeTrial:
                await Ulb.send_message(self.channel, "@here You have gotten it right! Alright, next question:")
                await self.new_question()
            elif self.game_mode == GameType.SyncMP:
                await Ulb.send_message(self.channel, "has gotten it right! Alright, next question:", player)
                await self.new_question()
            else:
                await Ulb.send_message(self.channel, "has gotten it right! Alright, next question:", player)
                await self.new_question(player)

    async def new_question(self, player: Member = None):
        with open(os.path.dirname(os.path.realpath(__file__)) + '\\trivia.json') as data_file:
            data = json.load(data_file)
        index = random.choice(range(len(data))) - 1
        await Ulb.send_message(self.channel, data[index]["question"], player)
        if self.game_mode != GameType.AsyncMP:
            self.answers = data[index]["answers"]
            self.last_question = time.time()
        else:
            self.players[player.name]["answers"] = data[index]["answers"]
            self.players[player.name]["last_question"] = time.time()
