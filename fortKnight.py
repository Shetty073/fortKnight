#!/usr/bin/env python
__author__ = "Ashish Shetty aka AlphaSierra,"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "AlphaSierra"
__status__ = "In Progress"


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
	rolled = random.randint(1,6)
	await bot.say("You have rolled a " + rolled)

# .rps play rock, paper, scissor with the bot
@bot.command()
async def rps(playerChoice):
	frtnight = ["rock", "paper", "scissor"]
	botChoice = random.choice(frtnight)
	playerChoice = playerChoice.lower()
	if botChoice == playerChoice:
		await bot.say("You said " + playerChoice + " and the Bot said " + botChoice + "\n" + "Its a tie!")
	elif botChoice == "rock" and playerChoice == "paper":
		await bot.say("You said paper and the Bot said rock." + "\n" + "You won! the Bot lost!")
	elif botChoice == "rock" and playerChoice == "scissor":
		await bot.say("You said scissor and the Bot said rock." + "\n" + "the Bot won! You lost! haha")
	elif botChoice == "paper" and playerChoice == "rock":
		await bot.say("You said rock and the Bot said paper." + "\n" + "the Bot won! You lost! haha")
	elif botChoice == "paper" and playerChoice == "scissor":
		await bot.say("You said scissor and the Bot said paper." + "\n" + "You won! the Bot lost!")
	elif botChoice == "scissor" and playerChoice == "paper":
		await bot.say("You said paper and the Bot said scissor." + "\n" + "You won! the Bot loose!")
	elif botChoice == "scissor" and playerChoice == "rock":
		await bot.say("You said rock and the Bot said scissor." + "\n" + "You won! the Bot lost!")

# .gn say good night to bot
@bot.command()
async def gn():
	await bot.say("Good Night" + "\n" + ":fist: :sweat_drops:")

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

