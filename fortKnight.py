#Fortknight-bot by Shetty073

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print("Let the battle begin")

@bot.command(pass_context=True)
async def ft():
	places = ["Lucky Landing", "Factories near Dusty Depot", "Motel", "Somewhere between Retail, Jail and Factories", "Football Ground", "Between Shifty and Flush", "Container", "Jail", "North of Wailing Woods", "Anarchy Acres", "Dusty Depot", "Fatal Fields", "Flush Factory", "Greasy Grove", "Haunted Hills", "Junk Junction", "Lonely Lodge", "Loot Lake", "Moisty Mire", "Pleasant Park", "Retail Row", "Salty Springs", "Shifty Shafts", "Snobby Shores", "Tilted Towers", "Tomato Town", "Wailing Woods"]
	await bot.say(random.choice(places))


bot.run("secret goes here")
