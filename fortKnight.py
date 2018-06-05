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

# .rps play rock, paper, scissor with the bot
@bot.command()
async def rps(playerChoice):
	frtnight = ["rock", "paper", "scissor"]
	botChoice = random.choice(frtnight)
	playerChoice = playerChoice.lower()
	if botChoice == playerChoice:
		await bot.say("You said " + playerChoice + " and I said " + botChoice + "\n" + "Its a tie!")
	elif botChoice == "rock" and playerChoice == "paper":
		await bot.say("You said paper and I said rock." + "\n" + "You won! I lost!")
	elif botChoice == "rock" and playerChoice == "scissor":
		await bot.say("You said scissor and I said rock." + "\n" + "I won! You lost! haha")
	elif botChoice == "paper" and playerChoice == "rock":
		await bot.say("You said rock and I said paper." + "\n" + "I won! You lost! haha")
	elif botChoice == "paper" and playerChoice == "scissor":
		await bot.say("You said scissor and I said paper." + "\n" + "You won! I lost!")
	elif botChoice == "scissor" and playerChoice == "paper":
		await bot.say("You said paper and I said scissor." + "\n" + "You won! I loose!")
	elif botChoice == "scissor" and playerChoice == "rock":
		await bot.say("You said rock and I said scissor." + "\n" + "You won! I lost!")

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
async def st(username):
	api_url = "https://fortnite.y3n.co/v2/player/{0}".format(username) #epicusername
	headers = {'User-Agent': 'nodejs request', 'X-Key': 'API-KEY-HERE'}
	response = req.get(api_url, headers = headers)
	data_acquired = json.loads(response.content.decode("utf-8"))
	await bot.say(data_acquired)
#TODO
#clean and beautify the json output into readable format


#Help menu
ft = "`.ft`"
toss = "`.toss`"
roll = "`.roll`"
tweet = "`.tweet`"
rps = "`.rps`"
gn = "`.gn`"
st = "`.st`"
help_menu = ft + ":    Random location chooser, gives a randomly choosen location to jump" + "\n\n" + toss + ": Tosses a coin for you" + "\n\n" + roll + ": Rolls a die for you" + "\n\n" + tweet + ": Displays the last three tweets by Fortnite's official handle" + "\n\n" + rps + ": Play Rock, Paper and Scissor" + "\n" + "Usage: " + "`.rps rock`" + "\n\n" + gn + ": Say Good Night to bot" + "\n\n" + st + ": Get player data" + "\n" + "Usage: " + "`.st \"epic username\"`"
@bot.command(pass_context = True)
async def ask():
	await bot.say(help_menu)


bot.run("discord_secret_goes_here")