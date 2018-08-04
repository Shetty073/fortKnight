import discord
import twitter
from discord.ext import commands
import requests as req
from random import choice
import json
import configparser


# Using configparser get the token from configuration file
config = configparser.ConfigParser()
config.read("config.ini")
TOKEN = config["BOT"]["token"]
CONSUMER_KEY = config["TWITTER"]["consumer_key"]
CONSUMER_SECRET = config["TWITTER"]["consumer_secret"]
ACCESS_TOKEN_KEY = config["TWITTER"]["access_token_key"]
ACCESS_TOKEN_SECRET = config["TWITTER"]["access_token_secret"]
API_KEY = config["FORTNITE"]["st_key"]

# Bot code begins
bot = commands.Bot(command_prefix='.', description="just `.ask` for help", case_insensitive=True)

@bot.event
async def on_ready():
	print(bot.user.name)
	print("Let the battle begin")
	await bot.change_presence(activity=discord.Game("just .ask for help"))

# Say good night to members
@bot.event
async def on_message(msg):
	message = msg.content.lower()
	auth = msg.author.name
	ch = msg.channel
	if message == "good night" or message == "gn":
		await ch.send(f"Good Night {auth}")
	await bot.process_commands(msg)

# .ft command gives the name of a fortnite location
@bot.command()
async def ft(ctx):
	places = ["Risky Reels", "Lucky Landing", 
	"China Motel", "New Factories", "Motel", "anywhere you want", 
	"Football Ground", "Between Shifty and Flush", "Container", "Paradise Palms",
	"North of Wailing Woods","Dusty Divot","Fatal Fields", "Flush Factory", 
	"Greasy Grove", "Haunted Hills", "Junk Junction", "Lonely Lodge", 
	"Loot Lake","Pleasant Park", "Retail Row", "Salty Springs", "Lazy Links",
	"Shifty Shafts", "Snobby Shores", "Tilted Towers", "Tomato Town", "Wailing Woods"]
	place = choice(places)
	if place == "anywhere you want":
		await ctx.send(f"Go {place}..")
	else:
		await ctx.send(f"Go to {place}")

# .roll rolls a die
@bot.command()
async def roll(ctx):
	await ctx.send(f"You have rolled a {choice(range(1, 7))}")

# .toss toss a coin
@bot.command()
async def toss(ctx):
	coin = choice(("Heads", "Tails"))
	await ctx.send(f"It's {coin}")

# .tweet gets the latest tweet by Fortnite
@bot.command()
async def tweet(ctx):
	birds = []
	api = twitter.Api(consumer_key=CONSUMER_KEY,
                   consumer_secret=CONSUMER_SECRET,
                   access_token_key=ACCESS_TOKEN_KEY,
                   access_token_secret=ACCESS_TOKEN_SECRET)
	t = api.GetUserTimeline(screen_name="FortniteGame", count=3)
	tweets = [i.AsDict() for i in t]
	for t in tweets:
		birds.append(t['text'] + "\n")
	
	tweet_embed = discord.Embed(
		title="@FortniteGame on twitter",
		type="rich",
		description="Latest 3 tweets",
		colour=discord.Colour.blue()
	)
	tweet_embed.set_author(name="FortniteGame on twitter:",
                        icon_url="https://i.imgur.com/JijqpW9.jpg")
	tweet_embed.add_field(name="Tweet 1", value=birds[0], inline=False)
	tweet_embed.add_field(name="Tweet 2", value=birds[1], inline=False)
	tweet_embed.add_field(name="Tweet 3", value=birds[2], inline=False)
	await ctx.send(embed=tweet_embed)

