from discord.ext import commands
from random import choice


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # .roll rolls a die
    @commands.command()
    async def roll(self, ctx):
        async with ctx.channel.typing():
            await ctx.send(f"{ctx.author.name} you have rolled a {choice(range(1, 7))}")

    # .toss toss a coin
    @commands.command()
    async def toss(self, ctx):
        coin = choice(("Heads", "Tails"))
        async with ctx.channel.typing():
            await ctx.send(f"{ctx.author.name} it's {coin}")


def setup(bot):
    bot.add_cog(Fun(bot))
