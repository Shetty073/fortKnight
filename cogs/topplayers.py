import discord
from discord.ext import commands
import requests as req
import json
import configparser

# Get the token from configuration file
config = configparser.ConfigParser()
config.read("config/config.ini")
API_KEY = config["FORTNITE"]["st_key"]


class TopPlayersCog:
    def __init__(self, bot):
        self.bot = bot

    # Top 10 players
    @commands.command()
    async def top(self, ctx):
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


def setup(bot):
    bot.add_cog(TopPlayersCog(bot))
