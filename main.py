import os
import keep_alive
import discord, asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
from colorama import Fore, Style
import io, smtplib, ssl
from discord.ext import commands, tasks
import random
from discord import Permissions
from discord import Guild, Member, Embed
import random, requests, os, sys, threading, time, json, asyncio, discord, aiohttp, urllib.parse, urllib.request, time
from itertools import cycle
from urllib import parse, request
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

import os

os.system('cls & mode 85,20 & title 340 SELF BOT ')
os.system('cls')
prefix = input('340 SELFBOT PREFIX :  ')
token = input('340 SELFBOT TOKEN: ')
password = input('340 SELFBOT PASSWORD: ')
client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
client.remove_command(name='help')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='340 Self Bot', url='https://twitch.tv/ExtaZy'))
    print('Im Ready\nLEGEND OP')



def check_token():
    if requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': f"{token}"}).status_code == 200:
        return 'user'
    else:
        return 'bot'


token_type = check_token()
intents = discord.Intents.all()
intents.members = True
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix='$', case_insensitive=False, self_bot=True, intents=intents)
else:
    if token_type == 'bot':
        headers = {'Authorization': f"Bot {token}"}
        client = commands.Bot(command_prefix='$', case_insensitive=False, intents=intents)
os.system('cls')

def check_token():
    if requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': f"{token}"}).status_code == 200:
        return 'user'


client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
client.remove_command(name='help')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')
token_type = check_token()
intents = discord.Intents.all()
intents.members = True
os.system(f"cls & mode 85,20 & title [340 SELF BOT] - Connected: {client.user}")
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix='$', case_insensitive=False, self_bot=True, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='340 Selfbot', url='https://twitch.tv/ExtaZy'))


print('YOUR ACCOUNT IS ALIVE WITH MOST OP SELF BOT TYPE $alive TO CHECK \n JOIN https:cord.gg/zRm2ccYJzt')

@client.command()
async def massban(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send('**Le massban commence...**')
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Banned{member.strip()}")
                    break
                else:
                    break

    members.close()





@client.command()
async def masskick(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send('**Le masskick commence...**')
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Kicked {member.strip()}")
                    break
                else:
                    break

    members.close()


@client.command()
async def general(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='340 - Selfbot')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(url='')
    embed.add_field(name=' `$prefix`', value='Change le pr??fixe du bot', inline=False)
    embed.add_field(name=' `$avatar <@user/user id`', value='Grab une pp', inline=False)
    embed.add_field(name=' `$leave <server-id>`', value='Quitter un serveur', inline=False)
    embed.add_field(name=' `$end`', value='??teint le selfbot', inline=False)
    embed.add_field(name=' `$copy`', value='Cr??e une back up', inline=False)
    embed.add_field(name=" `$snipe`", value='Affiche un message supprim??', inline=False)
    embed.set_footer(text='Cr??e par Extazy ')
    await ctx.send(embed=embed) 
    
    
@client.command()
async def text(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='340 - Selfbot')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(url='')
    embed.add_field(name='`$spam [message]`', value='Spam un message', inline=False)
    embed.add_field(name='`$embed [message]`', value='Envoie un message en embed', inline=False)
    embed.add_field(name='`$crash [message]`', value='Aggrandit le text', inline=False)
    embed.set_footer(text='Cr??e par Extazy ')
    await ctx.send(embed=embed)


@client.command()
async def info(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name=' 340 - Selfbot ')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(url='https://media.discordapp.net/attachments/918266987459784785/932250024040083466/20220116_132625.gif')
    embed.add_field(name=' `$userinfo <@user/user id>`', value='Donne les infos d un utilisateur', inline=False)
    embed.add_field(name=' `$banner <server id>`', value='Grab la banni??re d un serveur', inline=False)
    embed.add_field(name=' `$logo <server id>`', value='Grab le logo d un serveur', inline=False)
    embed.add_field(name='`$mc <server id>`',
    value='Voir le nombres de membre d un serveur',
    inline=False)
    embed.add_field(name=' `$tokeninfo <token>`', value='Sort les infos d un token', inline=False)
    embed.set_footer(text='Cr??e par Extazy ')
    await ctx.send(embed=embed)



@client.command()
async def status(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='340 - Selfbot')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(url='https://media.discordapp.net/attachments/918266987459784785/932250024040083466/20220116_132625.gif')
    embed.add_field(name='`$stream`', value='Active le statut stream', inline=False)
    embed.add_field(name='`$play`', value='Active le statut joue ??', inline=False)
    embed.add_field(name='`$listen`', value='Active le statut ??couter', inline=False)
    embed.add_field(name='`$watch`', value='Active le statut regarde', inline=False)
    embed.add_field(name='`$removestatus`', value='Retire le status personnalis??', inline=False)
    embed.set_footer(text='Cr??e par Extazy')
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name = '340 - Selfbot')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(url='https://media.discordapp.net/attachments/918266987459784785/932250024040083466/20220116_132625.gif')
    embed.add_field(name='`$general`', value='Affiche le menu g??n??ral', inline=False)
    embed.add_field(name='`$text`', value='Affiche le menu text', inline=False)
    embed.add_field(name='`$info`', value='Affiche le menu info', inline=False)
    embed.add_field(name='`$moderation`', value='Affiche le menu mod??ration', inline=False)
    embed.add_field(name='`$nuke`', value='Affiche le menu nuker', inline=False)
    embed.add_field(name='`$status`' , value='Affiche le menu status', inline=False)
    embed.set_footer(text='Cr??e par Extazy')
    await ctx.send(embed=embed)


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='340 - Selfbot')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(url='https://media.discordapp.net/attachments/918266987459784785/932250024040083466/20220116_132625.gif')
    embed.add_field(name='`$raid`', value='Raid un serveur', inline=False)
    embed.add_field(name='`$massban`', value='Massban sur un serveur', inline=False)
    embed.add_field(name='`$masskick`', value='Massban sur un serveur', inline=False)
    embed.add_field(name='`$rr`', value='Rename all r??les sur un serveur', inline=False)
    embed.add_field(name='`$rc`', value='Rename all channels sur un serveur', inline=False)
    embed.add_field(name='`$massping`', value='Massping sur un serveur', inline=False)
    embed.add_field(name=' `$stop`', value='Stop mass everyone ping', inline=False)
    embed.add_field(name=' `$deletewebhook`', value='Supprime les webhooks', inline=False)
    embed.add_field(name=' `$adminall`', value='Give le r??les admin a tous le monde', inline=False)
    embed.set_footer(text='Cr??e par Extazy')
    await ctx.send(embed=embed)


