import discord
from discord.ext import commands
import requests as req
import json
import configparser

# Get the token from configuration file
config = configparser.ConfigParser()
config.read("config/config.ini")
API_KEY = config["FORTNITE"]["st_key"]


class UpShopCog:
    def __init__(self, bot):
        self.bot = bot

    # Get list of upcoming shop items
    @commands.command()
    async def upshp(self, ctx):
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


def setup(bot):
    bot.add_cog(UpShopCog(bot))