# Get player data
@bot.command()
async def st(*,username):# Using * symbol our command can accept a username which consists of more than one word
	api_url = f"https://fortnite.y3n.co/v2/player/{username}"
	headers = {'User-Agent': 'nodejs request', 'X-Key': 'API-KEY-HERE'}
	response = req.get(api_url, headers = headers)
	data_acquired = json.loads(response.content.decode("utf-8"))
	displayName = data_acquired['displayName']
	battle_royale = data_acquired['br']
	stats = battle_royale['stats']
	pc = stats['pc']
	solo = pc['solo']
	duo = pc['duo']
	squad = pc['squad']
	_all = pc['all']

	#Squad_Data
	squad_kills = str(squad['kills'])
	squad_matchesPlayed = str(squad['matchesPlayed'])
	squad_lastMatch = str(squad['lastMatch'])
	squad_minutesPlayed = str(squad['minutesPlayed'])
	squad_wins = str(squad['wins'])
	squad_top3 = str(squad['top3'])
	squad_top6 = str(squad['top6'])
	squad_deaths = str(squad['deaths'])
	squad_kpd = str(squad['kpd'])
	squad_kpm = str(squad['kpm'])
	#squad_tpm = str(squad['tpm'])
	squad_score = str(squad['score'])
	squad_winRate = str(squad['winRate'])

	#Duo_Data
	duo_kills = str(duo['kills'])
	duo_matchesPlayed = str(duo['matchesPlayed'])
	duo_lastMatch = str(duo['lastMatch'])
	duo_minutesPlayed = str(duo['minutesPlayed'])
	duo_wins = str(duo['wins'])
	duo_top5 = str(duo['top5'])
	duo_top12 = str(duo['top12'])
	duo_deaths = str(duo['deaths'])
	duo_kpd = str(duo['kpd'])
	duo_kpm = str(duo['kpm'])
	#duo_tpm = str(duo['tpm'])
	duo_score = str(duo['score'])
	duo_winRate = str(duo['winRate'])
	
	#Solo_Data
	solo_kills = str(solo['kills'])
	solo_matchesPlayed = str(solo['matchesPlayed'])
	solo_lastMatch = str(solo['lastMatch'])
	solo_minutesPlayed = str(solo['minutesPlayed'])
	solo_wins = str(solo['wins'])
	solo_top10 = str(solo['top10'])
	solo_top25 = str(solo['top25'])
	solo_deaths = str(solo['deaths'])
	solo_kpd = str(solo['kpd'])
	solo_kpm = str(solo['kpm'])
	#solo_tpm = str(solo['tpm'])
	solo_score = str(solo['score'])
	solo_winRate = str(solo['winRate'])
	
	#All_Data
	all_kills = str(_all['kills'])
	all_matchesPlayed = str(_all['matchesPlayed'])
	all_minutesPlayed = str(_all['minutesPlayed'])
	all_wins = str(_all['wins'])
	all_score = str(_all['score'])
	all_kpm = str(_all['kpm'])
	#all_tpm = str(_all['tpm'])
	all_deaths = str(_all['deaths'])
	all_kpd = str(_all['kpd'])
	all_lastMatch = str(_all['lastMatch'])
	all_spm = str(_all['spm'])
	all_winRate = str(_all['winRate'])

	#Add VIP/battlestar to displayname if player has ever won
	if _all['wins'] >= 1:
		displayName = "<:battlestar:431861736597880837>" + displayName
	else:
		displayName = displayName

	#Output the data
	bold_solo = "__**SOLO**__"
	bold_squad = "__**SQUADS**__"
	bold_duo = "__**DUOS**__"
	bold_all = "__**ALL**__"

	discordOutSquads = bold_squad + ":" + "\n" + "Kills: " + squad_kills + "\n" + "Total matches played: " + squad_matchesPlayed + "\n" + "Last match played: " + squad_lastMatch + "\n" + "Total Minutes played: " + squad_minutesPlayed + "\n" + "No. of wins: " + squad_wins + " <:vr:431861842952978452>" + "\n" + "No. of times in top 3: " + squad_top3 + "\n" + "No. of times in top 6: " + squad_top6 + "\n" + "Total no. of deaths: " + squad_deaths + "\n" + "Kills per death/match: " + squad_kpd + "\n" + "Kills per minute: " + squad_kpm + "\n" + "Score: " + squad_score + "\n" + "Winrate: " + squad_winRate + "\n\n"
	discordOutSolo = bold_solo + ":" + "\n" + "Kills: " + solo_kills + "\n" + "Total matches played: " + solo_matchesPlayed + "\n" + "Last match played: " + solo_lastMatch + "\n" + "Total Minutes played: " + solo_minutesPlayed + "\n" + "No. of wins: " + solo_wins + " <:vr:431861842952978452>" + "\n" + "No. of times in top 10: " + solo_top10 + "\n" + "No. of times in top 25: " + solo_top25 + "\n" + "Total no. of deaths: " + solo_deaths + "\n" + "Kills per death/match: " + solo_kpd + "\n" + "Kills per minute: " + solo_kpm + "\n" + "Score: " + solo_score + "\n" + "Winrate: " + solo_winRate + "\n\n"
	discordOutDuos = bold_duo + ":" + "\n" + "Kills: " + duo_kills + "\n" + "Total matches played: " + duo_matchesPlayed + "\n" + "Last match played: " + duo_lastMatch + "\n" + "Total Minutes played: " + duo_minutesPlayed + "\n" + "No. of wins: " + duo_wins + " <:vr:431861842952978452>" + "\n" + "No. of times in top 5: " + duo_top5 + "\n" + "No. of times in top 12: " + duo_top12 + "\n" + "Total no. of deaths: " + duo_deaths + "\n" + "Kills per death/match: " + duo_kpd + "\n" + "Kills per minute: " + duo_kpm + "\n" + "Score: " + duo_score + "\n" + "Winrate: " + duo_winRate + "\n\n"
	discordOutAll = bold_all + ":" + "\n" + "Kills: " + all_kills + "\n" + "Total matches played: " + all_matchesPlayed + "\n" + "Total Minutes played: " + all_minutesPlayed + "\n" + "No. of wins: " + all_wins + " <:vr:431861842952978452>" + "\n" + "Total no. of deaths: " + all_deaths + "\n" + "Kills per death/match: " + all_kpd + "\n" + "Kills per minute: " + all_kpm + "\n" + "Score: " + all_score + "\n" + "Winrate: " + all_winRate + "\n\n"

	#Output to server formatted:
	discordOut = "Match stats for " + "__**" + displayName + "**__" + ":" + "\n\n" + discordOutSquads + discordOutDuos + discordOutSolo + discordOutAll
	#Output
	await bot.say(discordOut)

