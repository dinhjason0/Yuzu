import discord
from discord.ext import commands
import json

class start(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='start')
    async def start(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='Player')
        if role not in ctx.author.roles:
            await ctx.author.send("Thank you for participating. Enjoy yourself.")
            #consider asking the player for a custom name
            await ctx.send(
                f"Link connection has been established. Say hello to your new room {ctx.author.display_name}")
            await ctx.author.add_roles(role)
            self.pendstats(ctx.author.id, ctx.author.display_name)

        elif role in ctx.author.roles:
            await ctx.author.send("You're already a player!")
        pass

    def pendstats(self, id, display_name):
        with open('.\cogs\players..json') as f:
            data = json.load(f)
            data["Database"]["Player"][str(id)] = {
                "Name":display_name,
                "HP": 10,
                "STR": 1,
                "DEX": 1,
                "SPD": 1,
                "MPE": 1,
                "HIT": 5,
                "Inventory": [
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None
                ],
                "Favorites": []
            }
        with open('.\cogs\players..json', 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def setup(client):
    client.add_cog(start(client))