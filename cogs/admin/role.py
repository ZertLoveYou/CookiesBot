# Cookies on the clouds ☁️💤
# ==========================
# role.py - {prefix}role add/remove @mention <closed result with your role>

import discord
from discord.ext import commands
from difflib import get_close_matches

class RoleManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name = "role", invoke_without_command = True, help = "Manage roles with add/remove subcommands", brief = "Admin")
    @commands.has_permissions(manage_roles = True)
    async def role(self, ctx):
        await ctx.send("❌ Usage: `!role add/remove @member <role name>`")

    @role.command(name = 'add', help = 'Add a role to a member')
    async def add(self, ctx, member: discord.Member = None, *, rolename: str = None):
        await self._handle_role(ctx, member, rolename, add = True)

    @role.command(name = 'remove', help = 'Remove a role from a member')
    async def remove(self, ctx, member: discord.Member = None, *, rolename: str = None):
        await self._handle_role(ctx, member, rolename, add = False)

    async def _handle_role(self, ctx, member, rolename, add = True):
        if not member or not rolename:
            await ctx.send("❌ Usage: `!role add/remove @member <role name>`")
            return

        roles = [r for r in ctx.guild.roles if r.name != "@everyone"]
        role_names = [r.name for r in roles]
        matches = get_close_matches(rolename, role_names, n = 1, cutoff = 0.4)

        if not matches:
            await ctx.send("❌ Role not found")
            return
        
        role = discord.utils.get(ctx.guild.roles, name = matches[0])
        if not role:
            await ctx.send("❌ Could not solve role")
            return
        
        try:
            if add:
                await member.add_roles(role)
                await ctx.send(f"✅ Added role **{role.name}** to {member.mention}")

            else:
                await member.remove_roles(role)
                await ctx.send(f"✅ Removed role **{role.name}** from {member.mention}")
            
        except discord.Forbidden:
            await ctx.send(f"❌ I have no permission bro..")
        
        except Exception as e:
            await ctx.send(f"⚠️ Error: {e}")
        

async def setup(bot: commands.Bot):
    await bot.add_cog(RoleManager(bot))