import discord
import os

from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"bot on como {bot.user} fr")

# -------- lol --------

@bot.tree.command(name="calls", description="Escolher uma call e entrar nela")
async def calls(interaction: discord.Interaction):
    guild = interaction.guild
    voice_channels = guild.voice_channels

    if not voice_channels:
        await interaction.response.send_message(
            "ngl ts servidor não tem call",
            ephemeral=True
        )
        return

    msg = "escolhe a call twin:\n\n"
    for i, channel in enumerate(voice_channels, start=1):
        msg += f"{i}️⃣ {channel.name}\n"

    await interaction.response.send_message(msg + "\nresponde com o número", ephemeral=True)

    def check(m):
        return (
            m.author == interaction.user
            and m.channel == interaction.channel
            and m.content.isdigit()
        )

    try:
        reply = await bot.wait_for("message", check=check, timeout=30)
        choice = int(reply.content) - 1

        if choice < 0 or choice >= len(voice_channels):
            await interaction.followup.send("escolha inválida twin", ephemeral=True)
            return

        channel = voice_channels[choice]

        if interaction.guild.voice_client is None:
            await channel.connect()
            await interaction.followup.send(
                f"entrei na call **{channel.name}** e vou stay fr",
                ephemeral=True
            )
        else:
            await interaction.followup.send(
                "já tô em call twin, chill",
                ephemeral=True
            )

    except TimeoutError:
        await interaction.followup.send("demorou demais twin", ephemeral=True)

# -------- RUN --------

bot.run(os.environ["TOKEN"])

