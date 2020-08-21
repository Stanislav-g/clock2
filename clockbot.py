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

#autorole
@client.event

async def on_member_join( member ):
    channel = client.get_channel( 705461507953262793 )

    role = discord.utils.get( member.guild.roles, id = 705364781753958450 )

    await member.add_roles( role )
    await channel.send( embed = discord.Embed( description = f'Пользователь {member.mention}, присоеденился к нам! Пригласил {member.inviter}') )
    emb = discord.Embed( title = 'INFO', colour = discord.Color.red() )
    emb.add_field( name = 'ИНФОРМАЦИЯ',value = 'Добро пожаловать на наш сервер, ознакомьтесь с правилами нашего сервера\nПропиши команду -help что-бы узнать мои комманды\nПолезные команды:\n-help\n$help\n\n**ОБЯЗАТЕЛЬНО ПРОЧИТАЙТЕ ПРАВИЛА НА СЕРВЕРЕ И НАЖМИТЕ НА РЕАКЦИЮ 📖**')
    await member.send( embed = emb )
   
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
                channel = client.get_channel( 738779492339941537 )
                await channel.send( embed = discord.Embed( description = f'Пользователь {member.mention}, поставил реакцию 📖 в канале правила') )
            
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
                

@client.command()
@commands.has_permissions(administrator = True)
async def send_m(ctx, member: discord.Member, *, arg):
    await ctx.channel.purge(limit = 1)
    await member.send('```' + arg + '```') 
    
token= os.environ.get('BOT_TOKEN')
client.run( token )
