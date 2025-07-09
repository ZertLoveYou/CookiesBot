# Cookies on the clouds ☁️💤
# ==========================
# mute.py - {prefix}mute @mention <duration> <reason>

import discord
from discord.ext import commands
from datetime import timedelta

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "mute", help = "Mute (timeout) a member", brief = "Admin")
    @commands.has_permissions(moderate_members = True)
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def mute(self, ctx, member: discord.Member = None, time: int = 0, *, reason = None):
        if member is None or time <= 0:
            await ctx.send("❌ Usage: `!mute @user <seconds> [reason]`")
            return

        duration = timedelta(seconds = time)
        await member.timeout(duration, reason = reason)
        await ctx.send(f"{member.mention} has been muted for **{time} seconds** | Reason: **{reason or 'No reason'}**")

async def setup(bot):
    await bot.add_cog(Mute(bot))
