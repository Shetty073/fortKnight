import discord
from discord.ext import commands
import requests as req
import json


class PlayerStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Get player data
    @commands.command()
    async def st(self, ctx, *, epic_name):  # *arg captures everything after other specified args as a list *, arg captures it, and converts it to one string
        try:
            st_url = "https://fortnite-public-api.theapinetwork.com/prod09/users/id"
            st_data = req.post(st_url, data={'username': epic_name})
            st_json = json.loads(st_data.content.decode("utf-8"))
        except Exception as e:
            async with ctx.channel.typing():
                await ctx.send(f"API error!! Error code: {e}")
            # Get stats
        try:
            s_url = "https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats"
            s_data = req.post(s_url, data={
                        'user_id': st_json["uid"], 'platform': 'pc', 'window': "alltime"})
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
        st_embed.add_field(name="Solo/Duo/Squad: ",
                            value=f"{s_json_stat_embed}\n\n", inline=False)
        st_embed.add_field(name="Total overall: ",
                            value=f"{s_json_totals_embed}", inline=False)
        async with ctx.channel.typing():
            await ctx.send(embed=st_embed)


def setup(bot):
    bot.add_cog(PlayerStats(bot))
