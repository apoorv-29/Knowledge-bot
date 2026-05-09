import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("❌ TOKEN missing in .env file")

# =========================
# DISCORD INTENTS
# =========================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# =========================
# BOT SETUP
# =========================

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# =========================
# KNOWLEDGE DATABASE
# =========================

DATA = {
    "cybersecurity": {
        "explanation": (
            "Cybersecurity protects systems, networks, "
            "and data from cyber attacks."
        ),

        "videos": [
            "https://youtube.com/@LiveOverflow",
            "https://youtube.com/@JohnHammond010",
            "https://youtube.com/@NetworkChuck"
        ],

        "resources": [
            "https://owasp.org",
            "https://tryhackme.com",
            "https://hackthebox.com"
        ],

        "roadmap": (
            "1. Learn Networking\n"
            "2. Learn Linux\n"
            "3. Learn Web Security\n"
            "4. Practice on TryHackMe\n"
            "5. Learn Ethical Hacking"
        ),

        "books": [
            "The Web Application Hacker's Handbook",
            "Linux Basics for Hackers",
            "Hacking: The Art of Exploitation"
        ],

        "specializations": [
            "Web Security",
            "Malware Analysis",
            "Red Teaming",
            "Blue Teaming",
            "Cloud Security"
        ]
    },

    "ai_ml": {
        "explanation": (
            "AI and ML help machines learn patterns "
            "and make decisions from data."
        ),

        "videos": [
            "https://youtube.com/@Deeplearningai",
            "https://youtube.com/@sentdex",
            "https://youtube.com/@freecodecamp"
        ],

        "resources": [
            "https://kaggle.com",
            "https://scikit-learn.org",
            "https://pytorch.org"
        ],

        "roadmap": (
            "1. Learn Python\n"
            "2. Learn Math & Statistics\n"
            "3. Learn Machine Learning\n"
            "4. Learn Deep Learning\n"
            "5. Build Projects"
        ),

        "books": [
            "Hands-On Machine Learning",
            "Deep Learning with Python",
            "Pattern Recognition and Machine Learning"
        ],

        "specializations": [
            "Deep Learning",
            "Computer Vision",
            "NLP",
            "LLMs",
            "Prompt Engineering"
        ]
    }
}

# =========================
# EVENTS
# =========================

@bot.event
async def on_ready():
    print("=" * 50)
    print(f"✅ Logged in as {bot.user}")
    print("✅ Knowledge Bot is ONLINE")
    print("=" * 50)

# =========================
# PING COMMAND
# =========================

@bot.command()
async def ping(ctx):

    latency = round(bot.latency * 1000)

    await ctx.send(
        f"🏓 Pong! `{latency}ms`"
    )

# =========================
# HELP COMMAND
# =========================

@bot.command()
async def help(ctx):

    embed = discord.Embed(
        title="📚 Knowledge Bot Help",
        description=(
            "Advanced AI + Cybersecurity + Programming "
            "Learning Bot"
        ),
        color=discord.Color.purple()
    )

    embed.add_field(
        name="🛠️ Basic Commands",
        value=(
            "`!ping`\n"
            "`!help`\n"
        ),
        inline=False
    )

    embed.add_field(
        name="🎓 Learning Commands",
        value=(
            "`!learn cybersecurity`\n"
            "`!learn ai_ml`\n"
            "`!roadmap cybersecurity`\n"
            "`!resources cybersecurity`\n"
            "`!books cybersecurity`\n"
            "`!channels cybersecurity`\n"
            "`!specialize cybersecurity`\n"
        ),
        inline=False
    )

    embed.add_field(
        name="🧠 Available Topics",
        value=(
            "• cybersecurity\n"
            "• ai_ml"
        ),
        inline=False
    )

    embed.set_footer(
        text="Knowledge Bot • Version 1.0"
    )

    await ctx.send(embed=embed)

# =========================
# LEARN COMMAND
# =========================

@bot.command()
async def learn(ctx, topic=None):

    if topic is None:

        await ctx.send(
            "❌ Usage: `!learn cybersecurity`"
        )

        return

    topic = topic.lower()

    if topic not in DATA:

        await ctx.send(
            "❌ Topic not found."
        )

        return

    content = DATA[topic]

    embed = discord.Embed(
        title=f"📘 {topic.upper()}",
        description=content["explanation"],
        color=discord.Color.blue()
    )

    embed.add_field(
        name="📺 Videos",
        value="\n".join(content["videos"]),
        inline=False
    )

    embed.add_field(
        name="📚 Resources",
        value="\n".join(content["resources"]),
        inline=False
    )

    await ctx.send(embed=embed)

