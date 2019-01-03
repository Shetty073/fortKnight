import discord
from discord.ext import commands
import twitter
import configparser

# Get the token from configuration file
config = configparser.ConfigParser()
config.read("config/config.ini")
CONSUMER_KEY = config["TWITTER"]["consumer_key"]
CONSUMER_SECRET = config["TWITTER"]["consumer_secret"]
ACCESS_TOKEN_KEY = config["TWITTER"]["access_token_key"]
ACCESS_TOKEN_SECRET = config["TWITTER"]["access_token_secret"]


class TweetCog:
    def __init__(self, bot):
        self.bot = bot

    # .tweet gets the latest tweet by Fortnite
    @commands.command()
    async def tweet(self, ctx):
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


def setup(bot):
    bot.add_cog(TweetCog(bot))
