import discord
from discord.ext import commands
import json
import configparser
import logging

# Setting up logging
logger = logging.getLogger('discord')
# level argument specifies what level of events to log out and can any of CRITICAL, ERROR, WARNING, INFO,
# and DEBUG and if not specified defaults to WARNING
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Get the token from configuration file
config = configparser.ConfigParser()
config.read("config/config.ini")
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
async def on_message(self, msg):
    message = msg.content.lower()
    auth = msg.author.name
    ch = msg.channel
    if message == "good night" or message == "gn":
        await ch.send(f"Good Night {auth}")
    elif message == "good morning" or message == "gm":
        await ch.send(f"Good Morning {auth}")
    await bot.process_commands(msg)


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


# Cogs list
extensions = ["cogs.wstat",
			  "cogs.wlist",
			  "cogs.movie",
			  "cogs.news",
			  "cogs.playerstats",
			  "cogs.tweet",
			  "cogs.topplayers",
			  "cogs.challenges",
			  "cogs.shop",
			  "cogs.upshop",
			  "cogs.fun",
			  "cogs.places"]


# Load all cogs
if __name__ == "__main__":
	for extension in extensions:
		try:
			bot.load_extension(extension)
			print(f"{extension} loaded..")
		except Exception as error:
			print(f"{extension} cannot be loaded. [{error}]")

bot.run(TOKEN)
