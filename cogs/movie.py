import discord
from discord.ext import commands
import requests as req
import json


class MovieCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Movie details
    @commands.command()
    async def mv(self, ctx, *, movietitle):
        omdburl = "http://www.omdbapi.com/?t=" + movietitle + "&apikey=fe58df64"
        responseomdb = req.get(omdburl)
        if responseomdb.status_code == 200:
            omdbresult = json.loads(responseomdb.content.decode("utf-8"))
            poster_img = omdbresult["Poster"]
            responsemovieavail = omdbresult.get('Response')
            if responsemovieavail == "True":
                movielist = ""
                for k, v in omdbresult.items():
                    if k == "Poster":
                        pass
                    else:
                        movielist += f"**{k}**: {v}\n"
                mv_embed = discord.Embed(
                    title="Get movie details",
                    type="rich",
                    description="Go get your popcorn....",
                    colour=discord.Colour.magenta()
                )
                mv_embed.set_image(url=f"{poster_img}")
                mv_embed.set_author(name=f"Fortknight bot movie manager",
                                    icon_url="https://i.imgur.com/JijqpW9.jpg")
                mv_embed.add_field(name=f"Showing details for {movietitle}:",
                                   value=f"{movielist}\n\n", inline=False)
                async with ctx.channel.typing():
                    await ctx.send(embed=mv_embed)
            else:
                async with ctx.channel.typing():
                    await ctx.send("Movie not found! ")
        else:
            async with ctx.channel.typing():
                await ctx.send("API service is down! Please try again later...")


def setup(bot):
    bot.add_cog(MovieCog(bot))
