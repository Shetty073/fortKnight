import discord
import twitter
from discord.ext import commands
import requests as req
from random import choice
import json
import configparser


# Get the token from configuration file
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
	elif message == "good morning" or message == "gm":
		await ch.send(f"Good Morning {auth}")
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
	"Shifty Shafts", "Snobby Shores", "Tilted Towers", "Tomato Temple", "Wailing Woods"]
	place = choice(places)
	if place == "anywhere you want":
		async with ctx.channel.typing():
			await ctx.send(f"{ctx.author.name} go {place}..")
	else:
		async with ctx.channel.typing():
			await ctx.send(f"{ctx.author.name} go to {place}")

# .roll rolls a die
@bot.command()
async def roll(ctx):
	async with ctx.channel.typing():
		await ctx.send(f"{ctx.author.name} you have rolled a {choice(range(1, 7))}")

# .toss toss a coin
@bot.command()
async def toss(ctx):
	coin = choice(("Heads", "Tails"))
	async with ctx.channel.typing():
		await ctx.send(f"{ctx.author.name} it's {coin}")

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
	async with ctx.channel.typing():
		await ctx.send(embed=tweet_embed)

# Get player data
@bot.command()
async def st(ctx, *, epic_name):  # *arg captures everything after other specified args as a list *, arg captures it, and converts it to one string
	try:
		st_url = "https://fortnite-public-api.theapinetwork.com/prod09/users/id"
		st_headers = {'Authorization': API_KEY}
		st_data = req.post(st_url, data={'username': epic_name}, headers=st_headers)
		st_json = json.loads(st_data.content.decode("utf-8"))
	except Exception as e:
		async with ctx.channel.typing():
			await ctx.send(f"API error!! Error code: {e}")
		# Get stats
	try:
		s_url = "https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats"
		s_headers = {'Authorization': API_KEY}
		s_data = req.post(s_url, data={
                    'user_id': st_json["uid"], 'platform': 'pc', 'window': "alltime"}, headers=s_headers)
		s_json = json.loads(s_data.content.decode("utf-8"))
	except Exception as e:
		async with ctx.channel.typing():
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
	async with ctx.channel.typing():
		await ctx.send(embed=st_embed)

# Show in-game shop items
@bot.command()
async def shp(ctx):
	items_url = "https://fortnite-public-api.theapinetwork.com/prod09/store/get"
	items_headers = {'Authorization': API_KEY}
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
	shp_itm_dict = dict(zip(image_list, price_list))
	for k, v in shp_itm_dict.items():
		shp_embed = discord.Embed(
            title="Today's shop items",
            type="rich",
            description="Platform: PC",
            colour=discord.Colour.purple()
		)
		shp_embed.set_author(name="Fortnite: Battle Royale in-game shop item:",
						icon_url="https://i.imgur.com/JijqpW9.jpg")
		shp_embed.set_image(url=f"{k}")
		shp_embed.add_field(name="Price:", value=f"{v}", inline=False)
		async with ctx.channel.typing():
			await ctx.send(embed=shp_embed)

# Get list of upcoming shop items
@bot.command()
async def upshp(ctx):
	up_items_url = "https://fortnite-public-api.theapinetwork.com/prod09/upcoming/get"
	up_items_headers = {'Authorization': API_KEY}
	up_items_data = req.post(
		up_items_url, data={'language': 'en'}, headers=up_items_headers)
	up_items_json = json.loads(up_items_data.content.decode('utf-8'))
	up_items = up_items_json["items"]
	up_name_list = []
	up_image_list = []
	for up_item in up_items:
		up_name_list.append(up_item["name"])
		up_image_list.append(up_item["item"]["image"])
	up_shp_itm_dict = dict(zip(up_image_list, up_name_list))
	for k, v in up_shp_itm_dict.items():
		up_shp_embed = discord.Embed(
				title="Upcoming shop items",
				type="rich",
				description="Platform: PC",
				colour=discord.Colour.purple()
		)
		up_shp_embed.set_author(name="Fortnite: Battle Royale upcoming shop item:",
							icon_url="https://i.imgur.com/JijqpW9.jpg")
		up_shp_embed.add_field(name="Name:", value=f"{v}", inline=False)
		up_shp_embed.set_image(url=f"{k}")
		async with ctx.channel.typing():
			await ctx.send(embed=up_shp_embed)

