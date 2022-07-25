import json
from discord.ext import commands
import discord
import os
from datetime import datetime

config = open('config.json')
config = json.load(config)
token = config.get('token')
bot = commands.Bot(command_prefix='.', help_command=None)

@bot.event
async def on_ready():
    print('Bot online ! ')

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    my_embed = discord.Embed(title='Bashko Generator', description='`.stock : see account stock`\n`.gen : generate an account | example : .gen disney`', color=discord.Color(15277667))
    my_embed.set_image(url='https://cdn.discordapp.com/attachments/988414059315613709/1000504226788687912/standard.gif')
    await ctx.send(embed=my_embed)

@bot.command()
async def stock(ctx):
    await ctx.message.delete()
    list_amount_account = []
    account_file_list = os.listdir('E:\PROJECTS\BASHKO\BOTS\BashkoGen\stock')
    for account_file in account_file_list:
        account_type = account_file.replace('.txt', '')
        with open('stock/' + account_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            amount_account = account_type + " : " + str(len(lines))
            list_amount_account.append(amount_account)
    my_embed = discord.Embed(title='Bashko Generator', description=f'`Stock`\n`{list_amount_account[0]}`\n`{list_amount_account[1]}`\n`{list_amount_account[2]}`\n`{list_amount_account[3]}`\n`{list_amount_account[4]}`', color=discord.Color(15277667))
    my_embed.set_image(url='https://cdn.discordapp.com/attachments/988414059315613709/1000504226788687912/standard.gif')
    await ctx.send(embed=my_embed)

@bot.command()
async def gen(ctx, accountype):
    await ctx.message.delete()
    accounts = []
    account_file_list = os.listdir('E:\PROJECTS\BASHKO\BOTS\BashkoGen\stock')
    for account_file in account_file_list:
        account_type = account_file.replace('.txt', '')
        accounts.append(account_type)
    if accountype in accounts:
        with open('stock/' + accountype + '.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) == 0:
                my_embed = discord.Embed(title='Bashko Generator', description=f'`No {accountype} account is available`', color=discord.Color(15277667))
                my_embed.set_image(url='https://cdn.discordapp.com/attachments/988414059315613709/1000504226788687912/standard.gif')
                await ctx.send(embed=my_embed)
            else:
                for line in lines:
                    line = line.replace('\n', '')
                    combo = line.split(':')
                    email = combo[0]
                    password = combo[1]
                my_embed = discord.Embed(title='Bashko Generator', description=f"`Your {accountype} account was generated check dm's`", color=discord.Color(15277667))
                my_embed.set_image(url='https://cdn.discordapp.com/attachments/988414059315613709/1000504226788687912/standard.gif')
                await ctx.send(embed=my_embed)
                user = bot.get_user(ctx.author.id) or await bot.fetch_user(ctx.author.id)
                my_embed = discord.Embed(title='Bashko Generator', description=f"`Your {accountype} account\nEmail : {email}\nPassword : {password}\nCombo : {email}:{password}`", color=discord.Color(15277667))
                my_embed.set_image(url='https://cdn.discordapp.com/attachments/988414059315613709/1000504226788687912/standard.gif')
                await user.send(embed=my_embed)
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                with open('Generated_log.txt', 'a', encoding='utf-8') as logs:
                    logs.write(ctx.author.name + "#" + ctx.author.discriminator  + ' | ' + str(ctx.author.id) + ' | ' + accountype + ' | ' + email + ':' + password + ' | ' + dt_string + '\n')
                with open("stock/" + accountype + ".txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != f"{email}:{password}":
                            f.write(line)
    else:
        my_embed = discord.Embed(title='Bashko Generator', description=f'`Error invalid account type use .stock to see accounts stock`', color=discord.Color(15277667))
        my_embed.set_image(url='https://cdn.discordapp.com/attachments/988414059315613709/1000504226788687912/standard.gif')
        await ctx.send(embed=my_embed)


bot.run(token)