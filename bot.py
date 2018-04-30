import discord
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix="+",owner_id=277981712989028353)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(activity=discord.Game(name="+help for help!"))
    

@bot.command()
async def help(ctx):
    em = discord.Embed(color=discord.Color(value=0x00ff00), title="WCL Bot Help")
    em.add_field(name="twitter", value="Gives WCL's twitter link.", inline=False)
    em.add_field(name="website", value="Gives WCL's website link.", inline=False)
    em.add_field(name="s1winner", value="Gives the winner for WCL season 1.", inline=False)
    em.add_field(name="rules", value="Gets the rules for WCL.", inline=False)
    em.add_field(name="s2forms", value="Gets the signup forms for WCL season 2.", inline=False)
    em.add_field(name="delete [number of msgs]", value="Deletes a number of messages.", inline=False)
    em.add_field(name="role [user] [role name]", value="Gives a user a certain role.", inline=False)
    em.add_field(name='visitors [user]', value='Gives visitor role to user.', inline=False)
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


@bot.command()
@commands.has_permissions(manage_messages = True)
async def delete(ctx, msgs: int):
    if msgs is None:
        return await ctx.send("Please enter the number of messages you want to delete!")
    try:
        await ctx.channel.purge(limit=msgs+1)
        await ctx.send(f"Successfully deleted {msgs+1} messages. :white_check_mark:", delete_after=3)
    except discord.Forbidden:
        await ctx.send("Bot does not have Manage Messages permission.")


@bot.command()
@commands.has_permissions(manage_roles = True)
async def role(ctx, user: discord.Member, role):
    if role is None:
        return await ctx.send("Please enter the role you want to give!")
    try:
        r = discord.utils.get(ctx.guild.roles, name=role)
        if r is None:
            return await ctx.send("No roles found with that given name. Names must be case-sensitive.")
        await user.add_roles(r)
        await ctx.send(f"Successfully gave **{str(user)}** the **{r.name}** role.")
    except discord.Forbidden:
        await ctx.send("Bot does not have Manage Roles permission.")
        
@bot.command(aliases=['visitor'])
@commands.has_permissions(manage_roles = True)
async def visitors(ctx, user: discord.Member):
    if ctx.guild.id != 389162246627917826:
        return
    r = discord.utils.get(ctx.guild.roles, name='visitors')
    await user.add_roles(r)
    await ctx.send(f"Successfully added **visitors** role to **{str(user)}**")
    
bot.run(os.environ.get('TOKEN'))
    