# =========================
# ROADMAP COMMAND
# =========================

@bot.command()
async def roadmap(ctx, topic=None):

    if topic is None:

        await ctx.send(
            "❌ Usage: `!roadmap cybersecurity`"
        )

        return

    topic = topic.lower()

    if topic not in DATA:

        await ctx.send(
            "❌ Topic not found."
        )

        return

    embed = discord.Embed(
        title=f"🗺️ {topic.upper()} Roadmap",
        description=DATA[topic]["roadmap"],
        color=discord.Color.green()
    )

    await ctx.send(embed=embed)

# =========================
# RESOURCES COMMAND
# =========================

@bot.command()
async def resources(ctx, topic=None):

    if topic is None:

        await ctx.send(
            "❌ Usage: `!resources cybersecurity`"
        )

        return

    topic = topic.lower()

    if topic not in DATA:

        await ctx.send(
            "❌ Topic not found."
        )

        return

    links = "\n".join(DATA[topic]["resources"])

    embed = discord.Embed(
        title=f"📚 Resources for {topic.upper()}",
        description=links,
        color=discord.Color.orange()
    )

    await ctx.send(embed=embed)

# =========================
# BOOKS COMMAND
# =========================

@bot.command()
async def books(ctx, topic=None):

    if topic is None:

        await ctx.send(
            "❌ Usage: `!books cybersecurity`"
        )

        return

    topic = topic.lower()

    if topic not in DATA:

        await ctx.send(
            "❌ Topic not found."
        )

        return

    books_list = "\n".join(DATA[topic]["books"])

    embed = discord.Embed(
        title=f"📖 Best Books for {topic.upper()}",
        description=books_list,
        color=discord.Color.gold()
    )

    await ctx.send(embed=embed)

# =========================
# CHANNELS COMMAND
# =========================

@bot.command()
async def channels(ctx, topic=None):

    if topic is None:

        await ctx.send(
            "❌ Usage: `!channels cybersecurity`"
        )

        return

    topic = topic.lower()

    if topic not in DATA:

        await ctx.send(
            "❌ Topic not found."
        )

        return

    channels_list = "\n".join(DATA[topic]["videos"])

    embed = discord.Embed(
        title=f"📺 Best Channels for {topic.upper()}",
        description=channels_list,
        color=discord.Color.red()
    )

    await ctx.send(embed=embed)

# =========================
# SPECIALIZE COMMAND
# =========================

@bot.command()
async def specialize(ctx, topic=None):

    if topic is None:

        await ctx.send(
            "❌ Usage: `!specialize cybersecurity`"
        )

        return

    topic = topic.lower()

    if topic not in DATA:

        await ctx.send(
            "❌ Topic not found."
        )

        return

    specializations = "\n".join(
        DATA[topic]["specializations"]
    )

    embed = discord.Embed(
        title=f"🎯 {topic.upper()} Specializations",
        description=specializations,
        color=discord.Color.teal()
    )

    await ctx.send(embed=embed)

# =========================
# MOTIVATION COMMAND
# =========================

@bot.command()
async def motivation(ctx):

    quotes = [
        "🚀 Consistency beats motivation.",
        "🧠 Learn deeply, not quickly.",
        "💻 Build projects to learn faster.",
        "🔥 Discipline creates experts.",
        "🎯 Focus on progress, not perfection."
    ]

    import random

    quote = random.choice(quotes)

    embed = discord.Embed(
        title="⚡ Motivation",
        description=quote,
        color=discord.Color.random()
    )

    await ctx.send(embed=embed)
# =========================
# TOPIC ALIASES
# =========================

ALIASES = {
    "hacking": "cybersecurity",
    "pentesting": "cybersecurity",
    "infosec": "cybersecurity",
    "machinelearning": "ai_ml",
    "ai": "ai_ml",
    "ml": "ai_ml"
}

# =========================
# HELPER FUNCTION
# =========================

def resolve_topic(topic):

    topic = topic.lower()

    if topic in DATA:
        return topic

    if topic in ALIASES:
        return ALIASES[topic]

    return None

# =========================
# PROJECTS COMMAND
# =========================

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def projects(ctx, topic=None):

    if topic is None:
        return await ctx.send(
            "❌ Usage: `!projects cybersecurity`"
        )

    topic = resolve_topic(topic)

    if not topic:
        return await ctx.send(
            "❌ Topic not found."
        )

    project_data = {
        "cybersecurity": [
            "🔐 Password Strength Checker",
            "🛡️ Port Scanner",
            "🌐 Vulnerability Scanner",
            "🕵️ Packet Sniffer",
            "📡 Network Monitor"
        ],

        "ai_ml": [
            "🤖 Chatbot",
            "📈 Stock Price Predictor",
            "🧠 Image Classifier",
            "🎵 Recommendation System",
            "🗣️ AI Voice Assistant"
        ]
    }

    projects_list = "\n".join(
        project_data[topic]
    )

    embed = discord.Embed(
        title=f"💻 {topic.upper()} Projects",
        description=projects_list,
        color=discord.Color.dark_blue()
    )

    embed.set_footer(
        text="Build projects to improve faster."
    )

    await ctx.send(embed=embed)

