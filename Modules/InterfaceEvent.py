import discord


class InterfaceEvent(discord.Client):
    beta = False

    def __init__(self, client: discord.Client):
        pass


class InterfaceClientTick:
    def __init__(self, client: discord.Client):
        pass

    async def on_client_tick(self):
        raise NotImplementedError("This does not exist yet")


class InterfaceMessageEvent(InterfaceEvent):
    async def on_message(self, message: discord.Message):
        raise NotImplementedError("This does not exist yet")


class InterfaceVoiceEvent(InterfaceEvent):
    async def on_voice_state_update(self, before: discord.Member, after: discord.Member):
        raise NotImplementedError("This does not exist yet")
