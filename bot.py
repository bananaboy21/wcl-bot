import discord
import os
import textwrap
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
    em.add_field(name="links", value="All useful WCL links!", inline=False)
    em.add_field(name="s1winner", value="Gives the winner for WCL season 1.", inline=False)
    em.add_field(name="rules", value="Gets the rules for WCL.", inline=False)
    em.add_field(name="s2forms", value="Gets the signup forms for WCL season 2.", inline=False)
    em.add_field(name="delete [number of msgs]", value="Deletes a number of messages.", inline=False)
    em.add_field(name="role [user] [role name]", value="Gives a user a certain role.", inline=False)
    em.add_field(name='visitors [user]', value='Gives visitor role to user.', inline=False)
    em.add_field(name='s2info <type>', value='Gives information on WCL season 2!', inline=False)
    em.add_field(name='schedule', value='Gives a schedule on WCL season 2 events.', inline=False)
    em.add_field(name='hw', value='Get information on WCL\'s Heavy Weight League.', inline=False)
    em.add_field(name='invite', value='Gets the invite link for WCL server.', inline=False)
    em.add_field(name='wm', value='Gets war match info.', inline=False)
    em.add_field(name='pointtable', value='Gets the point table for S2 light weight.', inline=False)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/423921506737717248/423930582028779522/IMG-20171209-WA0004.jpg")
    await ctx.send(embed=em)

    
@bot.command()
async def invite(ctx):
    await ctx.send("https://discord.gg/WfNATEn")

@bot.command()
async def links(ctx):
    await ctx.send(textwrap.dedent("""
    :globe_with_meridians: __**WCL Links**__ :globe_with_meridians: 
   **Twitter**: https://twitter.com/wcl_warriors
   **Facebook**: https://www.facebook.com/Warriors-Championship-League-WCL-2002735889992134/
   **Instagram**: https://www.instagram.com/warriors_championship_league/
   **Website**: https://warriorschampionshipleague.weebly.com/
   """))
    
    
@bot.command()
async def clans(ctx):
    em = discord.Embed(color=discord.Color(value=0x00ff00), title="WCL Clans: S2 Heavy Weight")
    em.set_image(url="https://media.discordapp.net/attachments/389365839465545742/458490064817881098/all_together_Heavy.png?width=1442&height=503")
    await ctx.send(embed=em)
    

@bot.command()
async def pointtable(ctx):
    em = discord.Embed(color=discord.Color(value=0x00ff00), title="WCl S2: Light Weight - Point Table")
    em.set_image(url="https://cdn.discordapp.com/attachments/443879822318370816/461258900558315540/point_table.png")
    await ctx.send(embed=em)
    
    
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
    
    
@bot.command(aliases=['seasoninfo', 'info'])
async def s2info(ctx, Type=None):
    if not Type:
        image_link = "https://media.discordapp.net/attachments/389441146100776970/446772216219172877/all_together.png?width=1442&height=503"
    elif Type.lower() == 'armored':
        image_link = "https://cdn.discordapp.com/attachments/389441146100776970/446772185063751682/Armored_Clans.png"
    elif Type.lower() == 'airborne':
        image_link = "https://media.discordapp.net/attachments/389441146100776970/446772212272332812/Airborne_Clans.png?width=488&height=676"
    elif Type.lower() == 'infantry':
        image_link = "https://media.discordapp.net/attachments/389441146100776970/444239349073051648/Infantry_Clans.png?width=488&height=676"
    else:
        return await ctx.send("Unknown name. Either leave blank or choose from **armored**, **airborne**, or **infantry**.")
    em = discord.Embed(color=discord.Color(value=0x00ff00), title="WCL Season 2 Information")
    em.set_image(url=image_link)
    await ctx.send(embed=em)
    
    
@bot.command()
async def schedule(ctx, Type=None):
    if not Type:
        return await ctx.send("Which schedule? Heavy/light.")
    em = discord.Embed(color=discord.Color(value=0x00ff00), title="WCL Season 2 Schedule")
    if Type.lower() == "light":
        em.set_image(url="https://media.discordapp.net/attachments/389441146100776970/446772242634899456/schedual.png?width=1442&height=601")
    elif Type.lower() == "heavy":
        em.set_image(url="https://media.discordapp.net/attachments/389441146100776970/464528605393715200/Sch_heavy.png?width=1442&height=601")
    await ctx.send(embed=em)
    
    
@bot.command(aliases=['hw'])
async def heavyweight(ctx):
    em = discord.Embed(color=discord.Color(value=0x00ff00), title="WCL Heavy Weight Info")
    em.set_image(url="https://media.discordapp.net/attachments/389441146100776970/445313123809886228/heavy-weight-signup.gif?width=875&height=676")
    await ctx.send(embed=em)
    
    
@bot.command()
async def wm(ctx):
    await ctx.send("Warmatch info of: **Season 2 - Light Weight**\n\nhttps://warmatch.us/leagues/132")
    
bot.run(os.environ.get('TOKEN'))
    
