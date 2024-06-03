import os
import discord
import pytz

from discord import app_commands
from discord.ext import commands
from datetime import datetime
from gsheet.gsheet import GoogleSheet


TABLE_RANGE = 'A1:D1'
gs = GoogleSheet()

intents = discord.Intents.default()
intents.voice_states = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands!')
    except Exception as e:
        print(f'ERROR === bot.py -- 25: {e}')


@bot.tree.command(name="get_bot_email", description="Get Bot's Email")
async def get_bot_email(interaction: discord.Interaction):
    await interaction.response.send_message(f'Bot email: {gs.get_client_email()}')


@bot.tree.command(name="get_sheet", description="Get Sheet's Link")
async def get_sheet(interaction: discord.Interaction):
    await interaction.response.send_message(f'Sheet URL: {gs.url}')


@bot.tree.command(name='update_sheet', description="Update Sheet's Link")
@app_commands.describe(url='Sheet URL')
async def update_sheet(interaction: discord.Interaction, url: str):
    try:
        gs.update_url(url)
        await interaction.response.send_message(f'Sheet was updated successfully: {url}')
    except Exception as e:
        print(f'ERROR === bot.py -- 43: {e}')
        await interaction.response.send_message(f'ERROR: {e}')

        
@bot.tree.command(name='share_sheet', description="Share sheet with a specific email")
@app_commands.describe(email='Email')
async def share_sheet(interaction: discord.Interaction, email: str):
    try:
        gs.share_writer(email)
        await interaction.response.send_message(f'Sheet was shared successfully with {email}: {gs.url}')
    except Exception as e:
        print(f'ERROR === bot.py -- 52: {e}')
        await interaction.response.send_message(f'ERROR: {e}')


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if before.channel and before.channel.type == discord.ChannelType.stage_voice:
            print(f'{member} left the stage channel {before.channel.name}')
            channel = before.channel
            action = 'left'

        elif after.channel and after.channel.type == discord.ChannelType.stage_voice:
            print(f'{member} joined the stage channel {after.channel.name}')
            channel = after.channel
            action = 'join'

        elif before.channel and before.channel.type == discord.ChannelType.voice:
            print(f'{member} left the voice channel {before.channel.name}')
            channel = before.channel
            action = 'left'

        elif after.channel and after.channel.type == discord.ChannelType.voice:
            print(f'{member} joined the voice channel {after.channel.name}')
            channel = after.channel
            action = 'join'

        else:
            return
        
        wsheets = gs.sh.worksheets()
        now = datetime.now(pytz.timezone('Asia/Bangkok')).strftime("%Y-%m-%d %H:%M:%S")
        ws_title = f'{channel.name}'
        ws = None
        for _ws in wsheets:
            if ws_title == _ws.title:
                ws = _ws
                break

        if not ws:
            print(f'Create new worksheet: {ws_title}')
            ws = gs.sh.add_worksheet(ws_title, rows="100", cols="20")
            ws.append_row(['User', 'Action', 'Channel', 'Time'], table_range=TABLE_RANGE)
            ws.format(TABLE_RANGE, {'textFormat': {'bold': True}})

        ws.append_row([str(member), action, channel.name, now], table_range=TABLE_RANGE)
