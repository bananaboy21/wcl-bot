import discord
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix="+",owner_id=277981712989028353)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    

@bot.command()
async def help(ctx):
    em = discord.Embed(color=discord.Color(value=0x00ff00), title="WCL Bot Help")
    em.add_field(name="twitter", value="Gives WCL's twitter link.", inline=True)
    em.add_field(name="website", value="Gives WCL's website link.", inline=True)
    em.add_field(name="s1winner", value="Gives the winner for WCL season 1.", inline=True)
    em.add_field(name="rules", value="Gets the rules for WCL.", inline=True)
    em.add_field(name="s2forms", value="Gets the signup forms for WCL season 2.", inline=True)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/423921506737717248/423930582028779522/IMG-20171209-WA0004.jpg")
    await ctx.send(embed=em)
    

@bot.command()
async def twitter(ctx):
    """Gives WCL's twitter link."""
    await ctx.send("WCL Twitter: \nhttps://twitter.com/wcl_warriors")
    
    
@bot.command()
async def website(ctx):
    """Gives WCL's website link"""
    await ctx.send("WCL Website: \nhttps://warriorschampionshipleague.weebly.com/")
    
    
@bot.command()
async def s1winner(ctx):
    """Gives the winner for WCL season 1."""
    await ctx.send("`osfn` is the winnner of season 1!")
    
    
@bot.command()
async def rules(ctx):
    """Gets the rules for WCL."""
    await ctx.send("Read the rules carefully! \nhttps://docs.google.com/document/d/1yVdOugVGCxfuMGC3Fo2pGdqQqnXzHPMq7X1B12yYSFM/edit")
    
    
@bot.command()
async def s2forms(ctx):
    """Gets the signup forms for WCL season 2."""
    await ctx.send("**Forms**\n\nHeavy Weight:\nhttps://goo.gl/forms/pRSUXeH3lIadbDdY2\n\nLight Weight: https://goo.gl/forms/jsvy0gmWeAZdccK12")
    
    
bot.run(os.environ.get('TOKEN'))
    
