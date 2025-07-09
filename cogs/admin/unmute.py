# Cookies on the clouds ☁️💤
# ==========================
# unmute.py - {prefix}unmute @mention

import discord
from discord.ext import commands

class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "unmute", help = "Remove timed out for a member", brief = "Admin")
    @commands.has_permissions(moderate_members = True)
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def unmute(self, ctx: commands.Context, member: discord.Member = None):
        if member is None:
            await ctx.send(f"❌ You must mention a member who you want to remove timed out!")
            return

        try:
            await member.timeout(None)
            await ctx.send(f"✅ **{member.mention}** has been removed timeout! **Welcome back to the chat, fam!**")
        except discord.NotFound:
            await ctx.send(f"❌ User not found!")
        except discord.Forbidden:
            await ctx.send(f"❌ I have no permission bro..")
        except Exception as e:
            await ctx.send(f"⚠️ Error: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Unmute(bot))