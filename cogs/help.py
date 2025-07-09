# Cookies on the clouds ☁️💤
# ==========================
# help.py - {prefix}help

import discord
from collections import defaultdict
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name = 'help', help = 'Show all commands', brief = "Utilities")
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def help(self, ctx):
        botname = getattr(self.bot, 'botname', 'Bot')
        prefix = self.bot.prefix

        embed = discord.Embed(
            title = f"{botname} commands list",
            description = f"*Current prefix:* `{prefix}`\nCommands according to categories:",
            color = 0x58acfc
        )

        categories = defaultdict(list)
        for cmd in self.bot.commands:
            if cmd.hidden:
                continue
            cat = getattr(cmd, 'brief', None) or 'Uncategorized'
            categories[cat].append(cmd)
    
        for cat, cmds in categories.items():
            value = "\n".join(f"`{prefix}{cmd}` - {cmd.help or 'No description frfr'}" for cmd in cmds)
            embed.add_field(
                name = f"📂 {cat}",
                value = value,
                inline = False
            )

        embed.set_footer(
            text = f"Requested by {ctx.author.display_name}",
            icon_url = ctx.author.display_avatar.url
        )
        embed.set_thumbnail(url = self.bot.user.display_avatar.url)

        await ctx.send(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))
