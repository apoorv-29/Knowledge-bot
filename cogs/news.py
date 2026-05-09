import discord
from discord.ext import commands
import random

# =========================================
# TECH NEWS DATABASE
# =========================================

NEWS = {

    "cybersecurity": [

        "🛡️ New zero-day vulnerabilities discovered in enterprise software.",

        "🔐 Ransomware attacks are increasing globally.",

        "🌐 Cloud security is becoming one of the highest paying fields.",

        "⚠️ AI-powered phishing attacks are rising rapidly."
    ],

    "ai": [

        "🤖 Open-source LLMs are evolving rapidly.",

        "🧠 AI agents are becoming the next big trend.",

        "🚀 Multimodal AI models are transforming automation.",

        "💡 Companies are integrating AI into every workflow."
    ],

    "programming": [

        "💻 Python remains one of the most demanded languages.",

        "⚡ Rust adoption is increasing among developers.",

        "🌐 WebAssembly is gaining popularity.",

        "🚀 Full-stack AI engineering is growing rapidly."
    ],

    "startups": [

        "📈 AI startups are receiving massive investments.",

        "🚀 SaaS products continue dominating tech markets.",

        "💡 Indie hacking and solo startups are growing fast.",

        "🌍 Remote-first startups are becoming common."
    ]
}

# =========================================
# NEWS COG
# =========================================

class News(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =====================================
    # NEWS COMMAND
    # =====================================

    @commands.command()
    async def news(self, ctx, topic=None):

        if not topic:

            topics = ", ".join(NEWS.keys())

            return await ctx.send(
                f"❌ Usage: `!news <topic>`\n"
                f"Available: {topics}"
            )

        topic = topic.lower()

        if topic not in NEWS:

            return await ctx.send(
                "❌ News topic not found."
            )

        article = random.choice(NEWS[topic])

        embed = discord.Embed(
            title=f"📰 Latest {topic.upper()} News",
            description=article,
            color=discord.Color.gold()
        )

        embed.set_footer(
            text="Knowledge Bot News Engine"
        )

        await ctx.send(embed=embed)

    # =====================================
    # TRENDING COMMAND
    # =====================================

    @commands.command()
    async def trending(self, ctx):

        trends = [

            "🔥 AI Agents",
            "🔥 Cybersecurity Automation",
            "🔥 LLM Engineering",
            "🔥 DevOps + AI",
            "🔥 Cloud Security",
            "🔥 System Design",
            "🔥 Prompt Engineering",
            "🔥 Autonomous AI Systems"
        ]

        embed = discord.Embed(
            title="📈 Trending Technologies",
            description="\n".join(trends),
            color=discord.Color.red()
        )

        await ctx.send(embed=embed)

    # =====================================
    # STARTUPS COMMAND
    # =====================================

    @commands.command()
    async def startups(self, ctx):

        startups = [

            "🚀 OpenAI",
            "🚀 Anthropic",
            "🚀 Perplexity",
            "🚀 Midjourney",
            "🚀 HuggingFace",
            "🚀 Cursor AI",
            "🚀 Replit"
        ]

        embed = discord.Embed(
            title="💡 Top AI Startups",
            description="\n".join(startups),
            color=discord.Color.blue()
        )

        await ctx.send(embed=embed)

# =========================================
# COG SETUP
# =========================================

async def setup(bot):
    await bot.add_cog(News(bot))