# =========================
# CAREER COMMAND
# =========================

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def career(ctx, topic=None):

    if topic is None:
        return await ctx.send(
            "❌ Usage: `!career cybersecurity`"
        )

    topic = resolve_topic(topic)

    if not topic:
        return await ctx.send(
            "❌ Topic not found."
        )

    careers = {
        "cybersecurity": (
            "🛡️ SOC Analyst\n"
            "🔐 Penetration Tester\n"
            "☁️ Cloud Security Engineer\n"
            "🕵️ Malware Analyst\n"
            "🚨 Incident Responder"
        ),

        "ai_ml": (
            "🤖 ML Engineer\n"
            "🧠 AI Researcher\n"
            "📊 Data Scientist\n"
            "⚡ Prompt Engineer\n"
            "🖥️ Computer Vision Engineer"
        )
    }

    embed = discord.Embed(
        title=f"💼 Careers in {topic.upper()}",
        description=careers[topic],
        color=discord.Color.dark_green()
    )

    await ctx.send(embed=embed)

# =========================
# QUIZ COMMAND
# =========================

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def quiz(ctx, topic=None):

    if topic is None:
        return await ctx.send(
            "❌ Usage: `!quiz cybersecurity`"
        )

    topic = resolve_topic(topic)

    if not topic:
        return await ctx.send(
            "❌ Topic not found."
        )

    quizzes = {
        "cybersecurity": {
            "question": (
                "What does VPN stand for?"
            ),

            "answer": (
                "Virtual Private Network"
            )
        },

        "ai_ml": {
            "question": (
                "What language is most used in AI?"
            ),

            "answer": (
                "Python"
            )
        }
    }

    q = quizzes[topic]

    embed = discord.Embed(
        title=f"🧠 {topic.upper()} Quiz",
        description=q["question"],
        color=discord.Color.blurple()
    )

    embed.set_footer(
        text=f"Answer: {q['answer']}"
    )

    await ctx.send(embed=embed)

# =========================
# DAILY RESOURCE
# =========================

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def dailyresource(ctx):

    resources = [
        "🔗 https://roadmap.sh",
        "🔗 https://tryhackme.com",
        "🔗 https://freecodecamp.org",
        "🔗 https://kaggle.com",
        "🔗 https://owasp.org"
    ]

    import random

    resource = random.choice(resources)

    embed = discord.Embed(
        title="📚 Daily Learning Resource",
        description=resource,
        color=discord.Color.orange()
    )

    await ctx.send(embed=embed)

# =========================
# SMART RECOMMENDATION
# =========================

@bot.command()
async def recommend(ctx, topic=None):

    if topic is None:
        return await ctx.send(
            "❌ Usage: `!recommend ai_ml`"
        )

    topic = resolve_topic(topic)

    if not topic:
        return await ctx.send(
            "❌ Topic not found."
        )

    recommendations = {
        "cybersecurity": (
            "✅ Learn Linux\n"
            "✅ Learn Networking\n"
            "✅ Learn Python\n"
            "✅ Practice on TryHackMe"
        ),

        "ai_ml": (
            "✅ Learn Python\n"
            "✅ Learn Statistics\n"
            "✅ Learn Linear Algebra\n"
            "✅ Build ML Projects"
        )
    }

    embed = discord.Embed(
        title=f"🎯 Recommendations for {topic.upper()}",
        description=recommendations[topic],
        color=discord.Color.brand_green()
    )

    await ctx.send(embed=embed)    

# =========================
# ERROR HANDLING
# =========================

@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.CommandNotFound):

        await ctx.send(
            "❌ Unknown command. Use `!help`"
        )

    elif isinstance(
        error,
        commands.MissingRequiredArgument
    ):

        await ctx.send(
            "❌ Missing required arguments."
        )

    else:
        print(f"ERROR: {error}")

        await ctx.send(
            "⚠️ An unexpected error occurred."
        )

# =========================
# RUN BOT
# =========================

try:
    bot.run(TOKEN)

except discord.LoginFailure:
    print("❌ Invalid Discord Token")

except Exception as e:
    print(f"❌ Fatal Error: {e}")
