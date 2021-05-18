import discord
from discord.ext import commands

class PingCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        # await ctx.send(f'Pong! {client.latency}ms')
        await ctx.send('Pong!')
        
def setup(client):
    client.add_cog(PingCog(client))