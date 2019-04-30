import discord
from discord.ext import commands
import requests as req
import json


# Gets details of weapon by name and rarity
class WlistCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # Get list of all available weapons in-game
    async def wlist(self, ctx):
        weaponlist_url = "http://www.fortnitechests.info/api/weapons"
        header_weaponlist = {'accept': 'application/json'}
        response_3 = req.get(weaponlist_url, headers=header_weaponlist)
        weaponlist_acquired = json.loads(response_3.content.decode("utf-8"))

        # Get the list of all weapons by using the key 'name'
        w_list = [d['name'] for d in weaponlist_acquired if 'name' in d]
        # Using list(set()) get rid of duplicate entries in our list
        w_list = list(set(w_list))

        # Below code is written on purpose instead of using loops to prevent the bot from sending too many messages at once
        wp1 = w_list[0]
        wp2 = w_list[1]
        wp3 = w_list[2]
        wp4 = w_list[3]
        wp5 = w_list[4]
        wp6 = w_list[5]
        wp7 = w_list[6]
        wp8 = w_list[7]
        wp9 = w_list[8]
        wp10 = w_list[9]
        wp11 = w_list[10]
        wp12 = w_list[11]
        wp13 = w_list[12]
        wp14 = w_list[13]
        wp15 = w_list[14]
        wp16 = w_list[15]
        wp17 = w_list[16]
        wp18 = w_list[17]
        wp19 = w_list[18]
        wp20 = w_list[19]
        wp21 = w_list[20]
        wp22 = w_list[21]
        wp23 = w_list[22]
        wp24 = w_list[23]
        wp25 = w_list[24]

        # Ready for output
        w_list = wp1 + "\n" + wp2 + "\n" + wp3 + "\n" + wp4 + "\n" + wp5 + "\n" + wp6 + "\n" + wp7 + "\n" + wp8 + "\n" + wp9 + "\n" + wp10 + "\n" + wp11 + \
                "\n" + wp12 + "\n" + wp13 + "\n" + wp14 + "\n" + wp15 + "\n" + wp16 + "\n" + wp17 + "\n" + wp18 + \
                "\n" + wp19 + "\n" + wp20 + "\n" + wp21 + "\n" + \
                wp22 + "\n" + wp23 + "\n" + wp24 + "\n" + wp25 + "\n"
        wlist_embed = discord.Embed(
            title="Get the list of all available in-game weapons",
            type="rich",
            description="Weapons List",
            colour=discord.Colour.blurple()
        )
        wlist_embed.set_author(name=f"Fortnite: Battle Royale",
                               icon_url="https://i.imgur.com/JijqpW9.jpg")
        wlist_embed.add_field(name="List:",
                              value=f"{w_list}\n\n", inline=False)
        async with ctx.channel.typing():
            await ctx.send(embed=wlist_embed)


def setup(bot):
    bot.add_cog(WlistCog(bot))
