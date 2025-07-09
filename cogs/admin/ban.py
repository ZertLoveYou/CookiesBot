# Cookies on the clouds ☁️💤
# ==========================
# ban.py - {prefix}ban @mention <reason>

import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban", help="Ban a member by mention or ID", brief="Admin")
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def ban(self, ctx, user: str = None, *, reason=None):
        if user is None:
            await ctx.send("❌ You need to provide a user mention or ID.")
            return

        if ctx.message.mentions:
            target = ctx.message.mentions[0]
        else:
            try:
                user_id = int(user)
                target = discord.Object(id=user_id)
            except ValueError:
                await ctx.send("❌ Invalid user ID.")
                return

        try:
            await ctx.guild.ban(target, reason=reason)
            await ctx.send(f"✅ User **{user}** has been **banned**!\n📄 Reason: **{reason or 'No reason provided'}**")
        except discord.Forbidden:
            await ctx.send("❌ I have no permission bro..")
        except discord.HTTPException as e:
            await ctx.send(f"⚠️ Failed to ban user: `{e}`")

async def setup(bot):
    await bot.add_cog(Ban(bot))