# Get player data
@bot.command()
async def st(ctx,*epic_name):
	try:
		st_url = "https://fortnite-public-api.theapinetwork.com/prod09/users/id"
		st_headers = {'Authorization': API_KEY}
		st_data = req.post(st_url, data={'username': epic_name}, headers=st_headers)
		st_json = json.loads(st_data.content.decode("utf-8"))
	except Exception as e:
		await ctx.send(f"API error!! Error code: {e}")
		# Get stats
	try:
		s_url = "https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats"
		s_headers = {'Authorization': API_KEY}
		s_data = req.post(s_url, data={
                    'user_id': st_json["uid"], 'platform': 'pc', 'window': "alltime"}, headers=s_headers)
		s_json = json.loads(s_data.content.decode("utf-8"))
	except Exception as e:
		await ctx.send(f"API error!! Error code: {e}")
	s_json_stat = s_json["stats"]
	s_json_totals = s_json["totals"]
	usr = s_json["username"]
	win_pr = s_json["window"]
	s_json_stat_embed = ""
	s_json_totals_embed = ""  # this is for the embed
	for k, v in s_json_stat.items():
		s_json_stat_embed += f"**{k}**: {v}\n"
	for k, v in s_json_totals.items():
		s_json_totals_embed += f"**{k}**: {v}\n"
	st_embed = discord.Embed(
		title="Player statistics",
		type="rich",
		description="Platform: PC",
		colour=discord.Colour.purple()
	)
	st_embed.set_author(name=f"Showing stats of {usr} for {win_pr}",
					icon_url="https://i.imgur.com/JijqpW9.jpg")
	st_embed.add_field(name="Squad/Duo/Solo: ", 
						value=f"{s_json_stat_embed}\n\n", inline=False)
	st_embed.add_field(name="Total overall: ",
	            		value=f"{s_json_totals_embed}", inline=False)
	await ctx.send(embed=st_embed)

# Show in-game shop items
@bot.command()
async def shp(ctx):
	items_url = "https://fortnite-public-api.theapinetwork.com/prod09/store/get"
	items_headers = {'Authorization': '9f3b02bcaa8a878ef1cfe176ed8670b5'}
	items_data = req.post(
		items_url, data={'language': 'en'}, headers=items_headers)
	items_json = json.loads(items_data.content.decode('utf-8'))
	items = items_json["items"]
	name_list = []
	price_list = []
	image_list = []
	type_list = []
	rarity_list = []
	for item in items:
		name_list.append(item["name"])
		price_list.append(item["cost"])
		image_list.append(item["item"]["image"])
		type_list.append(item["item"]["type"])
		rarity_list.append(item["item"]["rarity"])
	shp_items = ""
	shp_embed = discord.Embed(
		title="In-game shop items list (daily updated)\n\n THIS FEATURE IS INCOMPLETE! FOR NOW, IT WILL TAKE SOME TIME TO IMPLEMENT",
		type="rich",
		description="Bot developer: AlphaSierra",
		colour=discord.Colour.gold()
	)
	shp_embed.set_author(name=f"Today's shop items are: ",
                      icon_url="https://i.imgur.com/JijqpW9.jpg")
	# item 1
	shp_embed.set_image(url=f"{image_list[0]}")
	shp_embed.add_field(name=f"Item name:",
                     value=f"{name_list[0]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item price:",
                     value=f"{price_list[0]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item rarity:",
                     value=f"{rarity_list[0]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item type:",
                     value=f"{type_list[0]}\n\n", inline=False)

	# item 2
	shp_embed.set_image(url=f"{image_list[1]}")
	shp_embed.add_field(name=f"Item name:",
                     value=f"{name_list[1]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item price:",
                     value=f"{price_list[1]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item rarity:",
                     value=f"{rarity_list[1]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item type:",
                     value=f"{type_list[1]}\n\n", inline=False)

	# item 3
	shp_embed.set_image(url=f"{image_list[2]}")
	shp_embed.add_field(name=f"Item name:",
                     value=f"{name_list[2]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item price:",
                     value=f"{price_list[2]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item rarity:",
                     value=f"{rarity_list[2]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item type:",
                     value=f"{type_list[2]}\n\n", inline=False)

	# item 4
	shp_embed.set_image(url=f"{image_list[3]}")
	shp_embed.add_field(name=f"Item name:",
                     value=f"{name_list[3]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item price:",
                     value=f"{price_list[3]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item rarity:",
                     value=f"{rarity_list[3]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item type:",
                     value=f"{type_list[3]}\n\n", inline=False)
	
	# item 5
	shp_embed.set_image(url=f"{image_list[4]}")
	shp_embed.add_field(name=f"Item name:",
                     value=f"{name_list[4]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item price:",
                     value=f"{price_list[4]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item rarity:",
                     value=f"{rarity_list[4]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item type:",
                     value=f"{type_list[4]}\n\n", inline=False)

	# item 6
	shp_embed.set_image(url=f"{image_list[5]}")
	shp_embed.add_field(name=f"Item name:",
                     value=f"{name_list[5]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item price:",
                     value=f"{price_list[5]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item rarity:",
                     value=f"{rarity_list[5]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item type:",
                     value=f"{type_list[5]}\n\n", inline=False)

	# item 7
	shp_embed.set_image(url=f"{image_list[6]}")
	shp_embed.add_field(name=f"Item name:",
                     value=f"{name_list[6]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item price:",
                     value=f"{price_list[6]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item rarity:",
                     value=f"{rarity_list[6]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item type:",
                     value=f"{type_list[6]}\n\n", inline=False)

	# item 8
	shp_embed.set_image(url=f"{image_list[7]}")
	shp_embed.add_field(name=f"Item name:",
                     value=f"{name_list[7]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item price:",
                     value=f"{price_list[7]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item rarity:",
                     value=f"{rarity_list[7]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item type:",
                     value=f"{type_list[7]}\n\n", inline=False)

	# item 9
	shp_embed.set_image(url=f"{image_list[8]}")
	shp_embed.add_field(name=f"Item name:",
                     value=f"{name_list[8]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item price:",
                     value=f"{price_list[8]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item rarity:",
                     value=f"{rarity_list[8]}\n\n", inline=False)
	shp_embed.add_field(name=f"Item type:",
                     value=f"{type_list[8]}\n\n", inline=False)

	await ctx.send(embed=shp_embed)