@client.command()
async def moderation(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='340 - Selfbot')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(url='https://media.discordapp.net/attachments/918266987459784785/932250024040083466/20220116_132625.gif')
    embed.add_field(name='`$ban <@user/user id`', value='Ban un utilisateur', inline=False)
    embed.add_field(name='`$kick <@user/user id`', value='Kick un utilisateur', inline=False)
    embed.add_field(name='`$unban <@user/user id`', value='Unban un utilisateur', inline=False)
    embed.add_field(name='`$lock`', value='Lock un channels', inline=False)
    embed.add_field(name='`$clear`', value='Supprime un message', inline=False)
    embed.add_field(name='`$dmall`', value='dm tous tes amis', inline=False)
    embed.add_field(name='`$mute`', value='Mute un utilisateur', inline=False)
    embed.add_field(name='`$unmute`', value='Unmute un utilisateur', inline=False)
    embed.set_footer(text='Cr??e par Extazy ')
    await ctx.send(embed=embed)

@client.command()
async def prefix(ctx, prefix):
    client.command_prefix = str(prefix)
    await ctx.message.delete()
    await ctx.send('```Le pr??fixe a bien ??t?? chang??```')


@client.command(aliases=["mc"])

async def member_count(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f"members in {ctx.guild.name}",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=embed)


