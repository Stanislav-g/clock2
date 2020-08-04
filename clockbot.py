import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
from time import sleep
from colorsys import hls_to_rgb

import os

import random
from random import randint, choice, choices
import io
import sqlite3
import random as r

import io




client = commands.Bot( command_prefix = '!s')
client.remove_command('help')


@client.event
async def on_redy():
    print( 'Bot connected')      


   
@client.event
async def on_message ( message ):
    emj = str('👍')
    await message.add_reaction(emj)
    emji = str('👎')
    await message.add_reaction(emji)
        
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 728658937905414234: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '📖': # Emoji для реакций
            role = guild.get_role(728659726870511677) # ID Ролей для выдачи 
 
        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role)
                channel = client.get_channel( 738779492339941537 )
                await channel.send( embed = discord.Embed( description = f'Пользователь {member.mention}, поставил реакцию 📖 в канале правила') )
    

@client.command()
@commands.has_permissions(administrator = True)
async def send_m(ctx, member: discord.Member, *, arg):
    await ctx.channel.purge(limit = 1)
    await member.send('```' + arg + '```') 
    
token= os.environ.get('BOT_TOKEN')
client.run( token )
