import discord
from discord.ext import commands
import platform
import psutil
from datetime import datetime
import random

# =========================================
# UTILITY COG
# =========================================

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =====================================
    # PING COMMAND
    # =====================================

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):

        latency = round(self.bot.latency * 1000)

        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Bot latency: `{latency}ms`",
            color=discord.Color.green()
        )

        embed.set_footer(
            text="Knowledge Bot Network Monitor"
        )

        await ctx.send(embed=embed)

    # =====================================
    # HELP COMMAND
    # =====================================

    @commands.command(name="help")
    async def help_command(self, ctx):

        embed = discord.Embed(
            title="📚 Knowledge Bot Help",
            description=(
                "Advanced AI + Cybersecurity + "
                "Programming Learning Ecosystem"
            ),
            color=discord.Color.blurple()
        )

        # =====================================
        # BASIC COMMANDS
        # =====================================

        embed.add_field(
            name="🛠 Basic Commands",
            value=(
                "`!ping`\n"
                "`!help`\n"
                "`!botinfo`\n"
                "`!motivation`\n"
                "`!alive`\n"
                "`!start`"
            ),
            inline=False
        )

        # =====================================
        # LEARNING COMMANDS
        # =====================================

        embed.add_field(
            name="🎓 Learning Commands",
            value=(
                "`!learn cybersecurity`\n"
                "`!roadmap ai_ml`\n"
                "`!resources programming`\n"
                "`!books psychology`\n"
                "`!channels ai_ml`\n"
                "`!specialize cybersecurity`\n"
                "`!projects programming`\n"
                "`!career ai_ml`\n"
                "`!quiz cybersecurity`\n"
                "`!recommend ai`\n"
                "`!dailyresource`"
            ),
            inline=False
        )

        # =====================================
        # AI COMMANDS
        # =====================================

        embed.add_field(
            name="🤖 AI Assistant Commands",
            value=(
                "`!explain api`\n"
                "`!ask what is docker`\n"
                "`!debug`\n"
                "`!interview`\n"
                "`!techstack`\n"
                "`!devops`"
            ),
            inline=False
        )

        # =====================================
        # NEWS COMMANDS
        # =====================================

        embed.add_field(
            name="📰 News & Trends",
            value=(
                "`!news cybersecurity`\n"
                "`!news ai`\n"
                "`!news programming`\n"
                "`!trending`\n"
                "`!startups`"
            ),
            inline=False
        )

        # =====================================
        # RESOURCE COMMANDS
        # =====================================

        embed.add_field(
            name="📚 Resource Commands",
            value=(
                "`!github cybersecurity`\n"
                "`!certifications ai_ml`\n"
                "`!labs`\n"
                "`!codingplatforms`\n"
                "`!websites cybersecurity`\n"
                "`!tools programming`"
            ),
            inline=False
        )

        # =====================================
        # TOPICS
        # =====================================

        embed.add_field(
            name="🧠 Available Topics",
            value=(
                "• cybersecurity\n"
                "• ai_ml\n"
                "• programming\n"
                "• psychology\n"
                "• startups\n"
                "• devops\n"
                "• cloud\n"
                "• competitive_programming"
            ),
            inline=False
        )

        embed.set_footer(
            text="Knowledge Bot • Production Edition"
        )

        await ctx.send(embed=embed)

    # =====================================
    # BOTINFO COMMAND
    # =====================================

    @commands.command()
    async def botinfo(self, ctx):

        uptime = datetime.utcnow() - self.bot.start_time

        embed = discord.Embed(
            title="🤖 Knowledge Bot",
            description=(
                "AI Learning + Cybersecurity + "
                "Developer Ecosystem"
            ),
            color=discord.Color.blue()
        )

        embed.add_field(
            name="🌐 Servers",
            value=str(len(self.bot.guilds)),
            inline=True
        )

        embed.add_field(
            name="👥 Users",
            value=str(len(self.bot.users)),
            inline=True
        )

        embed.add_field(
            name="⚡ Latency",
            value=f"{round(self.bot.latency * 1000)}ms",
            inline=True
        )

        embed.add_field(
            name="🖥 Python",
            value=platform.python_version(),
            inline=True
        )

        embed.add_field(
            name="📦 Discord.py",
            value=discord.__version__,
            inline=True
        )

        embed.add_field(
            name="💾 RAM Usage",
            value=f"{psutil.virtual_memory().percent}%",
            inline=True
        )

        embed.add_field(
            name="⏳ Uptime",
            value=str(uptime).split(".")[0],
            inline=False
        )

        embed.set_thumbnail(
            url=self.bot.user.avatar.url
            if self.bot.user.avatar
            else discord.Embed.Empty
        )

        embed.set_footer(
            text="Knowledge Bot System Monitor"
        )

        await ctx.send(embed=embed)

    # =====================================
    # MOTIVATION COMMAND
    # =====================================

    @commands.command()
    async def motivation(self, ctx):

        quotes = [

            "🚀 Consistency beats motivation.",

            "🔥 Discipline creates experts.",

            "💻 Build projects to learn faster.",

            "🧠 Learn deeply, not quickly.",

            "🎯 Focus on progress, not perfection.",

            "⚡ Small improvements daily become massive results.",

            "🌍 Skills create freedom.",

            "🛡️ Cybersecurity is one of the future-proof careers."
        ]

        quote = random.choice(quotes)

        embed = discord.Embed(
            title="⚡ Motivation",
            description=quote,
            color=discord.Color.orange()
        )

        embed.set_footer(
            text="Keep learning daily 🚀"
        )

        await ctx.send(embed=embed)

    # =====================================
    # SERVERINFO COMMAND
    # =====================================

    @commands.command()
    async def serverinfo(self, ctx):

        guild = ctx.guild

        embed = discord.Embed(
            title=f"🌐 {guild.name}",
            color=discord.Color.dark_blue()
        )

        embed.add_field(
            name="👥 Members",
            value=guild.member_count,
            inline=True
        )

        embed.add_field(
            name="📁 Channels",
            value=len(guild.channels),
            inline=True
        )

        embed.add_field(
            name="🎭 Roles",
            value=len(guild.roles),
            inline=True
        )

        embed.set_footer(
            text="Knowledge Bot Server Analytics"
        )

        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        await ctx.send(embed=embed)

# =========================================
# COG SETUP
# =========================================

async def setup(bot):
    await bot.add_cog(Utility(bot))
