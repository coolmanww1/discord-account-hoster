import discord
from discord.ext import commands
import json

geb = commands.Bot(command_prefix=".", help_command=None, self_bot=True)
token = ""

# made by Geb#1337

@geb.event
async def on_ready():
    await geb.change_presence(status=discord.Status.online)
    print('Logged in as {0.user}'.format(geb))

geb.run(token, bot=False)
