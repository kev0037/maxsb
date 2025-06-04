from discord.ext import commands
from discord import File

bot = commands.Bot(command_prefix=".", self_bot=False)

@bot.event
async def on_ready():
    print(f"{bot.user} is now running and active.")

@bot.event
async def on_message(message):
    if message.author.name == "USERNAME":
        try:
            await message.add_reaction("💀")
        except Exception as e:
            print(f"Couldn't react: {e}")



bot.run("TOKEN")
