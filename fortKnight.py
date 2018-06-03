import random
import asyncio
import discord
from discord.ext.commands import Bot
import twitter
#import requests as req

#Prefix for commands is set
bot = Bot(command_prefix = '.')

#On startup this message is shown on server side if everything and bot starts up fine
#Second line sets the Discord bot's playing status
@bot.event
async def on_ready():
	print("Let the battle begin")
	await bot.change_presence(game=discord.Game(name='.ask for help'))

# .ft command gives the name of a fortnite location
@bot.command(pass_context = True)
async def ft():
	places = ["Hero House", "Villain House", "Risky Reels", "Lucky Landing", "China Motel", "New Factories", "Motel", "anywhere you want", "Football Ground", "Between Shifty and Flush", "Container", "Jail", "North of Wailing Woods", "Anarchy Acres", "Dusty Divot", "Fatal Fields", "Flush Factory", "Greasy Grove", "Haunted Hills", "Junk Junction", "Lonely Lodge", "Loot Lake", "Moisty Mire", "Pleasant Park", "Retail Row", "Salty Springs", "Shifty Shafts", "Snobby Shores", "Tilted Towers", "Tomato Town", "Wailing Woods"]
	plc = random.choice(places)
	place = plc.lower()
	if plc == "anywhere you want":
		await bot.say("Go " + place)
	else:
		await bot.say("Go to " + place)

# .toss tosses a coin
@bot.command(pass_context = True)
async def toss():
	coin = ["Heads", "Tails"]
	flip = random.choice(coin)
	await bot.say("It is " + flip)

# .roll rolls a die
@bot.command(pass_context = True)
async def roll():
	dice = ["1", "2", "3", "4", "5", "6"]
	rolled = random.choice(dice)
	await bot.say("You have rolled a " + rolled)

# .tweet gets the (three) latest tweets by Fortnite
api = twitter.Api(consumer_key = 'consumer_key_here',
                  consumer_secret = 'consumer_secret_here',
                  access_token_key = 'access_token_key_here',
                  access_token_secret = 'access_token_secret_here')
t = api.GetUserTimeline(screen_name="FortniteGame", count=3)
tweets = [i.AsDict() for i in t]#Python List Comprehension
@bot.command(pass_context = True)
async def tweet():
	await bot.say("```Last three tweets by Fortnite official twitter handle:``` \n")
	for t in tweets:
		bird = t['text']
		await bot.say(bird)

#Help menu
ft = "`.ft`"
toss = "`.toss`"
roll = "`.roll`"
tweet = "`.tweet`"
help_menu = ft + ":    Random location chooser, gives a randomly choosen location to jump" + "\n\n" + toss + ": Tosses a coin for you" + "\n\n" + roll + ": Rolls a die for you" + "\n\n" + tweet + ": Displays the last three tweets by Fortnite's official handle"
@bot.command(pass_context = True)
async def ask():
	await bot.say(help_menu)

#TODO
#Get player data
#@bot.command(pass_context = True)
#async def player(nickname):
#	data = req.get("https://api.fortnitetracker.com/v1/profile/{platform}/{epic-nickname}", headers={"Api-Key": "API-KEY-HERE"})




bot.run("discord_secret_goes_here")