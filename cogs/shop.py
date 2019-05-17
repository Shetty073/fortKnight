import discord
from discord.ext import commands
import requests as req
import json


class ShopCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Show in-game shop items
    @commands.command()
    async def shp(self, ctx):
        items_url = "https://fortnite-public-api.theapinetwork.com/prod09/store/get"
        items_data = req.post(items_url, data={'language': 'en'})
        items_json = json.loads(items_data.content.decode('utf-8'))
        items = items_json["items"]
        name_list = []
        price_list = []
        image_list = []
        type_list = []
        rarity_list = []
        for item in items:
            name_list.append(item["name"])
            price_list.append(item["cost"])
            image_list.append(item["item"]["image"])
            type_list.append(item["item"]["type"])
            rarity_list.append(item["item"]["rarity"])
        shp_itm_dict = dict(zip(image_list, price_list))
        for k, v in shp_itm_dict.items():
            shp_embed = discord.Embed(
                title="Today's shop items",
                type="rich",
                description="Platform: PC",
                colour=discord.Colour.purple()
            )
            shp_embed.set_author(name="Fortnite: Battle Royale in-game shop item:",
                                 icon_url="https://i.imgur.com/JijqpW9.jpg")
            shp_embed.set_image(url=f"{k}")
            shp_embed.add_field(name="Price:", value=f"{v}", inline=False)
            async with ctx.channel.typing():
                await ctx.send(embed=shp_embed)


def setup(bot):
    bot.add_cog(ShopCog(bot))