#Get fortnite server status
@bot.command()
async def svr():
	status_url = "https://fortnite.y3n.co/v2/gamestatus"
	headers_1 = {'User-Agent': 'nodejs request', 'X-Key': 'API-KEY-HERE'}
	response_1 = req.get(status_url, headers = headers_1)
	data_status = json.loads(response_1.content.decode("utf-8"))
	status = data_status['status']#Fortnite server status
	message = data_status['message']#server status message
	#maintenanceUri = data_status['maintenanceUri']
	status_str = "Server is " + f"{status}." + "\n" + f"{ message}."
	await bot.say(status_str)

#Get todays shop items
@bot.command()
async def shp():
	shop_url = "https://fortnite.y3n.co/v2/shop"
	headers_2 = {'User-Agent': 'nodejs request', 'X-Key': 'API-KEY-HERE'}
	response_2 = req.get(shop_url, headers = headers_2)
	shop_status = json.loads(response_2.content.decode("utf-8"))
	#print(list(shop_status.keys())) TEST checking for keys available
	br_shop = shop_status['br']
	#print(list(br_shop.keys())) TEST checking for keys available
	wk_shop = br_shop['weekly']
	dl_shop = br_shop['daily']
	wk_item1 = wk_shop[0]
	wk_item2 = wk_shop[1]
	dl_item1 = dl_shop[0]
	dl_item2 = dl_shop[1]
	dl_item3 = dl_shop[2]
	dl_item4 = dl_shop[3]
	dl_item5 = dl_shop[4]
	dl_item6 = dl_shop[5]

	#weekly items/images
	wk_item1_url = wk_item1['imgURL']
	wk_item2_url = wk_item2['imgURL']

	#daily items/images
	dl_item1_url = dl_item1['imgURL']
	dl_item2_url = dl_item2['imgURL']
	dl_item3_url = dl_item3['imgURL']
	dl_item4_url = dl_item4['imgURL']
	dl_item5_url = dl_item5['imgURL']
	dl_item6_url = dl_item6['imgURL']

#	bold_shopitm = "__**Today's shop items are**__" THIS METHOD HAS EMBEDDING ISSUES AS 8 IMAGES ARE THERE
#	shop_out = bold_shopitm + ":" + wk_item1_url + "\n" + wk_item2_url + "\n" + dl_item1_url + "\n" + dl_item2_url + "\n" + dl_item3_url + "\n" + dl_item4_url + "\n" + dl_item5_url + "\n" + dl_item6_url + "\n"
#	await bot.say(shop_out)

	await bot.say("__**Today's shop items are**__")
	await bot.say(wk_item1_url)
	await bot.say(wk_item2_url)
	await bot.say(dl_item1_url)
	await bot.say(dl_item2_url)
	await bot.say(dl_item3_url)
	await bot.say(dl_item4_url)
	await bot.say(dl_item5_url)
	await bot.say(dl_item6_url)


#Help menu
ft = "`.ft`"
toss = "`.toss`"
roll = "`.roll`"
tweet = "`.tweet`"
rps = "`.rps`"
gn = "`.gn`"
st = "`.st`"
svr = "`.svr`"
shp = "`.shp`"
help_menu = ft + ":    Random location chooser, gives a randomly choosen location to jump" + "\n\n" + toss + ": Tosses a coin for you" + "\n\n" + roll + ": Rolls a die for you" + "\n\n" + tweet + ": Displays the last three tweets by Fortnite's official handle" + "\n\n" + rps + ": Play Rock, Paper and Scissor" + "\n" + "Usage: " + "`.rps rock`" + "\n\n" + gn + ": Say Good Night to bot" + "\n\n" + st + ": Get player data" + "\n" + "Usage: " + "`.st \"epic username\"`" + "\n\n" + svr + ": Get the Fortnite server status. Whether the servers are UP or DOWN" + "\n\n" + shp + ": Get today's items from the item shop" + "\n\n" + "Say NO to <:vbuck:431861845318696972> scams! Stay away from scam sites offering free <:vbuck:431861845318696972>"
@bot.command(pass_context = True)
async def ask():
	await bot.say(help_menu)


bot.run("discord_secret_goes_here")

#!!!ALERT!!!
# These custom emojis will not work on your server. Because you have to use your own custom emojis and their respective ids which you have added on your server
# for more information you can google "use custom emojis discord.py" and read the reddit or stack-overflow links as this is already answered I will not be explaining
# it in readme.

#Custom emojis will have a unique id just like these:
#<:vbuck:431861845318696972>
#<:battlestar:431861736597880837>
#<:vr:431861842952978452>