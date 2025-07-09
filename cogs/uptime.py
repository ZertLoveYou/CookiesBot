# Cookies on the clouds ☁️💤
# ==========================
# uptime.py - {prefix}uptime

import discord
import datetime
from discord.ext import commands

class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = "uptime", help = "See how long I've been floating in the clouds 💤", brief = "Utilities")
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def uptime(self, ctx):
        now = datetime.datetime.utcnow()
        delta = now - self.bot.start_time
        days, seconds = delta.days, delta.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        embed = discord.Embed(
            title = f"{self.bot.botname} uptime 🚀",
            description = f"I've been online for **{days}d {hours}h {minutes}m {seconds}s** 💤",
            color = 0x58acfc
        )
        embed.set_footer(
            text = f"Requested by {ctx.author.display_name}",
            icon_url = ctx.author.avatar.url
        )
        embed.set_thumbnail(
            url = self.bot.user.display_avatar.url
        )
        await ctx.send(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Uptime(bot))