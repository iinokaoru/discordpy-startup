import discord
from discord.ext import commands
import os
import traceback
from urllib import request as req
from urllib import parse

client = commands.Bot(command_prefix='/')
TOKEN = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@client.command()
async def ping(ctx):
    await ctx.send('pong')
    
@client.command()    
async def nyan(ctx):
    await ctx.send('mya-')


bot.run(TOKEN)
