# Cookies on the clouds ☁️💤
# ==========================
# handler.py

import asyncio
import discord
import os
import time
from discord.ext import commands
from difflib import get_close_matches
from utils.logger import log_usage, log_error
from utils.blacklist import is_blacklisted

bot_logged = False

def register_event(bot: commands.Bot, botname, prefix):
    async def load_cogs_from_dict(bot, dict):
        for filename in os.listdir(dict):
            path = os.path.join(dict, filename)

            if os.path.isdir(path):
                await load_cogs_from_dict(bot, path)

            elif filename.endswith('.py') and filename != "__init__.py":
                module = os.path.splitext(os.path.relpath(path, "./"))[0].replace(os.sep, ".")
                await bot.load_extension(module)
                print(f'[✅] Loaded: {module}')

    @bot.event
    async def on_ready():
        global bot_logged
        bot_logged = True

        await load_cogs_from_dict(bot, './cogs')

        print(f'[🍪] {"Bot" if not botname else botname} loaded all the good stuff and currently online as: {bot.user} | Prefix: {prefix}')

    @bot.event
    async def on_message(message):
        if message.author.bot:
            return

        if is_blacklisted(message.author.id):
            await message.channel.send(f"⛔️ **{message.author.mention}**, you are **blacklisted** from using **{botname}**!")
            return

        prefix = bot.command_prefix
        if callable(prefix):
            prefix = await prefix(bot, message)

        if bot_logged:
            if message.guild:
                print(f'[💬 {message.guild.name}] {message.author.display_name} ({message.author.name}): {message.content}')
            else:
                print(f'[💬 DMs] {message.author.display_name} ({message.author.name}): {message.content}')

        if message.content.lower().startswith('wlc'):
            await message.channel.send(f"Hi! Welcome to our server **{message.guild.name}**!\nCheck out **our rules**, read **news** and **pick new roles**!\n*Thank you for joining, we hope you enjoy your stay~*")

        if message.content.lower().startswith('cookie'):
            await message.channel.send("# 🍪")

        if message.content.strip() == prefix:
            ctx = await bot.get_context(message)
            help_command = bot.get_command('help')

            if help_command:
                ctx.command = help_command
                await bot.invoke(ctx)

            return

        await bot.process_commands(message)

    @bot.event
    async def on_member_join(member):
        role = discord.utils.get(member.guild.roles, name = 'member')
        if role:
            await member.add_roles(role)
        count = member.guild.member_count
        embed = discord.Embed(
            color = 0x58acfc,
            title = 'A new member has arrived!! 🚀',
        )
        embed.add_field(
            name=f"Hey there 👋",
            value= (
                f'Hi, **{member.mention}**!\n'
                f'You\'re member **#{count}** of **{member.guild.name}** 🎉\n'
                f'📌 Don\'t forget to read the rules, check the announcements, and pick your roles!\n'
                f'Hope you enjoy your stay here 🤍\n'
                f'------'
            ),
            inline=False
        )
        embed.set_footer(text = f"Brought to you by {botname}💤")
        channel = discord.utils.get(member.guild.text_channels, name = 'general')
        if channel:
            await channel.send(embed=embed)

        try:
            await member.send('# Welcome to our Discord server!')
            print(f"[✅] Sent welcome DM to {member.name}")
        except:
            print(f"[⚠️] Could not DM {member.name}, maybe they have DMs disabled.")

    @bot.event
    async def on_guild_join(guild):
        bot_member = guild.me
        bot_role = bot_member.top_role

        roles = guild.roles[::-1]
        index = roles.index(bot_role)

        if index > 2:
            embed = discord.Embed(
                title = "⚠️ Role Hierachy Warning!",
                description = (
                    f"Hi, I am **{bot.user.name}** | *Thanks for inviting me to your server❤️*\n"
                    f"However, my role (**{bot_role.mention}**) is currently **too low** in the server role list.\n\n"
                    f"Please **drag my role above** the roles you want me to manage (e.g. `member`), "
                    f"otherwise I won't be able to ban/kick/mute members with higher roles.\n\n"
                    f"I suggest that you **move my role just below the owner role**, I need just enough perms."
                    f"🔧 How to fix: Go to **Server Settings → Roles → Drag `{bot_role.name}` up**."
                ),
                color = 0x58acfc
            )
            embed.set_footer(text = f"Sent automatically by {bot.user.name} ✨")

            try:
                channel = guild.system_channel or discord.utils.get(guild.text_channels, name = "general")
                if channel:
                    await channel.send(embed = embed)
                    print(f"[⚠️] Sent role hierarchy warning to {guild.name}")

            except Exception as e:
                print(f"[⚠️] Failed to send hierarchy warning in {guild.name}: {e}")
    
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("❌ You must provide a **user ID (number only)**, not a mention!")
            return

        if isinstance(error, commands.CommandNotFound):
            command = ctx.message.content.lstrip(ctx.prefix).split()[0]
            cmds = [cmd.name for cmd in bot.commands if not cmd.hidden]

            matches = get_close_matches(command, cmds, n = 1, cutoff = 0.5)

            if matches:
                suggestion = matches[0]
                await ctx.send(f"❌ Command: `{command}` **does not exist**! *Did you mean*: `{suggestion}`?")
            else:
                await ctx.send(f"❌ Command: `{command}` **does not exist**!")
        if isinstance(error, commands.CommandOnCooldown):
            retry_after = round(error.retry_after)
            current_ts = int(time.time())
            retry_ts = current_ts + retry_after

            embed = discord.Embed(
                description = f"⏱️ | **{ctx.author}**! You're a little bit *too quick*! Retry <t:{retry_ts}:R> 💤",
                color = 0x58acfc
            )

            msg = await ctx.send(embed = embed)

            await asyncio.sleep(error.retry_after)
            await msg.delete()

        else:
            log_error(error)
            raise error
        
    @bot.event
    async def on_command(ctx):
        log_usage(f"{ctx.author} used {ctx.command} in {ctx.guild.name if ctx.guild else 'DM'}")

