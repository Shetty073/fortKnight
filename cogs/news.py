import discord
from discord.ext import commands
import requests as req
import json


class NewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Get fortnite batle royale news
    @commands.command()
    async def news(self, ctx):
        news_url = "https://fortnite-public-api.theapinetwork.com/prod09/br_motd/get"
        news_data = req.post(
            news_url, data={'language': 'en'})
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


def setup(bot):
    bot.add_cog(NewsCog(bot))
