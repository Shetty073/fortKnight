import discord
from discord.ext import commands
import requests as req
import json


# TODO: Response format is changed so this command needs work use statsexample.json file as reference for new response
class PlayerStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Get player data
    @commands.command()
    async def st(self, ctx, *,
                 epic_name):  # *arg captures everything after other specified args as a list *, arg captures it, and converts it to one string
        try:
            st_url = f"https://fortnite-public-api.theapinetwork.com/prod09/users/id?username={epic_name}"
            st_data = req.post(st_url)
            st_json = json.loads(st_data.content.decode("utf-8"))
        except Exception as e:
            async with ctx.channel.typing():
                await ctx.send(f"API error!! Error code: {str(e)}")
            # Get stats
        try:
            s_url = f"https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats_v2?user_id=" \
                f"{st_json['uid']}"
            s_data = req.post(s_url)
            s_json = json.loads(s_data.content.decode("utf-8"))
        except Exception as e:
            async with ctx.channel.typing():
                await ctx.send(f"API error!! Error code: {str(e)}")

        # Prepare the data for output
        devices = ""
        for d in s_json["devices"]:
            devices += d + " "

        squads = s_json["data"]["keyboardmouse"]["defaultsquad"]["default"]
        duos = s_json["data"]["keyboardmouse"]["defaultduo"]["default"]
        solos = s_json["data"]["keyboardmouse"]["defaultsolo"]["default"]

        s_json_squads = ""
        s_json_duos = ""
        s_json_solos = ""

        for k, v in squads.items():
            if not k == "lastmodified":
                s_json_squads += f"**{k}**: {v}\n"
        for k, v in duos.items():
            if not k == "lastmodified":
                s_json_duos = f"**{k}**: {v}\n"
        for k, v in solos.items():
            if not k == "lastmodified":
                s_json_solos += f"**{k}**: {v}\n"

        ovr_default = s_json["overallData"]["defaultModes"]
        ovr_ltm = s_json["overallData"]["ltmModes"]
        ovr_large_teams = s_json["overallData"]["largeTeamModes"]

        def_ovrall = "__**Squads/Duos/Solo**__: \n"
        ltm_ovrall = "__**LTM**__: \n"
        lg_team_ovrall = "__**Large Team modes**__: \n"

        for k, v in ovr_default.items():
            if not k == "includedPlaylists":
                def_ovrall += f"**{k}**: {v}\n"

        for k, v in ovr_ltm.items():
            if not k == "includedPlaylists":
                ltm_ovrall += f"**{k}**: {v}\n"

        for k, v in ovr_large_teams.items():
            if not k == "includedPlaylists":
                lg_team_ovrall += f"**{k}**: {v}\n"

        s_json_overall = def_ovrall + "\n" + ltm_ovrall + "\n" + lg_team_ovrall

        st_embed = discord.Embed(
            title="Player statistics",
            type="rich",
            description=f"Platform: {devices}",
            colour=discord.Colour.purple()
        )
        st_embed.set_author(name=f"Showing stats of **{s_json['epicName']}**",
                            icon_url="https://i.imgur.com/JijqpW9.jpg")
        st_embed.add_field(name="__Squads__: ",
                           value=f"{s_json_squads}\n\n", inline=False)
        st_embed.add_field(name="__Duos__: ",
                           value=f"{s_json_duos}\n\n", inline=False)
        st_embed.add_field(name="__Solo__: ",
                           value=f"{s_json_solos}\n\n\n", inline=False)
        st_embed.add_field(name="__Total overall__:",
                           value=f"{s_json_overall}", inline=False)
        async with ctx.channel.typing():
            await ctx.send(embed=st_embed)


def setup(bot):
    bot.add_cog(PlayerStats(bot))
