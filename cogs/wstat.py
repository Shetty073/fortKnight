import discord
from discord.ext import commands
import requests as req
import json


# Gets details of weapon by name and rarity
class WstatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wstat(self, ctx, weaponrarity, *, weaponname):
        # API call and raw response
        weapons_stats = "http://www.fortnitechests.info/api/weapons"
        header_for_wstats = {'accept': 'application/json'}
        response_4 = req.get(weapons_stats, headers=header_for_wstats)

        if response_4.status_code == 200:
            wstats_acquired = json.loads(response_4.content.decode("utf-8"))
            try:
                    # Processing response for individual data
                weaponname = weaponname.title()
                weaponrarity = weaponrarity.lower()
                weapon = list(filter(
                    lambda weapon: weapon['name'] == f'{weaponname}' and weapon['rarity'] == f'{weaponrarity}', wstats_acquired))
                weapon = weapon[0]

                # Get individual data by 'keys'
                wName = weapon['name']
                wRarity = weapon['rarity']
                wType = weapon['type']
                wDps = str(weapon['dps'])
                wDamage = str(weapon['damage'])
                wHeadShotDamage = str(weapon['headshotdamage'])
                wFireRate = str(weapon['firerate'])
                wMagSize = str(weapon['magsize'])
                wRange = str(weapon['range'])
                wDurability = str(weapon['durability'])
                wReloadTime = str(weapon['reloadtime'])
                wAmmoCost = str(weapon['ammocost'])
                wImpact = str(weapon['impact'])

                # Get the output ready to send
                wStat = "**Name: **" + wName + "\n" + "**Rarity: **" + wRarity + "\n" + "**Type: **" + wType + "\n" + "**DPS: **" + wDps + "\n" + "**Damage: **" + wDamage + "\n" + "**Headshot Damage: **" + wHeadShotDamage + "\n" + "**Firerate: **" + \
                                wFireRate + "\n" + "**Magsize Size: **" + wMagSize + "\n" + "**Range: **" + wRange + "\n" + "**Durability: **" + wDurability + \
                                "\n" + "**Reload Time: **" + wReloadTime + "\n" + "**Ammocost: **" + \
                                wAmmoCost + "\n" + "**Impact: **" + wImpact + "\n"
                wStat_embed = discord.Embed(
                                        title="Get weapon specifications",
                                        type="rich",
                                        description="Weapons Specs",
                                        colour=discord.Colour.blurple()
                                    )
                wStat_embed.set_author(name=f"Fortnite: Battle Royale",
                                icon_url="https://i.imgur.com/JijqpW9.jpg")
                wStat_embed.add_field(name=f"Showing specs of {weaponrarity} {weaponname}:",
                                value=f"{wStat}\n\n", inline=False)
                async with ctx.channel.typing():
                    await ctx.send(embed=wStat_embed)
            except IndexError:
                async with ctx.channel.typing():
                    await ctx.send("Invalid input!! please check weapon name and rarity combination before you type again" + "\n" + "Use the " + "`.wlist`" + " command for the list of available in-game weapons.")
        else:
            async with ctx.channel.typing():
                await ctx.send("API service unavailable! Please try again later")


def setup(bot):
    bot.add_cog(WstatCog(bot))
