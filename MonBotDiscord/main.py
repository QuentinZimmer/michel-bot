import discord
from discord.utils import get
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions
from os import getenv
bot = commands.Bot(command_prefix='!')
warnings = {}





@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Je suis le bot de Michel"))

@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    salon = payload.channel_id
    message = payload.message_id
    roles = bot.get_guild(payload.guild_id).roles
    python_role = get(roles, name="python")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    print(membre)

    if salon == 739465742801567788 and emoji == '✅' and message == 739514381020430346:
        print('Grade ajouté !')
        await membre.send("tu obtient le grade python")
        await membre.add_roles(python_role)

@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji.name
    salon = payload.channel_id
    message = payload.message_id
    roles = bot.get_guild(payload.guild_id).roles
    python_role = get(roles, name="python")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    print(membre)

    if salon == 739465742801567788 and emoji == '✅' and message == 739514381020430346:
        print('Grade supprimé !')
        await membre.send("tu obtient le grade python")
        await membre.remove_roles(python_role)


@bot.command()
@has_permissions(administrator=True)
async def ban(ctx, membre: discord.Member):
    pseudo = membre.mention
    await membre.send("Vous avez été ban du serveur !")
    await membre.ban()

@bot.command()
@has_permissions(administrator=True)
async def unban(ctx, membre: discord.Member):
    pseudo = membre.mention
    
    await ctx.send(f"Le membre {pseudo} a été unban !")
    await membre.unban()

@unban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("la commande est: !unban @pseudo")

@bot.command()
async def regles(ctx):
    await ctx.send("Les règles:\n1. Pas d'insultes\n2. Pas de double compte\n3. Pas de spam")


@bot.command()
async def bonjour(ctx):
    for i in range(4):

        await ctx.send(":stonks:")

@bot.command()
@has_permissions(administrator=True)
async def warning(ctx, membre: discord.Member):
    pseudo = membre.mention
    id = membre.id
    if id not in warnings:
        warnings[id] = 0
        print("Le membre n'a aucun avertissement")


    warnings[id] += 1
    print(warnings)
    await ctx.send(f"Le membre {pseudo} a recu un avertissement.")
    await ctx.send(f"Vous avez {warnings[id]}/3 avertissements.")
    print("test")

    if warnings[id] == 3:
        warnings[id] = 0
        await membre.send("Cheh")
        await membre.kick()



@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    pseudo = nouveau_membre.mention
    await ctx.send(f"Bienvenue à {pseudo} sur le serveur discord !")

@bienvenue.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("la commande est: !bienvenue @pseudo")

@warning.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("la commande est: !warning @pseudo")


#run on heroku

print("Lancement du bot...")
bot.run(getenv("TOKEN"))

#run local
"""jeton = ""
bot.run(jeton)"""