# Get the current week challenges
@bot.command()
async def ch(ctx):
	challenges_url = "https://fortnite-public-api.theapinetwork.com/prod09/challenges/get"
	challenges_headers = {
		'Authorization': API_KEY, 'X-Fortnite-API-Version': 'v1.1'}
	challenges_data = req.post(
		challenges_url, data={'season': 'current', 'language': 'en'}, headers=challenges_headers)
	challenges_json = json.loads(challenges_data.content.decode('utf-8'))
	challenges_desc_list = []
	challenges_total_list = []
	challenges_stars_list = []
	challenges_difficulty_list = []
	for challenges in challenges_json['challenges'][int(challenges_json['currentweek'])-1]['entries']:
		challenges_desc_list.append(challenges['challenge'])
		challenges_total_list.append(challenges['total'])
		challenges_stars_list.append(challenges['stars'])
		challenges_difficulty_list.append(challenges['difficulty'])
	count = 0
	for desc in challenges_desc_list:
		challenges_embed = discord.Embed(
                            title="Fortnite: Batle Royale challenges",
                            type="rich",
                            description="Platform: PC",
                            colour=discord.Colour.purple()
                        )
		challenges_embed.add_field(name="Season: ", value=challenges_json['season'], inline=False)
		challenges_embed.add_field(name="Week: ", value=challenges_json['currentweek'], inline=False)
		challenges_embed.set_author(name="Latest Battle Royale challenges: ",
                               icon_url=challenges_json['star'])
		challenges_embed.add_field(name=f"Challenge {count + 1}: ", value=desc, inline=False)
		challenges_embed.add_field(
			name="Total: ", value=challenges_total_list[count], inline=True)
		challenges_embed.add_field(
			name="Stars: ", value=challenges_stars_list[count], inline=True)
		challenges_embed.add_field(
			name="Difficulty: ", value=challenges_difficulty_list[count], inline=True)
		count += 1
		async with ctx.channel.typing():
			await ctx.send(embed=challenges_embed)

# Top 10 players
@bot.command()
async def top(ctx):
	top_10_url = "https://fortnite-public-api.theapinetwork.com/prod09/leaderboards/get"
	top_10_headers = {
		'Authorization': API_KEY}
	top_10_data = req.post(
		top_10_url, data={'window': 'top_10_kills'}, headers=top_10_headers)
	top_10_json = json.loads(top_10_data.content.decode('utf-8'))
	for top in top_10_json['entries']:
		top_10_embed = discord.Embed(
				title="Top 10 Fortnite: Batle Royale players",
				type="rich",
				description="Platform: All platforms",
				colour=discord.Colour.purple()
		)
		top_10_embed.set_author(name="Top 10 Battle Royale players: ",
							icon_url="https://i.imgur.com/JijqpW9.jpg")
		top_10_embed.add_field(name=f"Rank {top['rank']}: ", value=top['username'], inline=False)
		top_10_embed.add_field(name="Wins: ", value=top['wins'], inline=True)
		top_10_embed.add_field(name="Kills: ", value=top['kills'], inline=True)
		top_10_embed.add_field(name="Matches: ", value=top['matches'], inline=True)
		top_10_embed.add_field(name="Minutes: ", value=top['minutes'], inline=True)
		top_10_embed.add_field(name="Score: ", value=top['score'], inline=True)
		top_10_embed.add_field(name="K/D: ", value=top['kd'], inline=True)
		top_10_embed.add_field(name="Platform: ", value=top['platform'], inline=False)
		async with ctx.channel.typing():
			await ctx.send(embed=top_10_embed)

# Get fortnite batle royale news
@bot.command()
async def news(ctx):
	news_url = "https://fortnite-public-api.theapinetwork.com/prod09/br_motd/get"
	news_headers = {'Authorization': API_KEY}
	news_data = req.post(
		news_url, data={'language': 'en'}, headers=news_headers)
	news_json = json.loads(news_data.content.decode('utf-8'))
	news_entries = news_json['entries']
	for entry in news_entries:
		news_title = entry['title']
		news_body = entry['body']
		news_image = entry['image']
		news_embed = discord.Embed(
			title="Fortnite: Batle Royale News",
			type="rich",
			description="Platform: PC",
			colour=discord.Colour.purple()
		)
		news_embed.set_author(name="Latest Battle Royale news: ",
						icon_url="https://i.imgur.com/JijqpW9.jpg")
		news_embed.set_image(url=news_image)
		news_embed.add_field(name=news_title, value=news_body, inline=False)
		async with ctx.channel.typing():
			await ctx.send(embed=news_embed)

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
	async with ctx.channel.typing():
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
			wStat = "**Name: **" + wName + "\n" + "**Rarity: **" + wRarity + "\n" + "**Type: **" + wType + "\n" + "**DPS: **" + wDps + "\n" + "**Damage: **" + wDamage + "\n" + "**Headshot Damage: **" + wHeadShotDamage + "\n" + "**Firerate: **" + \
                            wFireRate + "\n" + "**Magsize Size: **" + wMagSize + "\n" + "**Range: **" + wRange + "\n" + "**Durability: **" + wDurability + \
                            "\n" + "**Reload Time: **" + wReloadTime + "\n" + "**Ammocost: **" + \
                            wAmmoCost + "\n" + "**Impact: **" + wImpact + "\n"
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
			async with ctx.channel.typing():
				await ctx.send(embed=wStat_embed)
		except IndexError:
			async with ctx.channel.typing():
				await ctx.send("Invalid input!! please check weapon name and rarity combination before you type again" + "\n" + "Use the " + "`.wlist`" + " command for the list of available in-game weapons.")
	else:
		async with ctx.channel.typing():
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
			async with ctx.channel.typing():
				await ctx.send(embed=mv_embed)
		else:
			async with ctx.channel.typing():
				await ctx.send("Movie not found! ")
	else:
		async with ctx.channel.typing():
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
	async with ctx.channel.typing():
		await ctx.send(embed=ask_embed)


bot.run(TOKEN)
