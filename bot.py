import discord
from discord.ext import commands

BOT_TOKEN = 'MTI0MTkyOTU0Njk3MDY5NzkzOQ.GdlMxu.RaJvgnU3iC6vW-T8-0uEpiXRaqBVGrS--vvYkQ'

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if before.channel and before.channel.type == discord.ChannelType.stage_voice:
            print(f'{member} left the stage channel {before.channel.name}')
        elif after.channel and after.channel.type == discord.ChannelType.stage_voice:
            print(f'{member} joined the stage channel {after.channel.name}')
        elif before.channel and before.channel.type == discord.ChannelType.voice:
            print(f'{member} left the voice channel {before.channel.name}')
        elif after.channel and after.channel.type == discord.ChannelType.voice:
            print(f'{member} joined the voice channel {after.channel.name}')


bot.run(BOT_TOKEN)
