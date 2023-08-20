# icornbytes
import discord, os, requests
from discord.ext import commands

TOKEN =  "MTE0MjYwNjUzMDkyMzk5NTIxNg.G6g78w.av-jB9gjTS2VSmtVuOpzxX02gVwfAImWhao4XQ"
#prefix itu yang ?samp ? namanya prefix
PREFIX = "?"

client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} - {client.user.id}')

@client.command()
async def samp(ctx, ip=None, port=None):
    if ip is None or port is None:
        embed = discord.Embed(title="(*) Error", description="`Please enter IP and port correctly.`", color=discord.Color.red())
        await ctx.reply(embed=embed)
        return
    try:
        response = requests.get(f"https://jade-doubtful-peacock.cyclic.cloud/api/samp?ip={ip}&port={port}")
        data = response.json()

        if "Something Went Wrong Please Check IP And Port Correctly or Please Try Again Later" in response.text:
            embed = discord.Embed(title="(*) Server Offline", description="`Something Went Wrong Please Check IP And Port Correctly or Please Try Again Later.`", color=discord.Color.red())
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Server Info", description="Informasi lengkap tentang server:", color=discord.Color.green())
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1142415595653042186/1142425790731014154/download_7.jpeg")
            embed.add_field(name="Server IP", value=data["response"]["serverip"])
            embed.add_field(name="Address", value=data["response"]["address"])
            embed.add_field(name="Gamemode", value=data["response"]["gamemode"])
            embed.add_field(name="Players Online", value=data["response"]["isPlayerOnline"])
            embed.add_field(name="Max Players", value=data["response"]["maxplayers"])
            embed.add_field(name="Hostname", value=data["response"]["hostname"])
            embed.add_field(name="Language", value=data["response"]["language"])
            embed.add_field(name="Password Protected", value=data["response"]["passworded"])
            embed.add_field(name="Lag Compensation", value=data["response"]["rule"]["lagcomp"])
            embed.add_field(name="Map Name", value=data["response"]["rule"]["mapname"])
            embed.add_field(name="Version", value=data["response"]["rule"]["version"])
            embed.add_field(name="Weather", value=data["response"]["rule"]["weather"])
            embed.add_field(name="Web URL", value=data["response"]["rule"]["weburl"])
            embed.add_field(name="World Time", value=data["response"]["rule"]["worldtime"])
            embed.add_field(name="Players In Game", value=data["response"]["isPlayersIngame"])
            await ctx.reply(embed=embed)
    except Exception as e:
        pass


try:
    client.run(TOKEN)
except discord.errors.HTTPException:
    os.system("python main.py")
    os.system('kill 1')
