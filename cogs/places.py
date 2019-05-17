from discord.ext import commands
from random import choice


class PlacesCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# .ft command gives the name of a fortnite location
	@commands.command()
	async def ft(self, ctx):
		places = ["Haunted Hills", "Junk Junction", "Loot Lake", "Pleasant Park",
				  "Snobby Shores", "Neo Tilted", "Happy Hamlet", "Polar Peak",
				  "Frosty Flights", "Lucky Landing", "Shifty Shafts", "Fatal Fields",
				  "Paradise Palms", "Mega Mall", "Salty Springs", "Dusty Divot",
				  "Lazy Lagoon", "Lonely Lodge", "The Block", "Lava Tomato Temple",
				  "Sunny Steps", "anywhere you want", "the three ski lodges", 
				  "Old Factories", "Viking Village", "Hero House", "Villain House",
				  "Football Stadium", "Mexico"]
		place = choice(places)
		if place == "anywhere you want":
			async with ctx.channel.typing():
				await ctx.send(f"{ctx.author.name} go {place}..")
		else:
			async with ctx.channel.typing():
				await ctx.send(f"{ctx.author.name} go to {place}")


def setup(bot):
	bot.add_cog(PlacesCog(bot))
