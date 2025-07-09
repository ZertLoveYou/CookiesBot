# Cookies on the clouds ☁️💤
# ==========================
# unban.py - {prefix}unban <userID>

import discord
from discord.ext import commands

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "unban", help = "Unban a member", brief = "Admin")
    @commands.has_permissions(ban_members = True)
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def unban(self, ctx: commands.Context, userID: int):
        user = await self.bot.fetch_user(userID)
        if user is None:
            await ctx.send("❌ Could not find user")
            return 

        try:
            await ctx.guild.unban(user)
            await ctx.send(f"✅ Successfully unbanned <@{userID}>")
        except discord.NotFound:
            await ctx.send("❌ User not found!")
        except discord.Forbidden:
            await ctx.send("❌ I have no permission bro..")
        except Exception as e:
            await ctx.send(f"⚠️ Error: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Unban(bot))