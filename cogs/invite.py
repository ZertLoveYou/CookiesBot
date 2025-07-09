# Cookies on the clouds ☁️💤
# ==========================
# invite.py - {prefix}invite

import discord
from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.invite.help = f"Invite link of {self.bot.botname}"

    @commands.command(name = "invite", brief = "Utilities")
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def invite(self, ctx):
        inv = f'https://discord.com/oauth2/authorize?client_id={self.bot.client_id}&permissions=8&scope=bot+applications.commands'
        embed = discord.Embed(
            title = f"{self.bot.botname}'s invite link",
            description = f"[Click here to invite me!]({inv})",
            color = 0x58acfc
        )
        embed.set_footer(
            text = f"Requested by {ctx.author.display_name}",
            icon_url = ctx.author.display_avatar.url
        )
        embed.set_thumbnail(
            url = self.bot.user.display_avatar.url
        )
        await ctx.send(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Invite(bot))