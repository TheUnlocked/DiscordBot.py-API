import discord
from discord import Message, Member

import DiscordBot as Ulb
import Modules.Commands.CommandPerms as CommandPerm
from Modules.Commands.CommandBase import CommandBase
from fml.InterfaceEvent import OnVoiceStateUpdate


class CommandTempVoice(CommandBase, OnVoiceStateUpdate):
    command_names = ['tempvoice']

    def valid_usage(self, args: []):
        return not len(args) == 0 if len(' '.join(args)) <= 93\
            else "The temporary voice channel name must be less than or equal to 93 characters."

    def get_usage_as_string(self):
        return '`tempvoice <Channel Name>'

    def valid_perms(self):
        return CommandPerm.CONNECT

    def get_action_as_string(self):
        return 'Creates a temporary voice channel that will remove itself once everyone leaves'

    async def command_action(self, message: Message, args: []):
        channel_name = ' '.join(args)
        if len(channel_name) <= 93:
            if message.author.voice.voice_channel is not None:
                vc = await Ulb.client.create_channel(message.server, channel_name + " [TEMP]",
                                                      type=discord.ChannelType.voice)
                await Ulb.client.move_member(message.author, vc)
                await Ulb.send_message(message.channel, "Voice channel successfully created.", message.author)
            else:
                await Ulb.send_message(message.channel,
                                       "You must join a voice channel before creating a temporary voice channel.",
                                       message.author)
        else:
            await Ulb.send_message(message.channel,
                                   "The temporary voice channel name must be less than 93 characters.", message.author)

    async def on_voice_state_update(self, before: Member, after: Member):
        # Delete temporary voice channels
        after_vc = after.voice.voice_channel
        before_vc = before.voice.voice_channel
        if before_vc is not None and before_vc.name.endswith(" [TEMP]"):
            if len(before_vc.voice_members) == 0:
                await Ulb.client.delete_channel(before_vc)

    def __init__(self):
        super(CommandTempVoice, self).__init__()
