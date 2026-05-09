import discord
from discord.ext import commands
import random

# =========================================
# KNOWLEDGE DATABASE
# =========================================

DATA = {

    "cybersecurity": {

        "description": (
            "Cybersecurity protects systems, "
            "networks, and data from attacks."
        ),

        "roadmap": (
            "1. Learn Networking\n"
            "2. Learn Linux\n"
            "3. Learn Python\n"
            "4. Learn Web Security\n"
            "5. Practice on TryHackMe\n"
            "6. Learn Ethical Hacking"
        ),

        "specializations": [
            "Web Security",
            "Malware Analysis",
            "Cloud Security",
            "Reverse Engineering",
            "Red Teaming",
            "Blue Teaming"
        ],

        "projects": [
            "🔐 Password Strength Checker",
            "🌐 Port Scanner",
            "📡 Packet Sniffer",
            "🛡️ Vulnerability Scanner"
        ],

        "careers": [
            "SOC Analyst",
            "Penetration Tester",
            "Security Engineer",
            "Malware Analyst"
        ]
    },

    "ai_ml": {

        "description": (
            "AI and Machine Learning allow "
            "machines to learn from data."
        ),

        "roadmap": (
            "1. Learn Python\n"
            "2. Learn Math\n"
            "3. Learn Statistics\n"
            "4. Learn Machine Learning\n"
            "5. Learn Deep Learning\n"
            "6. Build AI Projects"
        ),

        "specializations": [
            "Deep Learning",
            "Computer Vision",
            "NLP",
            "LLMs",
            "Prompt Engineering"
        ],

        "projects": [
            "🤖 AI Chatbot",
            "📈 Stock Predictor",
            "🧠 Image Classifier",
            "🎵 Recommendation System"
        ],

        "careers": [
            "ML Engineer",
            "Data Scientist",
            "AI Researcher",
            "Prompt Engineer"
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
    "machinelearning": "ai_ml"
}

# =========================================
# HELPER
# =========================================

def resolve_topic(topic):

    topic = topic.lower()

    if topic in DATA:
        return topic

    if topic in ALIASES:
        return ALIASES[topic]

    return None

# =========================================
# LEARNING COG
# =========================================

class Learning(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =====================================
    # LEARN COMMAND
    # =====================================

    @commands.command()
    async def learn(self, ctx, topic=None):

        if not topic:

            return await ctx.send(
                "❌ Usage: `!learn cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:

            return await ctx.send(
                "❌ Topic not found."
            )

        embed = discord.Embed(
            title=f"📘 {topic.upper()}",
            description=DATA[topic]["description"],
            color=discord.Color.blue()
        )

        embed.set_footer(
            text="Knowledge Bot Learning System"
        )

        await ctx.send(embed=embed)

    # =====================================
    # ROADMAP COMMAND
    # =====================================

    @commands.command()
    async def roadmap(self, ctx, topic=None):

        if not topic:

            return await ctx.send(
                "❌ Usage: `!roadmap cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:

            return await ctx.send(
                "❌ Topic not found."
            )

        embed = discord.Embed(
            title=f"🗺️ {topic.upper()} Roadmap",
            description=DATA[topic]["roadmap"],
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    # =====================================
    # SPECIALIZE COMMAND
    # =====================================

    @commands.command()
    async def specialize(self, ctx, topic=None):

        if not topic:

            return await ctx.send(
                "❌ Usage: `!specialize cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:

            return await ctx.send(
                "❌ Topic not found."
            )

        specializations = "\n".join(
            DATA[topic]["specializations"]
        )

        embed = discord.Embed(
            title=f"🎯 {topic.upper()} Specializations",
            description=specializations,
            color=discord.Color.orange()
        )

        await ctx.send(embed=embed)

    # =====================================
    # PROJECTS COMMAND
    # =====================================

    @commands.command()
    async def projects(self, ctx, topic=None):

        if not topic:

            return await ctx.send(
                "❌ Usage: `!projects cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:

            return await ctx.send(
                "❌ Topic not found."
            )

        projects = "\n".join(
            DATA[topic]["projects"]
        )

        embed = discord.Embed(
            title=f"💻 {topic.upper()} Projects",
            description=projects,
            color=discord.Color.purple()
        )

        await ctx.send(embed=embed)

    # =====================================
    # CAREER COMMAND
    # =====================================

    @commands.command()
    async def career(self, ctx, topic=None):

        if not topic:

            return await ctx.send(
                "❌ Usage: `!career cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:

            return await ctx.send(
                "❌ Topic not found."
            )

        careers = "\n".join(
            DATA[topic]["careers"]
        )

        embed = discord.Embed(
            title=f"💼 Careers in {topic.upper()}",
            description=careers,
            color=discord.Color.gold()
        )

        await ctx.send(embed=embed)

    # =====================================
    # QUIZ COMMAND
    # =====================================

    @commands.command()
    async def quiz(self, ctx, topic=None):

        quizzes = {

            "cybersecurity": [
                (
                    "What does VPN stand for?",
                    "Virtual Private Network"
                ),

                (
                    "What does SQL stand for?",
                    "Structured Query Language"
                )
            ],

            "ai_ml": [
                (
                    "Most popular AI language?",
                    "Python"
                ),

                (
                    "What does ML stand for?",
                    "Machine Learning"
                )
            ]
        }

        if not topic:

            return await ctx.send(
                "❌ Usage: `!quiz cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:

            return await ctx.send(
                "❌ Topic not found."
            )

        question, answer = random.choice(
            quizzes[topic]
        )

        embed = discord.Embed(
            title=f"🧠 {topic.upper()} Quiz",
            description=question,
            color=discord.Color.red()
        )

        embed.set_footer(
            text=f"Answer: {answer}"
        )

        await ctx.send(embed=embed)

    # =====================================
    # RECOMMEND COMMAND
    # =====================================

    @commands.command()
    async def recommend(self, ctx, topic=None):

        recommendations = {

            "cybersecurity": (
                "✅ Learn Linux\n"
                "✅ Learn Networking\n"
                "✅ Learn Python\n"
                "✅ Practice Labs"
            ),

            "ai_ml": (
                "✅ Learn Python\n"
                "✅ Learn Statistics\n"
                "✅ Learn Deep Learning\n"
                "✅ Build Projects"
            )
        }

        if not topic:

            return await ctx.send(
                "❌ Usage: `!recommend cybersecurity`"
            )

        topic = resolve_topic(topic)

        if not topic:

            return await ctx.send(
                "❌ Topic not found."
            )

        embed = discord.Embed(
            title=f"🎯 Recommendations for {topic.upper()}",
            description=recommendations[topic],
            color=discord.Color.teal()
        )

        await ctx.send(embed=embed)

# =========================================
# COG SETUP
# =========================================

async def setup(bot):
    await bot.add_cog(Learning(bot))
