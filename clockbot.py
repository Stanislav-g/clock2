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






client = commands.Bot( command_prefix = '!')
client.remove_command('help')


@client.event

async def on_redy():
    print( 'Bot connected')







@client.command()
async def clock(ctx, now, time ):
    await ctx.author.send(f'Меня создал Nitagas')
    nowtime = int(now)
    vremiya = (['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
    getup = int(time)
    day = int(2400)
    if nowtime < getup:
        sleeptime = float(day - nowtime + getup - day)
        
        
        if sleeptime >= 100:      #часы
            end = sleeptime /100
            if end != vremiya:
                endt = end *60
                endth = endt *60
                
                await asyncio.sleep(endth)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
            else:
                sleeptimetwo = end *60
                endtwo = end *60
                endthe = int(endtwo +720)
                await asyncio.sleep(endthe)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
        else:
            f = nowtime
            ff = f[0], f[1]
            s = getup
            ss = f[0], f[1]
            if ff > ss and < 50:
                first = sleeptime - 40
                awaait asyncio.sleep(first)
                await ctx.author.send(f'hihihihi')
            else:
                sleeptimesec = sleeptime *60#минуты
                await asyncio.sleep(sleeptimesec)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
    else:
        sleeptime = float(day - nowtime + getup)
       
        
        if sleeptime >= 100:
            end = sleeptime /100
            if end != vremiya:
                endt = end *60
                endth = endt *60
                
                await asyncio.sleep(endth)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
            else:
                
                endt = end *60
                endth = endt *60
                endthe = int(endth +720)
                await asyncio.sleep(endthe)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
                await asyncio.sleep(1)
                await ctx.author.send(f'Вставай')
        else:
            sleeptimetwo = sleeptime *60
            await asyncio.sleep(sleeptimetwo)
            await ctx.author.send(f'Вставай')
            await asyncio.sleep(1)
            await ctx.author.send(f'Вставай')
            await asyncio.sleep(1)
            await ctx.author.send(f'Вставай')
            await asyncio.sleep(1)
            await ctx.author.send(f'Вставай')
            await asyncio.sleep(1)
            await ctx.author.send(f'Вставай')



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
                
token= os.environ.get('BOT_TOKEN')
client.run( token )
