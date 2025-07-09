# Cookies on the clouds ☁️💤
# ==========================
# avatar.py - no mention or {prefix}avatar @mention

import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "avatar", help = "Show Guild avatar and Global avatar of someone", brief = "Utilities")
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        # Avatar URLs
        global_avatar = member.avatar.url if member.avatar else None
        server_avatar = member.display_avatar.url if member.display_avatar else member.avatar.url

        # Create embed
        embed = discord.Embed(
            title = f"🧑 Avatar of {member.display_name}",
            color = 0x58acfc
        )

        if server_avatar:
            embed.set_thumbnail(url = server_avatar)
            embed.add_field(
                name = "🏠 Server Avatar",
                value = f"[Click here to download]({server_avatar})",
                inline = False
            )

        if global_avatar:
            embed.set_image(url = global_avatar)
            embed.add_field(
                name = "🌐 Global Avatar",
                value = f"[Click here to download]({server_avatar})",
                inline = False
            )
        else:
            embed.add_field(
                name = "🌐 Global Avatar",
                value = "This user has no global avatar!",
                inline = False
            )

        embed.set_footer(
            text = f"Requested by {ctx.author.display_name}",
            icon_url = ctx.author.display_avatar.url
        )

        await ctx.send(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Avatar(bot))