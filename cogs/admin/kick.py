# Cookies on the clouds ☁️💤
# ==========================
# kcik.py - {prefix}kick @mention <reason>

import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "kick", help = "Kick a member", brief = "Admin")
    @commands.has_permissions(kick_members = True)
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def kick(self, ctx, member, *, reason = None):
        if not ctx.message.mentions:
            await ctx.send("❌ You need to **mention** a member to kick.")
            return
        
        member = ctx.message.mentions[0]

        if member not in ctx.guild.members:
            await ctx.send("❌ The mentioned member is not in this server.")
            return

        if member is None:
            await ctx.send("❌ You need to **mention** a member to kick.")
            return
        
        if member.id == ctx.author.id:
            await ctx.send("❌ You cant kick yourself")
            return

        await member.kick(reason = reason)
        await ctx.send(f"{member.mention} has been kicked | Reason: **{reason or 'No reason provided'}**")

async def setup(bot: commands.Bot):
    await bot.add_cog(Kick(bot))