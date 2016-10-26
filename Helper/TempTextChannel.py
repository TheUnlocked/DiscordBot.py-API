import discord
import DiscordBot as Ulb


async def new_text_channel(server: discord.Server, channel_name: str, users: []):
    role = await Ulb.client.create_role(server)
    await Ulb.client.edit_role(server, role, name=channel_name + " [TEMP]")

    everyone = discord.PermissionOverwrite(read_messages=False)
    users_perms = discord.PermissionOverwrite(read_messages=True)
    channel = await Ulb.client.create_channel(server, channel_name + "_temp",
                                              (server.default_role, everyone), (role, users_perms))

    await allow_users(server, channel_name, users, role)
    return channel


async def allow_users(server: discord.Server, channel_name: str, users: [], role: discord.Role):
    for user in users:
        await Ulb.client.add_roles(user, role)


async def close_channel(server: discord.Server, channel_name: str):
    await Ulb.client.delete_role(server, next(filter(lambda x: x.name == channel_name + " [TEMP]", server.roles)))
    await Ulb.client.delete_channel(next(filter(lambda x: x.name == channel_name + "_temp", server.channels)))