# Get list of all available weapons in-game
@bot.command()
async def wlist(ctx):
	weaponList_url = "http://www.fortnitechests.info/api/weapons"
	header_weaponList = {'accept': 'application/json'}
	response_3 = req.get(weaponList_url, headers=header_weaponList)
	weaponList_acquired = json.loads(response_3.content.decode("utf-8"))

	# Get the list of all weapons by using the key 'name'
	wList = [d['name'] for d in weaponList_acquired if 'name' in d]
	# Using list(set()) get rid of duplicate entries in our list
	wList = list(set(wList))

	# Below code is written on purpose instead of using loops to prevent the bot from sending too many messages at once
	wp1 = wList[0]
	wp2 = wList[1]
	wp3 = wList[2]
	wp4 = wList[3]
	wp5 = wList[4]
	wp6 = wList[5]
	wp7 = wList[6]
	wp8 = wList[7]
	wp9 = wList[8]
	wp10 = wList[9]
	wp11 = wList[10]
	wp12 = wList[11]
	wp13 = wList[12]
	wp14 = wList[13]
	wp15 = wList[14]
	wp16 = wList[15]
	wp17 = wList[16]
	wp18 = wList[17]
	wp19 = wList[18]
	wp20 = wList[19]
	wp21 = wList[20]
	wp22 = wList[21]
	wp23 = wList[22]
	wp24 = wList[23]
	wp25 = wList[24]

	# Ready for output
	wList = wp1 + "\n" + wp2 + "\n" + wp3 + "\n" + wp4 + "\n" + wp5 + "\n" + wp6 + "\n" + wp7 + "\n" + wp8 + "\n" + wp9 + "\n" + wp10 + "\n" + wp11 + \
            "\n" + wp12 + "\n" + wp13 + "\n" + wp14 + "\n" + wp15 + "\n" + wp16 + "\n" + wp17 + "\n" + wp18 + \
            "\n" + wp19 + "\n" + wp20 + "\n" + wp21 + "\n" + \
            wp22 + "\n" + wp23 + "\n" + wp24 + "\n" + wp25 + "\n"
	wlist_embed = discord.Embed(
                    title="Get the list of all available in-game weapons",
                    type="rich",
                    description="Weapons List",
                    colour=discord.Colour.blurple()
                )
	wlist_embed.set_author(name=f"Fortnite: Battle Royale",
                      icon_url="https://i.imgur.com/JijqpW9.jpg")
	wlist_embed.add_field(name="List:",
                     value=f"{wList}\n\n", inline=False)
	await ctx.send(embed=wlist_embed)

