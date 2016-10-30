import json
import traceback
import urllib.request
from Modules.Commands.CommandBase import CommandBase
from discord import Message, Client
import Modules.Commands.CommandPerms as CommandPerm
import DiscordBot as Ulb


class CommandDictionary(CommandBase):
    def __init__(self):
        super(CommandDictionary, self).__init__()
        self.command_names = ['definition', 'define']
        self.module_id = "0001_1005"

    def valid_usage(self, args: []):
        return len(args) == 1 and args[0].isalpha()

    def get_usage_as_string(self):
        return "`definition|define|def <_word_>"

    def valid_perms(self):
        return CommandPerm.SEND_MESSAGES

    request_url = "http://api.pearson.com/v2/dictionaries/laad3/entries?headword={0}&limit=1"
    result_text = "Found definition for `{0}`:\nPart of speech: `{1}`\n`{2}`"

    async def command_action(self, message: Message, args: []):
        try:
            data = json.loads(urllib.request.urlopen(self.request_url.format(args[0])).read().decode('utf-8'))
            if len(data["results"]) > 0:
                headword = data["results"][0]["headword"]
                pos = data["results"][0]["part_of_speech"]
                try:
                    definition = data["results"][0]["senses"][0]["definition"]
                    await Ulb.send_message(message.channel, self.result_text.format(headword, pos, definition),
                                           message.author)
                except:
                    await Ulb.send_message(message.channel,
                                           "No definition for `{0}` found and no fallback was provided".format(args[0]),
                                           message.author)
            else:
                await Ulb.send_message(message.channel, "No definition for `{0}` found".format(args[0]), message.author)
        except Exception as e:
            traceback.print_exc()

    def get_action_as_string(self):
        return "Gets the definition of the searched word"
