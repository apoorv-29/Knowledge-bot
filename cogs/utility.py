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
                "Programming Learning Bot"
            ),
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="🛠 Basic Commands",
            value=(
                "`!ping`\n"
                "`!help`\n"
                "`!botinfo`\n"
                "`!motivation`"
            ),
            inline=False
        )

        embed.add_field(
            name="🎓 Learning Commands",
            value=(
                "`!learn cybersecurity`\n"
                "`!roadmap cybersecurity`\n"
                "`!resources cybersecurity`\n"
                "`!books cybersecurity`\n"
                "`!channels cybersecurity`\n"
                "`!specialize cybersecurity`"
            ),
            inline=False
        )

        embed.add_field(
            name="🚀 Advanced Commands",
            value=(
                "`!projects cybersecurity`\n"
                "`!career ai_ml`\n"
                "`!quiz cybersecurity`\n"
                "`!recommend ai`\n"
                "`!dailyresource`"
            ),
            inline=False
        )

        embed.set_footer(
            text="Knowledge Bot • Production Version"
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
                "Developer Assistant"
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

        embed.set_footer(
            text="Knowledge Bot"
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
            "🎯 Focus on progress, not perfection."
        ]

        quote = random.choice(quotes)

        embed = discord.Embed(
            title="⚡ Motivation",
            description=quote,
            color=discord.Color.orange()
        )

        await ctx.send(embed=embed)

# =========================================
# COG SETUP
# =========================================

async def setup(bot):
    await bot.add_cog(Utility(bot))
