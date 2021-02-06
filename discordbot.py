import discord
from discord.ext import commands
import os
import traceback
from urllib import request as req
from urllib import parse

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()    
async def nyan(ctx):
    await ctx.send('mya-')


bot.run(token)