@client.command()
async def stop(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass

    spammingdawebhookeroos = False


@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@client.command()
async def avatar(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    format = 'gif'
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = 'png'
    avatar = user.avatar_url_as(format=(format if format != 'gif' else None))
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as (file):
        await ctx.send(file=(discord.File(file, f"Avatar.{format}")))


@client.command(aliases=['logout'])
async def end(ctx):
    await ctx.message.delete()
    await client.logout()


@client.command(aliases=['copyserver'])
async def backup(ctx):
    await ctx.message.delete()
    await client.create_guild(f"backup-{ctx.guild.name}")
    await asyncio.sleep(4)
    for g in client.guilds:
        if f"backup-{ctx.guild.name}" in g.name:
            for c in g.channels:
                await c.delete()

            for cate in ctx.guild.categories:
                x = await g.create_category((f"{cate.name}"))
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel((f"{chann}"))
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel((f"{chann}"))

    try:
        await g.edit(icon=(ctx.guild.icon_url))
    except:
        pass


@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name=("{}'s info".format(ctx.message.server.name)), description='Voici les infos sur le serveur', color=65280)
    embed.set_author(name='340 - Selfbot')
    embed.add_field(name='Name', value=(ctx.message.server.name), inline=True)
    embed.add_field(name='ID', value=(ctx.message.server.id), inline=True)
    embed.add_field(name='Roles', value=(len(ctx.message.server.roles)), inline=True)
    embed.add_field(name='Members', value=(len(ctx.message.server.members)))
    embed.set_thumbnail(url=(ctx.message.server.icon_url))
    await client.say(embed=embed)


@client.command(description='Unmuttes un utilisateur')
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get((ctx.guild.roles), name='340 tas mut??')
    await member.remove_roles(mutedRole)
    await member.send(f" Tu as ??t?? d??mut??: - {ctx.guild.name}")
    embed = discord.Embed(title='340 - Selfbot ', description=f" unmute-{member.mention}", colour=(discord.Colour.light_gray()))
    await ctx.send(embed=embed)


@client.command(description='Mutes un utilisateur')
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get((guild.roles), name='340 ta mut??')
    if not mutedRole:
        mutedRole = await guild.create_role(name='340 mute')
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    embed = discord.Embed(title='340 - Selfbot', description=f"{member.mention} as ??t?? mute ", colour=(discord.Colour.light_gray()))
    embed.add_field(name='Raison :', value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" Tu as ??t?? mute par : {guild.name} Raison : {reason}")


@client.command()
async def userinfo(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=(discord.Colour.default()), timestamp=(ctx.message.created_at), title=f"User Info - {member}")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text='Cr??e par Extazy ')
    embed.add_field(name='ID:', value=(member.id), inline=False)
    embed.add_field(name='Display Name:', value=(member.display_name), inline=False)
    embed.add_field(name='Compte cr??e le : ', value=(member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Serveur rejoint : ', value=(member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')), inline=False)
    embed.add_field(name='Roles:', value=(''.join([role.mention for role in roles])), inline=False)
    embed.add_field(name='Role :', value=(member.top_role.mention), inline=False)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@client.command()
