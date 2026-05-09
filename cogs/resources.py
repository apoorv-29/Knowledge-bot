import discord
from discord.ext import commands
import random

# =========================================
# RESOURCE DATABASE
# =========================================

RESOURCES = {

    # =====================================
    # CYBERSECURITY
    # =====================================

    "cybersecurity": {

        "resources": [
            "https://owasp.org",
            "https://tryhackme.com",
            "https://hackthebox.com",
            "https://portswigger.net/web-security",
            "https://picoctf.org"
        ],

        "books": [
            "The Web Application Hacker's Handbook",
            "Linux Basics for Hackers",
            "Hacking: The Art of Exploitation",
            "Practical Malware Analysis"
        ],

        "channels": [
            "LiveOverflow",
            "John Hammond",
            "NetworkChuck",
            "David Bombal",
            "The Cyber Mentor"
        ],

        "github": [
            "https://github.com/OWASP",
            "https://github.com/projectdiscovery",
            "https://github.com/rapid7/metasploit-framework",
            "https://github.com/swisskyrepo/PayloadsAllTheThings"
        ],

        "certifications": [
            "CompTIA Security+",
            "PNPT",
            "OSCP",
            "CEH"
        ]
    },

    # =====================================
    # AI / ML
    # =====================================

    "ai_ml": {

        "resources": [
            "https://kaggle.com",
            "https://huggingface.co",
            "https://pytorch.org",
            "https://scikit-learn.org",
            "https://fast.ai"
        ],

        "books": [
            "Hands-On Machine Learning",
            "Deep Learning with Python",
            "Pattern Recognition and Machine Learning"
        ],

        "channels": [
            "Andrew Ng",
            "DeepLearningAI",
            "Sentdex",
            "CodeEmporium",
            "Two Minute Papers"
        ],

        "github": [
            "https://github.com/huggingface/transformers",
            "https://github.com/langchain-ai/langchain",
            "https://github.com/pytorch/pytorch"
        ],

        "certifications": [
            "TensorFlow Developer",
            "Google ML Certification",
            "AWS ML Specialty"
        ]
    },

    # =====================================
    # PROGRAMMING
    # =====================================

    "programming": {

        "resources": [
            "https://developer.mozilla.org",
            "https://freecodecamp.org",
            "https://w3schools.com",
            "https://geeksforgeeks.org"
        ],

        "books": [
            "Clean Code",
            "The Pragmatic Programmer",
            "Design Patterns"
        ],

        "channels": [
            "Fireship",
            "freeCodeCamp",
            "CodeWithHarry",
            "Traversy Media",
            "Programming with Mosh"
        ],

        "github": [
            "https://github.com/public-apis/public-apis",
            "https://github.com/EbookFoundation/free-programming-books"
        ],

        "certifications": [
            "Meta Frontend",
            "Google IT Automation",
            "CS50"
        ]
    },

    # =====================================
    # COMPETITIVE PROGRAMMING
    # =====================================

    "competitive_programming": {

        "resources": [
            "https://codeforces.com",
            "https://leetcode.com",
            "https://atcoder.jp",
            "https://codechef.com"
        ],

        "books": [
            "Competitive Programming 4",
            "CP Handbook",
            "Introduction to Algorithms"
        ],

        "channels": [
            "Errichto",
            "William Lin",
            "Abdul Bari",
            "NeetCode"
        ],

        "github": [
            "https://github.com/cp-algorithms/cp-algorithms"
        ],

        "certifications": [
            "Google Kickstart",
            "ICPC Preparation"
        ]
    },

    # =====================================
    # PSYCHOLOGY
    # =====================================

    "psychology": {

        "resources": [
            "https://psychologytoday.com",
            "https://verywellmind.com",
            "https://simplypsychology.org"
        ],

        "books": [
            "Atomic Habits",
            "Deep Work",
            "Thinking Fast and Slow"
        ],

        "channels": [
            "HealthyGamerGG",
            "Huberman Lab",
            "The School of Life"
        ],

        "github": [
            "https://github.com/topics/psychology"
        ],

        "certifications": [
            "Positive Psychology",
            "Neuroscience Basics"
        ]
    }
}

# =========================================
# TOPIC ALIASES
# =========================================

ALIASES = {

    "hacking": "cybersecurity",
    "pentesting": "cybersecurity",
    "infosec": "cybersecurity",

    "ai": "ai_ml",
    "ml": "ai_ml",

    "coding": "programming",
    "development": "programming",

    "cp": "competitive_programming"
}

# =========================================
# HELPER
# =========================================

def resolve_topic(topic):

    topic = topic.lower()

    if topic in RESOURCES:
        return topic

    if topic in ALIASES:
        return ALIASES[topic]

    return None

# =========================================
# RESOURCES COG
# =========================================

