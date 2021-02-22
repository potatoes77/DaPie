# bot.py
import discord
token = "Nzk5Njg0OTQ2Nzg3Njk2NjUw.YAHKpA.zYhrfjvPLBnRwedMSeJ8Ad8RrFI"
my_guild = "SirPythonTestsAlot"
client = discord.Client()

intents = discord.Intents.default()
intents.members = True
Client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

    print(
    f"{client.user} has connected to the following guild:\n"
    f"{guild.name}(id: {guild.id})"
    )

    print(guild.members[0])
    members = '\n - '.join([member.name for member in guild.members])
    print(f"Guild Member:\n - {members}")

client.run(token)
