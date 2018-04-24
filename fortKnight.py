#Fortknight-bot by Shetty073

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
from bs4 import BeautifulSoup as bs
import requests as req

#status grabber code starts
page = req.get("https://lightswitch-public-service-prod06.ol.epicgames.com/lightswitch/api/service/bulk/status?serviceId=Fortnite")
soup = bs(page.content, "html.parser")
status = soup.prettify()
update = "UP"
#status grabber code ends

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print("Let the battle begin")

@bot.command(pass_context=True)
async def ft():
	places = ["Lucky Landing", "Factories near Dusty Depot", "Motel", "Somewhere between Retail, Jail and Factories", "Football Ground", "Between Shifty and Flush", "Container", "Jail", "North of Wailing Woods", "Anarchy Acres", "Dusty Depot", "Fatal Fields", "Flush Factory", "Greasy Grove", "Haunted Hills", "Junk Junction", "Lonely Lodge", "Loot Lake", "Moisty Mire", "Pleasant Park", "Retail Row", "Salty Springs", "Shifty Shafts", "Snobby Shores", "Tilted Towers", "Tomato Town", "Wailing Woods"]
	await bot.say(random.choice(places))

#status grabber command code
@bot.command(pass_context=True)
async def st():
	if update in status:
		await bot.say("Grab your guns! 'cause Fortnite servers are UP and running!")
	else:
		await bot.say("Fortnite servers are DOWN!")

bot.run("secret goes here")
