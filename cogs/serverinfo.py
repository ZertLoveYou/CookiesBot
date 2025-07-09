# Cookies on the clouds ☁️💤
# ==========================
# serverinfo.py - {prefix}serverinfo

import discord
import datetime
from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="serverinfo", help="Show server's informations", brief="Utilities")
    @commands.cooldown(5, 10, commands.BucketType.user)
    async def serverinfo(self, ctx: commands.Context):
        try:
            guild = ctx.guild
            if not guild:
                await ctx.send('❌ This command can only be used in a server!')
                return

            # Thử debug để biết đang chạy được đến đâu
            print(f"[DEBUG] serverinfo called in guild: {guild.name}")

            members = len([m for m in guild.members if not m.bot])
            bots = len([b for b in guild.members if b.bot])
            text_channels = len(guild.text_channels)
            voice_channels = len(guild.voice_channels)
            created_at = guild.created_at.strftime('%b %d %Y')

            embed = discord.Embed(
                title="Server's information",
                color=0x58acfc,
                timestamp=datetime.datetime.now()
            )

            if guild.icon:
                embed.set_thumbnail(url=guild.icon.url)

            embed.add_field(name="ℹ️  Server name", value=f"`{guild.name}`", inline=True)
            embed.add_field(name="🆔 Server ID", value=f"`{guild.id}`", inline=True)
            embed.add_field(name="👑 Owner", value=f"{guild.owner.mention}", inline=True)
            embed.add_field(name="📅 Created At", value=f"`{created_at}`", inline=True)
            embed.add_field(name="👥 Members", value=f"{members} humans 🙋‍♂️\n{bots} bots 🤖", inline=True)
            embed.add_field(name="💬 Channels", value=f"📝 {text_channels} text\n🔊 {voice_channels} voice", inline=True)
            embed.add_field(name="🎭 Roles", value=f"`{len(guild.roles)}` roles", inline=True)

            if guild.vanity_url_code:
                embed.add_field(
                    name="🌐 Vanity URL",
                    value=f"https://discord.gg/{guild.vanity_url_code}",
                    inline=False
                )

            embed.add_field(
                name="🔐 Verification Level",
                value=f"`{guild.verification_level.name.capitalize()}`",
                inline=True
            )

            embed.set_footer(
                text=f"Requested by {ctx.author.display_name}",
                icon_url=ctx.author.display_avatar.url
            )

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"⚠️ Có lỗi khi xử lý command:\n`{type(e).__name__}: {e}`")
            print("[ERROR] serverinfo:", type(e).__name__, e)

    
async def setup(bot: commands.Bot):
    await bot.add_cog(ServerInfo(bot))