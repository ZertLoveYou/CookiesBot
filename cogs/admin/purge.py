# Cookies on the clouds ☁️💤
# ==========================
# purge.py - {prefix}purge <number>

import discord
from discord.ext import commands

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "purge", help = "Delete recent messages", brief = "Admin")
    @commands.has_permissions(manage_messages = True)
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def purge(self, ctx, amount: int = -1):
        if amount <= 0:
            await ctx.send("❌ Enter a number greater than 0.")
            return
        await ctx.channel.purge(limit = amount + 1)
        confirm = await ctx.send(f"🧹 Deleted **{amount}** messages.")
        await confirm.delete(delay = 3)

async def setup(bot):
    await bot.add_cog(Purge(bot))