class Resources(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =====================================
    # RESOURCES
    # =====================================

    @commands.command()
    async def resources(self, ctx, topic=None):

        if not topic:
            return await ctx.send(
                "❌ Usage: `!resources cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:
            return await ctx.send(
                "❌ Topic not found."
            )

        content = "\n".join(
            RESOURCES[topic]["resources"]
        )

        embed = discord.Embed(
            title=f"📚 Resources • {topic.upper()}",
            description=content,
            color=discord.Color.blue()
        )

        await ctx.send(embed=embed)

    # =====================================
    # BOOKS
    # =====================================

    @commands.command()
    async def books(self, ctx, topic=None):

        if not topic:
            return await ctx.send(
                "❌ Usage: `!books ai`"
            )

        topic = resolve_topic(topic)

        if not topic:
            return await ctx.send(
                "❌ Topic not found."
            )

        content = "\n".join(
            RESOURCES[topic]["books"]
        )

        embed = discord.Embed(
            title=f"📖 Books • {topic.upper()}",
            description=content,
            color=discord.Color.orange()
        )

        await ctx.send(embed=embed)

    # =====================================
    # CHANNELS
    # =====================================

    @commands.command()
    async def channels(self, ctx, topic=None):

        if not topic:
            return await ctx.send(
                "❌ Usage: `!channels cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:
            return await ctx.send(
                "❌ Topic not found."
            )

        content = "\n".join(
            RESOURCES[topic]["channels"]
        )

        embed = discord.Embed(
            title=f"📺 YouTube Channels • {topic.upper()}",
            description=content,
            color=discord.Color.red()
        )

        await ctx.send(embed=embed)

    # =====================================
    # GITHUB
    # =====================================

    @commands.command()
    async def github(self, ctx, topic=None):

        if not topic:
            return await ctx.send(
                "❌ Usage: `!github programming`"
            )

        topic = resolve_topic(topic)

        if not topic:
            return await ctx.send(
                "❌ Topic not found."
            )

        content = "\n".join(
            RESOURCES[topic]["github"]
        )

        embed = discord.Embed(
            title=f"💻 GitHub Resources • {topic.upper()}",
            description=content,
            color=discord.Color.dark_theme()
        )

        await ctx.send(embed=embed)

    # =====================================
    # CERTIFICATIONS
    # =====================================

    @commands.command()
    async def certifications(self, ctx, topic=None):

        if not topic:
            return await ctx.send(
                "❌ Usage: `!certifications cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:
            return await ctx.send(
                "❌ Topic not found."
            )

        content = "\n".join(
            RESOURCES[topic]["certifications"]
        )

        embed = discord.Embed(
            title=f"🎓 Certifications • {topic.upper()}",
            description=content,
            color=discord.Color.gold()
        )

        await ctx.send(embed=embed)

    # =====================================
    # RANDOM RESOURCE
    # =====================================

    @commands.command()
    async def randomresource(self, ctx):

        all_resources = []

        for category in RESOURCES.values():
            all_resources.extend(category["resources"])

        resource = random.choice(all_resources)

        embed = discord.Embed(
            title="🎲 Random Learning Resource",
            description=resource,
            color=discord.Color.random()
        )

        await ctx.send(embed=embed)

    # =====================================
    # CYBERSECURITY LABS
    # =====================================

    @commands.command()
    async def labs(self, ctx):

        embed = discord.Embed(
            title="🛡️ Cybersecurity Labs",
            description=(
                "🔹 https://tryhackme.com\n"
                "🔹 https://hackthebox.com\n"
                "🔹 https://portswigger.net/web-security\n"
                "🔹 https://picoctf.org\n"
                "🔹 https://overthewire.org"
            ),
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    # =====================================
    # CODING PLATFORMS
    # =====================================

    @commands.command()
    async def codingplatforms(self, ctx):

        embed = discord.Embed(
            title="💻 Coding Platforms",
            description=(
                "🔹 https://leetcode.com\n"
                "🔹 https://codeforces.com\n"
                "🔹 https://codechef.com\n"
                "🔹 https://hackerrank.com\n"
                "🔹 https://atcoder.jp"
            ),
            color=discord.Color.purple()
        )

        await ctx.send(embed=embed)

    # =====================================
    # NEWS
    # =====================================

    @commands.command()
    async def news(self, ctx):

        embed = discord.Embed(
            title="📰 Tech News Sources",
            description=(
                "🔹 https://thehackernews.com\n"
                "🔹 https://techcrunch.com\n"
                "🔹 https://arstechnica.com\n"
                "🔹 https://bleepingcomputer.com\n"
                "🔹 https://news.ycombinator.com"
            ),
            color=discord.Color.light_grey()
        )

        await ctx.send(embed=embed)

# =========================================
# COG SETUP
# =========================================

async def setup(bot):
    await bot.add_cog(Resources(bot))