async def crash(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")


@client.command()
async def deletewebhook(ctx, link=None):
    if link == None:
        embed = discord.Embed(title='340 - Selfbot', description='```>delete les webhook <webhook```')
        embed.set_footer(text='Cr??e par Extazy')
        await ctx.message.edit(content='', embed=embed)
    else:
        embed = discord.Embed(title='340 - Selfbot', description=f"Sending a delete request to\n{link}")
        embed.set_footer(text='Cr??e par Extazy')
        await ctx.message.edit(content='', embed=embed)
        result = requests.delete(link)
        if result.status_code == 204:
            embed = discord.Embed(title='340 - Selfbot', description='Webhook supprimer')
            embed.set_footer(text='Cr??e par Extazy')
            await ctx.message.edit(embed=embed)
        else:
            embed = discord.Embed(title='340 - Selfbot', description=f"Delete request responded with status code : {result.status_code}\\{result.text}")
            embed.set_footer(text='Cr??e par Extazy')
            await ctx.message.edit(embed=embed)


@client.command()
async def banner(ctx):
    em = discord.Embed(title=(ctx.guild.name))
    em.set_image(url=(ctx.guild.banner_url))
    await ctx.send(embed=em)


@client.command()
async def logo(ctx):
    em = discord.Embed(title=(ctx.guild.name))
    em.set_image(url=(ctx.guild.icon_url))
    await ctx.send(embed=em)

@client.command()
async def host(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "dnd"
    }
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    await asyncio.sleep(5)
    while True:
        setting = {
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@client.command()
async def tokeninfo(ctx, _token):
    headers = {'Authorization':_token,  'Content-Type':'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {'Authorization':'Bot ' + _token, 
         'Content-Type':'application/json'}
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
             {'name':'Flags', 
              'value':res['flags']},
             {'name':'Local language', 
              'value':res['locale'] + (f"{language}")},
             {'name':'Verified', 
              'value':res['verified']}]
            for field in fields:
                if field['value']:
                    em.add_field(name=(field['name']), value=(field['value']),
                      inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")

            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send('Invalid token')

    em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    nitro_type = 'None'
    if 'premium_type' in res:
        if res['premium_type'] == 2:
            nitro_type = 'Nitro Premium'
        elif res['premium_type'] == 1:
            nitro_type = 'Nitro Classic'
    fields = [
     {'name':'Phone', 
      'value':res['phone']},
     {'name':'Flags', 
      'value':res['flags']},
     {'name':'Local language', 
      'value':res['locale'] + (f"{language}")},
     {'name':'MFA', 
      'value':res['mfa_enabled']},
     {'name':'Verified', 
      'value':res['verified']},
     {'name':'Nitro', 
      'value':nitro_type}]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']), value=(field['value']),
              inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            em.set_footer(text='Created by Extazy')

    return await ctx.send(embed=em)


@client.command ()#line:932
async def restart (OOO0OOOO0OO0000OO ):#line:933
    await OOO0OOOO0OO0000OO .send ("\x52\x65\x73\x74\x61\x72\x74\x69\x6E\x67\x20\x53\x65\x6C\x66\x62\x6F\x74\x2E\x2E\x2E\x2E\x2E\x2E\x2E\x2E")#line:934
    os .system ('python '+sys .argv [0 ])#line:935

@client.command()
async def ipinfo(ctx, *, ipaddr: str='54.47.2.7'):
    r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
    geo = r.json()
    em = discord.Embed()
    fields = [
     {'name':'IP', 
      'value':geo['query']},
     {'name':'Type', 
      'value':geo['ipType']},
     {'name':'Country', 
      'value':geo['country']},
     {'name':'City', 
      'value':geo['city']},
     {'name':'Continent', 
      'value':geo['continent']},
     {'name':'Country', 
      'value':geo['country']},
     {'name':'Hostname', 
      'value':geo['ipName']},
     {'name':'ISP', 
      'value':geo['isp']},
     {'name':'Latitute', 
      'value':geo['lat']},
     {'name':'Longitude', 
      'value':geo['lon']},
     {'name':'Org', 
      'value':geo['org']},
     {'name':'Region', 
      'value':geo['region']}]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']), value=(field['value']), inline=True)

    return await ctx.send(embed=em)


languages = {'hu':'Hungarian, Hungary', 
 'nl':'Dutch, Netherlands', 
 'no':'Norwegian, Norway', 
 'pl':'Polish, Poland', 
 'pt-BR':'Portuguese, Brazilian, Brazil', 
 'ro':'Romanian, Romania', 
 'fi':'Finnish, Finland', 
 'sv-SE':'Swedish, Sweden', 
 'vi':'Vietnamese, Vietnam', 
 'tr':'Turkish, Turkey', 
 'cs':'Czech, Czechia, Czech Republic', 
 'el':'Greek, Greece', 
 'bg':'Bulgarian, Bulgaria', 
 'ru':'Russian, Russia', 
 'uk':'Ukranian, Ukraine', 
 'th':'Thai, Thailand', 
 'zh-CN':'Chinese, China', 
 'ja':'Japanese', 
 'zh-TW':'Chinese, Taiwan', 
 'ko':'Korean, Korea'}
locales = [
 'da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl',
 'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg',
 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko']

@client.command()
async def raid(ctx):
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

    try:
        await ctx.guild.edit(name='340', description='340 Selfbot',
          reason='Extazy ta niquer',
          icon=None,
          banner=None)
    except:
        pass

    for _i in range(100):
        await ctx.guild.create_text_channel(name='340')

    for _i in range(100):
        await ctx.guild.create_role(name='340')

    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason='340 ?? niquer le serveur')
        except:
            pass

    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason='340 ?? niquer le serveur')
        except:
            pass


format = '%a, %d %b %Y | %H:%M:%S % ZGMT'

@client.command()
async def rr(ctx, *, name):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        await role.edit(name=name)


from random import choice
from discord.ext import commands

@client.command()
@commands.guild_only()
async def tag(ctx):
    await ctx.message.delete()
    await ctx.send(choice(tuple(member.mention for member in ctx.guild.members)))

    import random

@client.command()
async def rip(ctx):
      await ctx.message.delete()
      channel = ctx.channel
      randomMember = random.choice(channel.guild.members)
      randomMember1 = random.choice(channel.guild.members)
      randomMember2 = random.choice(channel.guild.members)
      await ctx.send(f'{randomMember.mention}{randomMember1.mention}{randomMember2.mention}')
      await ctx.channel.purge(limit=1)
      await asyncio.sleep(5)
      await ctx.send(">rip")

@client.command()
async def rc(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name) 


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('```Utilisateur kick avec succ??s``')

@client.command()
async def role(ctx, user):
  await ctx.message.delete()
  await ctx.send(f"<@235148962103951360> role {user} 869444380879101952")
  await ctx.send(f"-invite reset {user}")
  await ctx.send(f"{user} **340** <#869433500347031593>")

@client.command()
async def bbb(ctx, amount: int=None):
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('```Utilisateur bannit avec succ??s```')


@client.command()
async def lock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role), send_messages=False)
    await ctx.send(ctx.channel.mention + 'Permissions bloqu??')


