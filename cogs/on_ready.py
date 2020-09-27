from discord.ext import commands
import discord
#Good Morning, Yuzuki

class on_ready(commands.Cog):
    def __init__(self, client):
        self.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print(f'{commands.user.name} Is Awake')

            #commands.loop.create_task(change_status())

        # Uptime Clock
        async def change_status(self):
            # The "currently playing" message on Yuzuki
            await commands.change_presence(activity=discord.Game(f"This message is pissing me off"))

def setup(client):
    client.add_cog(on_ready(client))