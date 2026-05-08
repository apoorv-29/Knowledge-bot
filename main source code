import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# =========================
# LOAD ENV VARIABLES
# =========================
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# PUT YOUR SERVER ID HERE
# Enable Developer Mode in Discord
# Right click server -> Copy Server ID
GUILD_ID =123456789012345678


# =========================
# BOT SETUP
# =========================
class KnowledgeBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)

        # Copy global commands to guild
        self.tree.copy_global_to(guild=guild)

        # Sync instantly to your server
        await self.tree.sync(guild=guild)

        print("✅ Slash commands synced instantly!")


bot = KnowledgeBot()


# =========================
# DATABASE
# =========================
DATA = {
    "cybersecurity": {
        "explanation": (
            "Cybersecurity is the protection of systems, "
            "networks, and data from cyber attacks and hackers."
        ),
        "videos": [
            "• Cybersecurity for Beginners",
            "• How Ethical Hacking Works"
        ],
        "resources": [
            "• https://owasp.org",
            "• https://tryhackme.com"
        ],
        "roadmap": (
            "1. Learn Networking\n"
            "2. Learn Linux\n"
            "3. Learn Web Security\n"
            "4. Practice on TryHackMe\n"
            "5. Learn Ethical Hacking"
        )
    },

    "ai_ml": {
        "explanation": (
            "Artificial Intelligence helps machines simulate "
            "human intelligence. Machine Learning allows systems "
            "to learn from data."
        ),
        "videos": [
            "• AI For Everyone",
            "• Neural Networks Explained"
        ],
        "resources": [
            "• https://scikit-learn.org",
            "• https://kaggle.com"
        ],
        "roadmap": (
            "1. Learn Python\n"
            "2. Learn Math Basics\n"
            "3. Learn Machine Learning\n"
            "4. Build Projects\n"
            "5. Learn Deep Learning"
        )
    }
}


# =========================
# HELPER FUNCTION
# =========================
def get_contextual_topic(interaction: discord.Interaction):
    channel_name = interaction.channel.name.lower()

    user_roles = [
        role.name.lower()
        for role in interaction.user.roles
    ]

    if "cyber" in channel_name or "cybersecurity" in user_roles:
        return "cybersecurity"

    if (
        "ai" in channel_name
        or "ml" in channel_name
        or "ai_ml" in user_roles
    ):
        return "ai_ml"

    return None


# =========================
# COMMANDS
# =========================

# ---------- PING ----------
@bot.tree.command(
    name="ping",
    description="Check if bot is online"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong! Bot is working.")


# ---------- LEARN ----------
@bot.tree.command(
    name="learn",
    description="Learn about a topic"
)
@app_commands.describe(
    topic="Example: cybersecurity or ai_ml"
)
async def learn(
    interaction: discord.Interaction,
    topic: str = None
):
    selected_topic = (
        topic.lower()
        if topic
        else get_contextual_topic(interaction)
    )

    if not selected_topic or selected_topic not in DATA:
        return await interaction.response.send_message(
            "❌ Topic not found.\n"
            "Try:\n"
            "/learn cybersecurity\n"
            "/learn ai_ml",
            ephemeral=True
        )

    content = DATA[selected_topic]

    embed = discord.Embed(
        title=f"🎓 {selected_topic.upper()}",
        description=content["explanation"],
        color=discord.Color.green()
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

    await interaction.response.send_message(embed=embed)


# ---------- ROADMAP ----------
@bot.tree.command(
    name="roadmap",
    description="Get learning roadmap"
)
async def roadmap(interaction: discord.Interaction):
    topic = get_contextual_topic(interaction)

    if not topic:
        return await interaction.response.send_message(
            "❌ Use this inside AI or Cyber channel.",
            ephemeral=True
        )

    embed = discord.Embed(
        title=f"🗺️ {topic.upper()} Roadmap",
        description=DATA[topic]["roadmap"],
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=embed)


# ---------- RESOURCES ----------
@bot.tree.command(
    name="resources",
    description="Get useful resources"
)
async def resources(interaction: discord.Interaction):
    topic = get_contextual_topic(interaction)

    if not topic:
        return await interaction.response.send_message(
            "❌ Use this in AI or Cyber channels.",
            ephemeral=True
        )

    links = "\n".join(DATA[topic]["resources"])

    await interaction.response.send_message(
        f"📚 Resources for {topic.upper()}:\n{links}"
    )


# =========================
# READY EVENT
# =========================
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


# =========================
# RUN BOT
# =========================
bot.run(TOKEN)