@client.command()
async def adminall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get((guild.roles), name='@everyone')
        await role.edit(permissions=(Permissions.all()))
        print(Fore.MAGENTA + '**Give r??le admin...**' + Fore.RESET)
    except:
        print(Fore.GREEN + '**Give avec succ??s' + Fore.RESET)


@client.command()
async def unlock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role), send_messages=True)
    await ctx.send(ctx.channel.mention + 'Permissions d??bloqu??')


@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_user:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@client.command()
async def clear(ctx, amount=5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)




@client.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening),
      name=message))

def spam(webhook):
    while spammingdawebhookeroos:
        data = {'content':'@everyone @here 340 te ez !!'}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command()
async def pings(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 100 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 2
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Ez by 340 ')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Webhook Error")

@client.command()
async def play(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await client.change_presence(activity=game)


@client.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message,
      url='https://twitch.tv/ExtaZy')
    await client.change_presence(activity=stream)


@client.command()
async def watch(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching),
      name=message))


@client.command()
async def removestatus(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=(discord.Status.dnd))


@client.command()
async def massmail(ctx, reciver):
    email = 'fg.pheonix.gaming@gmail.com'
    password = 'anger2009#'
    reciever = reciver
    sslcontext = ssl.create_default_context()
    for i in range(0, 1000):
        message = ' Extazy '    
        port = 465
        connection = smtplib.SMTP_SSL('smtp.gmail.com', port, context=sslcontext)
        connection.login(email, password)
        connection.sendmailemailrecievermessage
        await ctx.send('DONE')



@client.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@client.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('```' + message + '```')


@client.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=100).flatten()
    for message in messages:
        await message.add_reaction(emote)


@client.command()
async def dm(ctx, user: discord.Member, *, message):
    await ctx.message.delete()
    user = client.get_user(user.id)
    if ctx.author.id == client.user.id:
        return
    try:
        await user.send(message)
    except:
        pass


@client.command()
async def embed(ctx, *, description):
    embed = discord.Embed(title='340 - Selfbot', description=description)
    embed.set_footer(text='Cr??e par Extazy ')
    await ctx.send(embed=embed)


@client.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(arguments[str.find(arguments, 'msg:'):str.find(arguments, '1:')]).replace('msg:', '')
    option1 = discord.utils.escape_markdown(arguments[str.find(arguments, '1:'):str.find(arguments, '2:')]).replace('1:', '')
    option2 = discord.utils.escape_markdown(arguments[str.find(arguments, '2:'):]).replace('2:', '')
    message = await ctx.send(f"`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`")
    await message.add_reaction('?????????')
    await message.add_reaction('?????????')


@client.command()
async def leave(ctx, guild_id):
    await client.get_guild(int(guild_id)).leave()
    await ctx.send(f"Tu as quitt?? {guild_id}")


@client.command()
async def hi(ctx):
    await ctx.add_reaction(':xeodanceshorty:')

@client.command()
async def owo(ctx):
    for _i in range(1000000000):
        await ctx.send("owo h")
        await asyncio.sleep(120)

@client.command()
async def bump(ctx):
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')


@client.command()
async def dmall(ctx, *, message):
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"messaged: {user.name}")
        except:
            print(f"couldnt message: {user.name}")

@client.command()
async def alive(ctx):
    embed = discord.Embed(title='340 - Selfbot', description='340 Selfbot est toujours connect?? faite $help')
    embed.set_footer(text='Cr??e par Extazy ')
    await ctx.send(embed=embed)

@client.command()
async def roxxop(ctx):
    await ctx.send('Extazy')
 

snipe_message_author = {}
snipe_message_content = {}
 
@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
 
@client.command()
async def snipe(ctx):
    channel = ctx.channel 
    try:
        snipeEmbed = discord.Embed(title=f"Dernier message supprim?? #{channel.name}", description = snipe_message_content[channel.id])
        snipeEmbed.set_footer(text=f"Supprimer par {snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
    except:
        await ctx.send(f"Aucun message supprim?? ici #{channel.name}")

  
keep_alive.keep_alive()

client.run(token, bot=False)
