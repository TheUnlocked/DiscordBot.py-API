import discord
import datetime


class InterfaceEvent:
    beta = False

    def __init__(self):
        pass


class InterfaceOnClientTick:
    async def on_client_tick(self):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnReady(InterfaceEvent):
    async def on_ready(self):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnResumed(InterfaceEvent):
    async def on_resumed(self):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnError(InterfaceEvent):
    async def on_error(self, event_method, *args, **kwargs):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnMessage(InterfaceEvent):
    async def on_message(self, message: discord.Message):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnSocketRawReceive(InterfaceEvent):
    async def on_socket_raw_receive(self, msg):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnSocketRawSend(InterfaceEvent):
    async def on_socket_raw_send(self, msg):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnMessageDelete(InterfaceEvent):
    async def on_message_delete(self, message: discord.Message):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnMessageEdit(InterfaceEvent):
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnChannelDelete(InterfaceEvent):
    async def on_channel_delete(self, channel: discord.Channel):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnChannelCreate(InterfaceEvent):
    async def on_channel_create(self, channel: discord.Channel):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnChannelUpdate(InterfaceEvent):
    async def on_channel_update(self, before: discord.Channel, after: discord.Channel):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnMemberJoin(InterfaceEvent):
    async def on_member_join(self, member: discord.Member):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnMemberRemove(InterfaceEvent):
    async def on_member_remove(self, member: discord.Member):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnMemberUpdate(InterfaceEvent):
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnServerJoin(InterfaceEvent):
    async def on_server_join(self, server: discord.Server):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnServerRemove(InterfaceEvent):
    async def on_server_remove(self, server: discord.Server):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnServerUpdate(InterfaceEvent):
    async def on_server_update(self, before: discord.Server, after: discord.Server):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnServerRoleCreate(InterfaceEvent):
    async def on_server_role_create(self, role: discord.Role):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnServerRoleDelete(InterfaceEvent):
    async def on_server_role_delete(self, role: discord.Role):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnServerRoleUpdate(InterfaceEvent):
    async def on_server_role_update(self, before: discord.Role, after: discord.Role):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnServerEmojisUpdate(InterfaceEvent):
    async def on_server_emojis_update(self, before: [], after: []):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnServerAvailable(InterfaceEvent):
    async def on_server_available(self, server: discord.Server):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnServerUnavailable(InterfaceEvent):
    async def on_server_unavailable(self, server: discord.Server):
        raise NotImplementedError("This does not exist yet")


class OnVoiceStateUpdate(InterfaceEvent):
    async def on_voice_state_update(self, before: discord.Member, after: discord.Member):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnMemberBan(InterfaceEvent):
    async def on_member_ban(self, server: discord.Server, user: discord.User):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnMemberUnban(InterfaceEvent):
    async def on_member_unban(self, server: discord.Server, user: discord.User):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnTyping(InterfaceEvent):
    async def on_typing(self, channel: discord.Channel, user: discord.User, when: datetime.datetime):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnGroupJoin(InterfaceEvent):
    async def on_group_join(self, channel: discord.Channel, user: discord.User):
        raise NotImplementedError("This does not exist yet")


class InterfaceOnGroupRemove(InterfaceEvent):
    async def on_group_remove(self, channel: discord.Channel, user: discord.User):
        raise NotImplementedError("This does not exist yet")
