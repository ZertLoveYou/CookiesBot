# Cookies on the clouds ☁️💤
# ==========================
# blacklist.py - {prefix}blacklist add/remove @mention/userID

import discord
from discord.ext import commands
from utils.blacklist import is_blacklisted, add_to_blacklist, remove_from_blacklist

class BlackList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name = "blacklist", invoke_without_command = True, help = "Manage blacklist users", brief = "Admin")
    @commands.has_permissions(administrator = True)
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def blacklist(self, ctx):
        await ctx.send("❌ Usage: `!blacklist add/remove @user|userID`")

    @blacklist.command(name = "add", help = "Add user to blacklist")
    async def add(self, ctx, user: str = None):
        if not user:
            await ctx.send("❌ Usage: `!blacklist add/remove @user|userID`")
            return
        
        try:
            if ctx.message.mentions:
                target = ctx.message.mentions[0]
                user_id = target.id
            else:
                user_id = int(user)
                target = await self.bot.fetch_user(user_id)
        except:
            await ctx.send("❌ Invalid user or ID")
            return
        if is_blacklisted(user_id):
            await ctx.send(f"⛔️ {target.mention} is **already** blacklisted")
            return
        
        add_to_blacklist(user_id)
        await ctx.send(f"✅ Blacklisted {target.mention} ({user_id}) successfully")
    
    @blacklist.command(name = "remove", help = "Remove user from blacklist")
    async def remove(self, ctx, user: str = None):
        if not user:
            await ctx.send("❌ Usage: `!blacklist add/remove @user|userID`")
            return

        try:
            if ctx.message.mentions:
                target = ctx.message.mentions[0]
                user_id = target.id
            else:
                user_id = int(user)
                target = await self.bot.fetch_user(user_id)
        except:
            await ctx.send("❌ Invalid user or ID")
            return
        if not is_blacklisted(user_id):
            await ctx.send(f"⚠️ {target.mention} is **not** blacklisted")
            return

        remove_from_blacklist(user_id)
        await ctx.send(f"✅ Removed blacklist {target.mention} ({user_id}) successfully")

async def setup(bot: commands.Bot):
    await bot.add_cog(BlackList(bot))