# Gets details of weapon by name and rarity
@bot.command()
async def wstat(ctx, weaponRarity, *, weaponName):
	# API call and raw response
	weapons_stats = "http://www.fortnitechests.info/api/weapons"
	header_for_wstats = {'accept': 'application/json'}
	response_4 = req.get(weapons_stats, headers=header_for_wstats)

	if response_4.status_code == 200:
		wstats_acquired = json.loads(response_4.content.decode("utf-8"))
		try:
				# Processing response for individual data
			weaponName = weaponName.title()
			weaponRarity = weaponRarity.lower()
			weapon = list(filter(
				lambda weapon: weapon['name'] == f'{weaponName}' and weapon['rarity'] == f'{weaponRarity}', wstats_acquired))
			weapon = weapon[0]

			# Get individual data by 'keys'
			wName = weapon['name']
			wRarity = weapon['rarity']
			wType = weapon['type']
			wDps = str(weapon['dps'])
			wDamage = str(weapon['damage'])
			wHeadShotDamage = str(weapon['headshotdamage'])
			wFireRate = str(weapon['firerate'])
			wMagSize = str(weapon['magsize'])
			wRange = str(weapon['range'])
			wDurability = str(weapon['durability'])
			wReloadTime = str(weapon['reloadtime'])
			wAmmoCost = str(weapon['ammocost'])
			wImpact = str(weapon['impact'])

			# Get the output ready to send
			wStat = "Name: " + wName + "\n" + "Rarity: " + wRarity + "\n" + "Type: " + wType + "\n" + "DPS: " + wDps + "\n" + "Damage: " + wDamage + "\n" + "Headshot Damage: " + wHeadShotDamage + "\n" + "Firerate: " + \
                            wFireRate + "\n" + "Magsize Size: " + wMagSize + "\n" + "Range: " + wRange + "\n" + "Durability: " + wDurability + \
                            "\n" + "Reload Time: " + wReloadTime + "\n" + "Ammocost: " + \
                            wAmmoCost + "\n" + "Impact: " + wImpact + "\n"
			wStat_embed = discord.Embed(
                                    title="Get weapon specifications",
                                    type="rich",
                                    description="Weapons Specs",
                                    colour=discord.Colour.blurple()
                                )
			wStat_embed.set_author(name=f"Fortnite: Battle Royale",
                        	icon_url="https://i.imgur.com/JijqpW9.jpg")
			wStat_embed.add_field(name=f"Showing specs of {weaponRarity} {weaponName}:",
                       		value=f"{wStat}\n\n", inline=False)
			await ctx.send(embed=wStat_embed)
		except IndexError:
			await ctx.send("Invalid input!! please check weapon name and rarity combination before you type again" + "\n" + "Use the " + "`.wlist`" + " command for the list of available in-game weapons.")
	else:
		await ctx.send("API service unavailable! Please try again later")

# Movie details
@bot.command()
async def mv(ctx,*, movieTitle):
	omdbURL = "http://www.omdbapi.com/?t=" + movieTitle + "&apikey=fe58df64"
	responseOMDB = req.get(omdbURL)
	if responseOMDB.status_code == 200:
		OMDBresult = json.loads(responseOMDB.content.decode("utf-8"))
		poster_img = OMDBresult["Poster"]
		responseMovieAvail = OMDBresult.get('Response')
		if responseMovieAvail == "True":
			movieList = ""
			for k, v in OMDBresult.items():
				if k == "Poster":
					pass
				else:
					movieList += f"**{k}**: {v}\n"
			mv_embed = discord.Embed(
                                    title="Get movie details",
                                    type="rich",
                                    description="Go get your popcorn....",
                                    colour=discord.Colour.magenta()
                                )
			mv_embed.set_image(url=f"{poster_img}")
			mv_embed.set_author(name=f"Fortknight bot movie manager",
                            icon_url="https://i.imgur.com/JijqpW9.jpg")
			mv_embed.add_field(name=f"Showing details for {movieTitle}:",
                       		value=f"{movieList}\n\n", inline=False)
			await ctx.send(embed=mv_embed)
		else:
			await ctx.send("Movie not found! ")
	else:
		await ctx.send("API service is down! Please try again later...")

# Help menu
@bot.command()
async def ask(ctx):
	with open("ask.json", 'r') as f:
		ask_content = json.load(f)
	ask_help = ""
	for k, v in ask_content.items():
		ask_help += f"**{k}**: {v}\n"
	ask_embed = discord.Embed(
		title="Help Menu: All usable commands are listed below more are upcoming",
		type="rich",
		description="Bot developer: AlphaSierra",
		colour=discord.Colour.gold()
	)
	ask_embed.set_author(name=f"Remember just '.ask' for help",
                      icon_url="https://i.imgur.com/JijqpW9.jpg")
	ask_embed.add_field(name="Commands:",
                     value=f"{ask_help}\n\n", inline=False)
	await ctx.send(embed=ask_embed)


bot.run(TOKEN)
