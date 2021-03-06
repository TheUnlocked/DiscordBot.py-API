"""
THIS IS AN ESSENTIAL FILE. DO NOT MODIFY OR REMOVE IT UNLESS SPECIFIED BY OTHER DOCUMENTATION.
"""

from discord import Client, Message, Member, User, Emoji, Channel, Server, Role
from fml.InterfaceEvent import *


def instantiate_events(client: Client):
    import DiscordBot as Bot

    @client.event
    async def on_ready():
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnReady):
                try:
                    await event.on_ready()
                except:
                    pass

    @client.event
    async def on_resumed():
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnResumed):
                try:
                    await event.on_resumed()
                except:
                    pass

    @client.event
    async def on_error(event, *args, **kwargs):
        for event_ in Bot.get_modules():
            if isinstance(event_, InterfaceOnError):
                try:
                    await event.on_error(event_, *args, **kwargs)
                except:
                    pass

    @client.event
    async def on_message(message: Message):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnMessage):
                try:
                    await event.on_message(message)
                except:
                    pass

    @client.event
    async def on_socket_raw_receive(msg):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnSocketRawReceive):
                try:
                    await event.on_socket_raw_receive(msg)
                except:
                    pass

    @client.event
    async def on_socket_raw_send(payload):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnSocketRawSend):
                try:
                    await event.on_socket_raw_send(payload)
                except:
                    pass

    @client.event
    async def on_message_delete(message: Message):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnMessageDelete):
                try:
                    await event.on_message_delete(message)
                except:
                    pass

    @client.event
    async def on_message_edit(before: Message, after: Message):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnMessageEdit):
                try:
                    await event.on_message_edit(before, after)
                except:
                    pass

    @client.event
    async def on_channel_delete(channel: Channel):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnChannelDelete):
                try:
                    await event.on_channel_delete(channel)
                except:
                    pass

    @client.event
    async def on_channel_create(channel: Channel):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnChannelCreate):
                try:
                    await event.on_channel_create(channel)
                except:
                    pass

    @client.event
    async def on_channel_update(before: Channel, after: Channel):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnChannelUpdate):
                try:
                    await event.on_channel_update(before, after)
                except:
                    pass

    @client.event
    async def on_member_join(member: Member):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnMemberJoin):
                try:
                    await event.on_member_join(member)
                except:
                    pass

    @client.event
    async def on_member_remove(member: Member):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnMemberRemove):
                try:
                    await event.on_member_remove(member)
                except:
                    pass

    @client.event
    async def on_member_update(before: Member, after: Member):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnMemberUpdate):
                try:
                    await event.on_member_update(before, after)
                except:
                    pass

    @client.event
    async def on_server_join(server: Server):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnServerJoin):
                try:
                    await event.on_server_join(server)
                except:
                    pass

    @client.event
    async def on_server_remove(server: Server):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnServerRemove):
                try:
                    await event.on_server_remove(server)
                except:
                    pass

    @client.event
    async def on_server_update(before: Server, after: Server):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnServerUpdate):
                try:
                    await event.on_server_update(before, after)
                except:
                    pass

    @client.event
    async def on_server_role_create(role: Role):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnServerRoleCreate):
                try:
                    await event.on_server_role_create(role)
                except:
                    pass

    @client.event
    async def on_server_role_delete(role: Role):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnServerRoleDelete):
                try:
                    await event.on_server_role_delete(role)
                except:
                    pass

    @client.event
    async def on_server_role_update(before: Role, after: Role):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnServerRoleUpdate):
                try:
                    await event.on_server_role_update(before, after)
                except:
                    pass

    @client.event
    async def on_server_emojis_update(before: [], after: []):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnServerEmojisUpdate):
                try:
                    await event.on_server_emojis_update(before, after)
                except:
                    pass

    @client.event
    async def on_server_available(server: Server):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnServerAvailable):
                try:
                    await event.on_server_available(server)
                except:
                    pass

    @client.event
    async def on_server_unavailable(server: Server):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnServerUnavailable):
                try:
                    await event.on_server_unavailable(server)
                except:
                    pass

    @client.event
    async def on_voice_state_update(before: Member, after: Member):
        for event in Bot.get_modules():
            if isinstance(event, OnVoiceStateUpdate):
                try:
                    await event.on_voice_state_update(before, after)
                except:
                    pass

    @client.event
    async def on_member_ban(member: Member):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnMemberBan):
                try:
                    await event.on_member_ban(member)
                except:
                    pass

    @client.event
    async def on_member_unban(server: Server, user: User):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnMemberUnban):
                try:
                    await event.on_member_unban(server, user)
                except:
                    pass

    @client.event
    async def on_typing(channel: Channel, user: User, when: datetime.datetime):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnTyping):
                try:
                    await event.on_typing(channel, user, when)
                except:
                    pass

    @client.event
    async def on_group_join(channel: Channel, user: User):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnGroupJoin):
                try:
                    await event.on_group_join(channel, user)
                except:
                    pass

    @client.event
    async def on_group_remove(channel: Channel, user: User):
        for event in Bot.get_modules():
            if isinstance(event, InterfaceOnGroupRemove):
                try:
                    await event.on_group_remove(channel, user)
                except:
                    pass
