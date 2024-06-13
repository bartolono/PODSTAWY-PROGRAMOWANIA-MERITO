import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print(f'Zalogowano jako {bot.user}!')
        print('Komendy zostały zsynchronizowane pomyślnie')
    except Exception as e:
        print(f'Błąd podczas synchronizacji komend: {e}')

@bot.tree.command(name='avatar', description='Pobierz avatar użytkownika')
async def avatar(interaction: discord.Interaction, member: discord.Member = None):
    member = member or interaction.user
    embed = discord.Embed(title=f'Avatar użytkownika {member}', color=discord.Color.blue())
    embed.set_image(url=member.avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='banner', description='Pobierz baner użytkownika')
async def banner(interaction: discord.Interaction, member: discord.Member = None):
    member = member or interaction.user
    user = await bot.fetch_user(member.id)

    if user.banner:
        embed = discord.Embed(title=f'Baner użytkownika {member}', color=discord.Color.blue())
        embed.set_image(url=user.banner.url)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(f'Użytkownik "{member}" nie ma ustawionego baneru.')

@bot.tree.command(name='avataribanner', description='Pobierz avatar i baner użytkownika')
async def userinfo(interaction: discord.Interaction, member: discord.Member = None):
    member = member or interaction.user
    user = await bot.fetch_user(member.id)

    embed = discord.Embed(title=f'Użytkownik: "{member}"', color=discord.Color.blue())
    embed.set_thumbnail(url=member.avatar.url)

    if user.banner:
        embed.set_image(url=user.banner.url)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='roll', description='Rzuć kostką d20')
async def roll(interaction: discord.Interaction):
    result = random.randint(1, 20)
    await interaction.response.send_message(f'Użytkownik "{interaction.user}" rzucił kostką d20 i wylosował: {result}')

@bot.tree.command(name='ask', description='Zadaj pytanie, a bot odpowie (losowo)')
async def ask(interaction: discord.Interaction, question: str):
    answers = ["Tak", "Nie", "Nie wiem"]
    response = random.choice(answers)
    await interaction.response.send_message(f'Pytanie od użytkownika "{interaction.user}": {question}\nOdpowiedź: {response}')

bot.run(TOKEN)