# Cookies on the clouds ☁️💤
# ==========================
# ping.py - {prefix}ping

import discord
import datetime
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "ping", help = "Check the bot's latency", brief = "Utilities")
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def ping(self, ctx):
        bot_latency: float = self.bot.latency
        embed = discord.Embed(
            color = 0x58acfc,
            timestamp = datetime.datetime.now(),
            title = f"{self.bot.user.name}'s ping latency:"
        )
        embed.add_field(
            name = "",
            value = f"{bot_latency * 1000:.2f} ms"
        )
        embed.set_footer(
            text = f"Requested by {ctx.author.display_name}",
            icon_url = ctx.author.display_avatar.url
        )
        embed.set_thumbnail(
            url = self.bot.user.display_avatar.url
        )
        await ctx.send(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))