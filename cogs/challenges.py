import discord
from discord.ext import commands
import requests as req
import json


class ChallengesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Get the current week challenges
    @commands.command()
    async def ch(self, ctx):
        challenges_url = "https://fortnite-public-api.theapinetwork.com/prod09/challenges/get?season=current"
        challenges_data = req.post(challenges_url)
        challenges_json = json.loads(challenges_data.content.decode('utf-8'))
        challenges_desc_list = []
        challenges_total_list = []
        challenges_stars_list = []
        challenges_difficulty_list = []
        for challenges in challenges_json['challenges'][int(challenges_json['currentweek']) - 1]['entries']:
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


def setup(bot):
    bot.add_cog(ChallengesCog(bot))
