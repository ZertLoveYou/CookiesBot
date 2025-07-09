# Cookies on the clouds ☁️💤
# ==========================
# userinfo.py - no mention or {prefix}userinfo @mention

import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'userinfo', help = 'Show user\'s informations', brief = "Utilities")
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def user(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        roles = [
            role for role in member.roles if role.name != "@everyone"
        ]
        roles_mention = [role.mention for role in roles]
        embed = discord.Embed(
            title = f"{member.name}'s information",
            color = 0x58acfc
        )
        embed.add_field(
            name = "Display name",
            value = f"`{member.display_name}`"
        )
        embed.add_field(
            name = "Created at",
            value = f"`{member.created_at.strftime('%b %d %Y')}`"
        )
        embed.add_field(
            name = "Joined at",
            value = f"`{member.joined_at.strftime('%b %d %Y')}`"
        )
        embed.add_field(
            name = "Roles",
            value = ", ".join(roles_mention) if roles_mention else "`This user has no role 💤`"
        )
        embed.set_thumbnail(url = member.avatar.url)
        embed.set_footer(
            text = f"Requested by `{ctx.author.display_name}`",
            icon_url = ctx.author.display_avatar.url
        )
        await ctx.send(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(UserInfo(bot))
