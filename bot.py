# bot.py
import flask
import os
import random
import discord
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown

from discord import Intents
#this is for webhosting
from keep_alive import keep_alive
#what are your intents with my daughter?
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

#Giving Bot commands prefix with !, you can use multiple if you want, as in: command_prefix='!', '?', '/', 
client = commands.Bot(command_prefix='!', intents=intents)

#Lists for the map, likely to be moved into an Sqlite database later.

Erangel_list = ["Georgopol", "Novorepnoye", "Pochinki", "Yasnaya Polyana", "Gatka", "Kameshki", "Lipovka", "Mylta", "Primorsk", "Rozhok", "Severny", "Stalber", "Zharki", "Island", "Military Base"]
Vikendi_list = ["Dobro Mesto", "Goroka", "Podvosto", "Volnova", "Abbey", "Cantra", "Krichas", "Milnar", "Movatra", "Pilnec", "Peshkova", "Tovar", "Trevno", "Vihar", "Zabava", "Dino Park", "Castle", "Cement Factory", "Cosomodrome", "Hot Springs", "Villa", "Lumber Yard", "Mount Kreznic","Port", "Sawmill", "Winery"]
Miramar_list = ["Chumacera","El Pozo","La Cobreria", "Los Leones", "Valle del Mar", "Monte Nuevo", "San Martin", "Cruz del Valle", "El Azahar","Impala", "Los Higos", "Pecado", "Puerto Paraíso", "Tierra Bronca", "Torre Ahumada", "La Bendita", "Hacienda del Patrón", "Prison"]
Sanhok_list = ["Ban Tai", "Camp Alpha", "Camp Bravo", "Camp Charlie", "Ha Tinh", "Khao", "Pai Nan", "Tat Mok", "Cave", "Bhan", "Docks", "Lakawi", "Mongnai", "Na  Kham", "Resort", "Tambang", "Temple", "Quarry"]
Taego_list = ["Wol Song", "Army Base", "Ship yard", "Airport", "Hae Moo Sa", "Go Dok", "Yong Cheon", "Terminal", "Palace", "Ha Po", "Fishing camp", "Ho San", "Buk San Sa", "Kang Neung", "Oh Hyang", "Studio", "Song Am", "School", "Prison"]
Deston_list = ["Buxley", "Cavala", "El Koro", "Los Arcos", "Ripton", "Sancarna", "Arema", "Assembly", "Concert", "Construction Site", "Hydroelectric Dam", "Lodge", "Swamp", "Ten Forts", "Wind Farms", "Carpenter's End", "Holston Meadows", "Barclift"]
Rondo_list = ["Min Hu", "Nan Chuan", "Rai An", "Kun Xia", "Bei Li", "Mu Ho Pan", "Hemay Town", "Stadium", "Bamboo", "Test Track", "Neox Factory", "Lo Hua Xing", "Mey Ran", "Jao Tin", "Fong Tun", "Yu Lin", "Dan Ching", "Tu Ling", "Jadena City", "Lan Po", "Long Ho", "Rin Jiang", "Hung Shan", "Tin Long Garden", "Yun Gu"]
Maps_list = ["available maps: Vikendi, Miramar, Erangel, Sanhok, Taego, Deston, Rondo"]


# Dot env for the token and server ID's, those are stored in a separate file called .env

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


# Client responses, this is gonna be reworked into something cleaner.
@client.command(aliases=['Erangel','erangel'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def _Erangel(ctx):
    await ctx.send(random.choice(Erangel_list))

@client.command(aliases=['Vikendi', 'vikendi'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def _Vikendi(ctx):
    await ctx.send(random.choice(Vikendi_list))

@client.command(aliases=['Miramar', 'miramar'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def _Miramar(ctx):
    await ctx.send(random.choice(Miramar_list))

@client.command(aliases=['Sanhok', 'sanhok'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def _Sanhok(ctx):
    await ctx.send(random.choice(Sanhok_list))

@client.command(aliases=['Maps','maps'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def _Maps(ctx):
    await ctx.send(Maps_list)

@client.command(aliases=['Test','test'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def _Test(ctx):
    await ctx.send("Hello does this mic work? 1-2,1-2")

@client.command(aliases=['Taego','taego'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def _Taego(ctx):
    await ctx.send(random.choice(Taego_list))

@client.command(aliases=['Deston','deston'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def _Deston(ctx):
    await ctx.send(random.choice(Deston_list))    

@client.command(aliases=['Rondo','rondo'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def _Rondo(ctx):
    await ctx.send(random.choice(Rondo_list))

#Error handling for excessive use
@_Erangel.error
@_Vikendi.error
@_Miramar.error
@_Sanhok.error
@_Taego.error
@_Deston.error
@_Rondo.error
@_Maps.error
@_Test.error
async def on_command_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f"You're too many commands too fast. Try again in {error.retry_after:.2f} seconds.")
    else:
        print(f"Error occurred: {error}")
        await ctx.send(f"An error occurred: {str(error)}")


#Reference to the webhost file    
keep_alive()

client.run(TOKEN)
