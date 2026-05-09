import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load token
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

# Knowledge database
DATA = {
    "cybersecurity": {
        "explanation": "Cybersecurity protects systems, networks, and data from cyber attacks.",
        "videos": [
            "https://youtube.com/",
            "https://youtube.com/"
        ],
        "resources": [
            "https://owasp.org",
            "https://tryhackme.com"
        ],
        "roadmap": (
            "1. Learn Networking\n"
            "2. Learn Linux\n"
            "3. Learn Web Security\n"
            "4. Practice on TryHackMe"
        )
    },

    "ai_ml": {
        "explanation": "AI and ML help machines learn patterns and make decisions from data.",
        "videos": [
            "https://youtube.com/",
            "https://youtube.com/"
        ],
        "resources": [
            "https://kaggle.com",
            "https://scikit-learn.org"
        ],
        "roadmap": (
            "1. Learn Python\n"
            "2. Learn Math & Statistics\n"
            "3. Learn Machine Learning\n"
            "4. Learn Deep Learning"
        )
    }
}


# Bot ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! Bot is working.")


# Learn command
@bot.command()
async def learn(ctx, topic=None):

    if topic is None:
        await ctx.send(
            "❌ Usage: `!learn cybersecurity` or `!learn ai_ml`"
        )
        return

    topic = topic.lower()

    if topic not in DATA:
        await ctx.send("❌ Topic not found.")
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


# Roadmap command
@bot.command()
async def roadmap(ctx, topic=None):

    if topic is None:
        await ctx.send(
            "❌ Usage: `!roadmap cybersecurity`"
        )
        return

    topic = topic.lower()

    if topic not in DATA:
        await ctx.send("❌ Topic not found.")
        return

    embed = discord.Embed(
        title=f"🗺️ {topic.upper()} Roadmap",
        description=DATA[topic]["roadmap"],
        color=discord.Color.green()
    )

    await ctx.send(embed=embed)


# Resources command
@bot.command()
async def resources(ctx, topic=None):

    if topic is None:
        await ctx.send(
            "❌ Usage: `!resources cybersecurity`"
        )
        return

    topic = topic.lower()

    if topic not in DATA:
        await ctx.send("❌ Topic not found.")
        return

    links = "\n".join(DATA[topic]["resources"])

    await ctx.send(
        f"📚 Resources for **{topic.upper()}**\n{links}"
    )


# Error handling
@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Unknown command.")

    else:
        print(error)


# Run bot
bot.run(TOKEN)
