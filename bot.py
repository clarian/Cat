# Build V0.2

import discord, sys
import json
import time
from enum import Enum
import aiohttp
import asyncio
import calendar
import logging
from random import *

from discord.ext import commands

admins = ["300355783265353728", "285870888493121536"]

LUNCH_OPTIONS = ["In-N-Out", "Panda Express", "Canes", "Chipotle", "McDonalds", "Jack in the Box", "Kentucky Fried Chicken", "Burger King", "Domino's Pizza", "New York Pizza"]

description = 'client created by Timmy.'
bot_prefix = '!'

version = "1.5"
build = "version 0.2"

client = commands.Bot(description=description, command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Booting up..")
    asyncio.sleep(0.1)
    print("""

 __        __   _                            _           ____      _
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___    / ___|__ _| |_
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |   / _` | __|
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |__| (_| | |_ _
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \____\__,_|\__(_)

    """)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='Type !help for help.'))
    print('------')
    print('Description:')
    print("""


  ____        _ _     _    __     __            _               _
 | __ ) _   _(_) | __| |_  \ \   / /__ _ __ ___(_) ___  _ __   / |
 |  _ \| | | | | |/ _` (_)  \ \ / / _ \ '__/ __| |/ _ \| '_ \  | |
 | |_) | |_| | | | (_| |_    \ V /  __/ |  \__ \ | (_) | | | | | |
 |____/ \__,_|_|_|\__,_(_)    \_/ \___|_|  |___/_|\___/|_| |_| |_|






   ____                _           _   _             _____ _
  / ___|_ __ ___  __ _| |_ ___  __| | | |__  _   _  |_   _(_)_ __ ___  _ __ ___  _   _
 | |   | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |   | | | | '_ ` _ \| '_ ` _ \| | | |
 | |___| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |   | | | | | | | | | | | | | | |_| |
  \____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, |   |_| |_|_| |_| |_|_| |_| |_|\__, |
                                             |___/                               |___/


  _   _ _               _           _         _               _
 | \ | (_)_ __   ___   (_)___    __| | __ _  | |__   ___  ___| |_
 |  \| | | '_ \ / _ \  | / __|  / _` |/ _` | | '_ \ / _ \/ __| __|
 | |\  | | | | | (_) | | \__ \ | (_| | (_| | | |_) |  __/\__ \ |_
 |_| \_|_|_| |_|\___/  |_|___/  \__,_|\__,_| |_.__/ \___||___/\__|

 d8b d8b
888888888
`Y88888P'
 `Y888P'
  `Y8P'
   `Y'
    """)
    print("""

  ___  __                                           _            _   _ _                    _ _
 |_ _|/ _|  _   _  ___  _   _    ___ _ __ __ _  ___| | _____  __| | (_) |_    __      _____| | |
  | || |_  | | | |/ _ \| | | |  / __| '__/ _` |/ __| |/ / _ \/ _` | | | __|   \ \ /\ / / _ \ | |
  | ||  _| | |_| | (_) | |_| | | (__| | | (_| | (__|   <  __/ (_| | | | |_ _   \ V  V /  __/ | |
 |___|_|    \__, |\___/ \__,_|  \___|_|  \__,_|\___|_|\_\___|\__,_| |_|\__( )   \_/\_/ \___|_|_|
            |___/                                                         |/

          .-.                     .-.
          |U|                     | |
          | |                     | |
          | |                     | |
         _| |_                   _| |_
        | | | |-.               | |_| |-.
       /|     ` |              / )| |_|_|
      | |       |             | |-' `-^-'
      |         |             |     ||  |
      \         /             \     '   /
       |       |               |       |
       |       |   VK          |       |

  _   _                    __             _
 | | | | __ ___   _____   / _|_   _ _ __ | |
 | |_| |/ _` \ \ / / _ \ | |_| | | | '_ \| |
 |  _  | (_| |\ V /  __/ |  _| |_| | | | |_|
 |_| |_|\__,_| \_/ \___| |_|  \__,_|_| |_(_)
    """)

@client.event
async def on_member_join(member):
    server = member.server
    await client.send_message(message.channel,'**{0.name}** joined in **{0.server}** Welcome {0.mention}! :) Read the rules to avoid getting banned!'.format(member))

@client.event
async def on_member_remove(member):
    server = member.server
    await client.send_message(message.channel, '**{0.name}** left **{0.server}** :( Goodbye.'.format(member))

@client.event
async def on_message(message):
    from datetime import datetime
    if(str(message.author.id) == '317955240542470154'):
      return

    elif message.content.startswith('!ud'):
      await client.send_message(message.channel, 'https://www.urbandictionary.com/define.php?term={}'.format(str(message.content)).replace('!ud', '').replace(' ', '+'))

    elif message.content.startswith('!time'):
      time = datetime.now()
      current_time = "It's **%s:%s:%s**" % (time.hour, time.minute, time.second)
      current_date = "It's the **%sth of %s %s**" % (time.day, str(calendar.month_name[int(time.month)]), time.year)
      await client.send_message(message.channel, str(current_time))
      await client.send_message(message.channel, str(current_date))


    elif message.content.startswith('!changelog'):
        with open('changelog.txt', 'r') as helpfile:
           helpsend=helpfile.read()
           await client.send_message(message.channel, helpsend)

    elif message.content.startswith('!help'):
        with open('help.txt', 'r') as helpfile:
           helpsend=helpfile.read()
           await client.send_message(message.channel, helpsend)

    #LMGTFY functionality
    elif message.content.startswith('!lmgtfy'):
        await client.send_message(message.channel, 'http://lmgtfy.com/?q={}'.format(str(message.content)).replace('!lmgtfy', '').replace(' ', '+'))

    elif message.content.startswith('!youtube'):
        await client.send_message(message.channel, 'https://www.youtube.com/results?search_query={}'.format(str(message.content)).replace('!youtube', '').replace(' ', '+'))

    #Google Search functionality
    elif message.content.startswith('!goog'):
        await client.send_message(message.channel, 'https://www.google.com/search?q={}'.format(str(message.content)).replace('!goog', '').replace(' ', '+'))

    elif message.content.startswith('!killme'):
        msg = '{} you are now dead'.format(message.author.mention)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!credits'):
        await client.send_message(message.channel, """
Before I begin, I want to say that thanks to **these** nice and awesome people, **Cat** is created.
Show them some love!! <3

Credits:
**NINO Cikoo**#3602 - This guy is the best guy ever. He helped me with everything. \
Errors, basics, cleaning, everything.
**Autistic-Face-Fucker**#6326 - Bringing me to NINO, helped me with a few basic Errors
**spiritual**#8193 - Developer
**mental**#8504 - Developer
**All** people who created a bot on discord in python, so i could learn from them!""")

    elif message.content.startswith('!echo'):
        await client.delete_message(message)
        messageToTTS = message.content[5:]
        await client.send_message(message.channel, messageToTTS)

    elif message.content.startswith('ay'):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=a2v_zGWawP0")

    elif message.content.startswith ('shrug'):
        await client.send_message(message.channel, content='Ã‚Â¯\_(Ã£Æ’â€ž)_/Ã‚Â¯')

    elif message.content.startswith('!smash'):
        import random
        tmp = await client.send_message(message.channel, "Thinking if i should smash...")
        answers = ["Nah, you're too ugly.", "Ofcourse, you're hot.", "Let me pass.", "I want to smash that fat ass.", "I'd rip that pussy apart.",
        "I'm suprised you don't have a fuckbuddy. Here's your new one.", "*slaps dat fatass* I'd deffo smash."]
        await asyncio.sleep(1)
        await client.edit_message(tmp, "Thinking..")
        await asyncio.sleep(1)
        await client.edit_message(tmp, "Thinking.")
        await client.edit_message(tmp, random.choice(answers))

    elif message.content.startswith('!roll'):
        tmp = await client.send_message(message.channel, "Rolling...")
        await asyncio.sleep(1)
        await client.edit_message(tmp, "Rolling..")
        await asyncio.sleep(1)
        await client.edit_message(tmp, "Rolling.")
        await asyncio.sleep(1)
        await client.edit_message(tmp, "Rolling...")
        import random
        roll = random.randint(1, 6)
        await asyncio.sleep(1)
        await client.edit_message(tmp, 'Rolled. You got {}'.format(roll))

    elif message.content.startswith('1738'):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=i_kF4zLNKio")

    elif message.content.startswith('panda'):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=E5ONTXHS2mM")

    elif message.content.startswith('logic'):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=cycUHgg0zzU")
        await client.send_message(message.channel, "I don't wanna be alive..")

    elif message.content.startswith('kys'):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=cycUHgg0zzU")
        await client.send_message(message.channel, "I don't wanna be alive..")

    elif message.content.startswith('kms'):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=cycUHgg0zzU")
        await client.send_message(message.channel, "I don't wanna be alive..")

    elif message.content.startswith('bobby'):
        await client.send_message(message.channel, "Free my nigga Bobby Shmurda ")
        await client.send_message(message.channel, "http://ima.ulximg.com/image/src/artist/1409260459_bd1d432bb741f8243ae6a85c39e4e4da.jpg/6b18f95c2a6666bd688b56db11e4ff60/1409260459_bobby_shmurda_29.jpg")

    elif message.content.startswith("!join"):
        await client.send_message(message.channel, ":smile: You can add me here: https://discordapp.com/oauth2/authorize?client_id=317955240542470154&scope=client&permissions=0 I :heart: you.")

    elif message.content.startswith('bot'):
        await client.send_message(message.channel, "I'm an bot :)")

    elif message.content.startswith('sup'):
        await client.send_message(message.channel, 'Wassup!')

    elif message.content.startswith('Sup'):
        await client.send_message(message.channel, "Waz crackalackin!")

    elif message.content.startswith('!sleep'):
        tmp = await client.send_message(message.channel, 'z')
        for _ in range(3):
            await client.edit_message(tmp, 'z')
            await asyncio.sleep(1)
            await client.edit_message(tmp, 'zz')
            await asyncio.sleep(1)
            await client.edit_message(tmp, 'zzz')
            await asyncio.sleep(1)
        await client.edit_message(tmp, "Done sleeping :)")


    if message.content.startswith('>suggestions'):
        await client.delete_message(message)
        await client.send_message(message.channel, """**Hey there!**

#suggestions is the channel to suggest new things we could add to **Cat** _meow_

We would sincerely appreciate it, if you used this template and give so much information as possible.

**Name of the command**:
**Purpose**:
**Needed libraries**: (optional)
**Example of what it would do**
**More information**(optional)
Please keep in mind that we have also other things to do, so we'll tell you when its done.

**All** suggestions will as soon as possible be under review!
**Please submit possible commands**.

Meow,
**Developers**.""")

    elif message.content.startswith('!support'):
        await client.send_message(message.channel, """**Hey there!**

The official/support server is https://discord.gg/euFUepb / http://discord.me/catbot

Meow,
**Developers**.""")

    elif message.content.startswith('!maintenance'):
        await client.send_message(message.channel, """**Hey there!**

Please note that if the bot is not responding/offline that it's under maintenance.
We are constantly improving **Cat**, to be more efficent, faster, cooler.

Meow,
**Developers**.""")


    elif message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have posted {} messages.'.format(counter))

    elif message.content.startswith('!lunch'):
        temp = randint(0, len(LUNCH_OPTIONS) -1)
        await client.send_message(message.channel, 'I think you should go to %s for lunch.' % LUNCH_OPTIONS[temp])

    elif message.content.startswith("simon says"):
        await client.send_message(message.channel, message.content[10:])

    elif message.content.startswith("!dot"):
        admins = ["300355783265353728", "285870888493121536", "290565955153821696"]
        if message.author.id in admins:
            if message.content[5:] == "online":
                await client.change_presence(status=None, game=discord.Game(name='Type !help for help.'))
                await client.send_message(message.channel, ":ok: I've set status to: **Online**.")
            elif message.content[5:] == "dnd":
                await client.change_presence(status=discord.Status.dnd, game=discord.Game(name='Type !help for help.'))
                await client.send_message(message.channel, ":ok: I've set status to: **Do Not Disturb**.")
            elif message.content[5:] == "ninja":
                await client.change_presence(status=discord.Status.invisible, game=discord.Game(name='Type !help for help.'))
                await client.send_message(message.channel, ":ok: I've set status to: **Invisible**.")
            elif message.content[5:] == "idle":
                await client.change_presence(status=discord.Status.idle, game=discord.Game(name='Type !help for help.'))
                await client.send_message(message.channel, ":ok: I've set status to: **Idle**.")
            else:
                await client.send_message(message.channel, ":no_entry: - Whaaaat. U havin a laugh?")
        else:
            await client.send_message(":no_entry: - no perms 4 u.")

    elif message.content.startswith("!status"):
        admins = ["300355783265353728", "285870888493121536", "290565955153821696"]
        if message.author.id in admins:
            await client.change_presence(game=discord.Game(name=message.content[7:]))
            await client.send_message(message.channel, ":white_check_mark: - All done kthx")
        else:
            await client.send_message(message.channel, ":no_entry: - U got no perms. kthxbye")

    elif message.content.startswith("!servers"):
        admins = ["300355783265353728", "285870888493121536", "290565955153821696"]
        if message.author.id in admins:
            servers = list(client.servers)
            listsrv = []
            for i in servers:
                listsrv.append(i.name)
                listsrv.append(i.id)
            await client.send_message(message.channel, "```[servername, serverid] \n " + str(listsrv) + "```")

    elif message.content.startswith("!invite"):
        admins = ["300355783265353728", "285870888493121536", "290565955153821696"]
        if message.author.id in admins:
            temp = await client.send_message(message.author, ":clock3: Creating invite for: " + message.content[8:] + ".")
            try:
                id = message.content[8:]
                print("Making invite for " + id)
                invite = await client.create_invite(discord.Object(id), max_uses=0, temporary=False, max_age=0)
                print("Created invite: " + str(invite))
                await client.edit_message(temp, ":white_check_mark: Created invite for: " + message.content[11:] + ", valid for 5 minutes: " + str(invite))
            except:
                await client.edit_message(temp, ":no_entry: Failed to create invite.")

    elif message.content.startswith('!updateimage'):
        admins = ["300355783265353728", "285870888493121536", "290565955153821696"]
        if message.author.id in admins:
            print("Updating image now...")
            print(message.content[13:])
            file = "logo.png"
            print("Updating profile image...")
            logo = open(file,"rb")
            msg = await client.send_message(message.channel, ":clock1: - Processing image from assets server...")
            await client.edit_profile(avatar=logo.read())
            await client.edit_message(msg, ":white_check_mark: - Updated image!")
        else:
            await client.send_message(message.channel, "No perms, lmfao.")

    elif message.content.startswith('!serverinfo'):
        import random
        server = message.server
        online = len([m.status for m in server.members
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle])
        total_users = len(server.members)
        text_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.text])
        voice_channels = len(server.channels) - text_channels
        passed = (message.timestamp - server.created_at).days
        created_at = ("Since {}. That's over {} days ago!"
                      "".format(server.created_at.strftime("%d %b %Y %H:%M"),
                                passed))

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description=created_at,
            colour=discord.Colour(value=colour))
        data.add_field(name="Region", value=str(server.region))
        data.add_field(name="Users", value="{}/{}".format(online, total_users))
        data.add_field(name="Text Channels", value=text_channels)
        data.add_field(name="Voice Channels", value=voice_channels)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Owner", value=str(server.owner))
        data.set_footer(text="Server ID: " + str(server.id))

        if server.icon_url:
            data.set_author(name=server.name, url=server.icon_url)
            data.set_thumbnail(url=server.icon_url)
        else:
            data.set_author(name=server.name)

        try:
            await client.send_message(message.channel, embed=data)
        except discord.HTTPException:
            await client.send_message(message.channel, "I need the `Embed links` permission "
                               "to send this")

    elif message.content.startswith("!ball"):
        mess = str(message.content)
        qs = mess.split(" ", 1)
        print (qs[1][-1])
        if qs[1][-1] == "?":
            answers = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                       "Signs point to yes", "Without a doubt", "Yes", "Yes Ã¢â‚¬â€œ definitely", "You may rely on it",
                       "Reply hazy, try again",
                       "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                       "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
                       "Very doubtful"]
            import random
            msg = await client.send_message(message.channel, "Asking my most trustworthy-samurai sources..")
            await client.edit_message(msg, random.choice(answers))
        elif "?" in qs[1]:
            await client.send_message(message.channel, "Are you confused to ask a straight question, huh?")
        else:
            await client.send_message(message.channel, "That's not a question.")

    elif message.content.startswith("!8"):
        mess = str(message.content)
        qs = mess.split(" ", 1)
        print (qs[1][-1])
        if qs[1][-1] == "?":
            answers = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                       "Signs point to yes", "Without a doubt", "Yes", "Yes Ã¢â‚¬â€œ definitely", "You may rely on it",
                       "Reply hazy, try again",
                       "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                       "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
                       "Very doubtful"]
            import random
            msg = await client.send_message(message.channel, "Asking my most trustworthy-samurai sources..")
            await client.edit_message(msg, random.choice(answers))
        elif "?" in qs[1]:
            await client.send_message(message.channel, "Are you confused to ask a straight question, huh?")
        else:
            await client.send_message(message.channel, "That's not a question.")

    elif message.content.startswith("!8ball"):
        mess = str(message.content)
        qs = mess.split(" ", 1)
        print (qs[1][-1])
        if qs[1][-1] == "?":
            answers = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                       "Signs point to yes", "Without a doubt", "Yes", "Yes Ã¢â‚¬â€œ definitely", "You may rely on it",
                       "Reply hazy, try again",
                       "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                       "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
                       "Very doubtful"]
            import random
            msg = await client.send_message(message.channel, "Asking my most trustworthy-samurai sources..")
            await client.edit_message(msg, random.choice(answers))
        elif "?" in qs[1]:
            await client.send_message(message.channel, "Are you confused to ask a straight question, huh?")
        else:
            await client.send_message(message.channel, "That's not a"
             "question.")

    elif message.content.startswith('!load'):
        import random
        x = random.randrange(0,10)
        loading = await client.send_message(message.channel, '`0%   -------------------`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`10%  ||------------------`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`20%  ||||----------------`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`30%  ||||||--------------`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`40%  ||||||||------------`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`50%  ||||||||||----------`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`60%  ||||||||||||--------`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`70%  ||||||||||||||------`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`80%  ||||||||||||||||----`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`90%  ||||||||||||||||||--`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`95%  |||||||||||||||||||-`')
        await asyncio.sleep(x)
        await client.edit_message(loading, '`100% ||||||||||||||||||||`')
        await client.edit_message(loading, 'Loading Complete!')

    elif message.content.startswith('!shutdown'):
        admins = ["300355783265353728", "285870888493121536", "290565955153821696"]
        if message.author.id in admins:
            await client.send_message(message.channel, 'Bye!')
            sys.exit()
        else:
            await client.send_message(message.channel, "Nice try!")

    elif message.content.startswith('!info'):
        import time
        import datetime
        import sys, os
        author_repo = "https://github.com/timmyturnah"
        build = "V0.1"
        server_url = "https://discord.me/catbot"
        python_url = "https://www.python.org/"
        dpy_repo = "https://github.com/Rapptz/discord.py"
        since = datetime.datetime(2017, 5, 27, 0, 0)
        dpy_version = "[{}]({})".format(discord.__version__, dpy_repo)
        days_since = (datetime.datetime.utcnow() - since).days
        py_version = "[{}.{}.{}]({})".format(*os.sys.version_info[:3],
                                     python_url)

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        owner = "ážµ ážµ ážµ ážµ#8193"
        about = (
            "This is an instance of Cat, an (temporarily) closed-source Discord bot "
            "created by Timmy, Nino and Mental. \n\n"
            "Cat is a bot created by passionate developers "
            "that will do everything to rise to the top. \n\n"
            "[Join us today]({}) "
            "and help us improve!\n\n"
            "".format(server_url))

        embed = discord.Embed(colour=discord.Colour(value=colour))
        embed.add_field(name="Owner", value=str(owner))
        embed.add_field(name="Python", value=py_version)
        embed.add_field(name="Build", value=build)
        embed.add_field(name="discord.py", value=dpy_version)
        embed.add_field(name="About Cat", value=about, inline=False)
        embed.set_footer(text="Bringing joy since 27 May 2017 (over "
                 "{} days ago!)".format(days_since))

        try:
          await client.send_message(message.channel, embed=embed)
        except discord.HTTPException:
          await client.send_message(message.channel, "I need the `Embed links` permission to send this")

client.run('token!')
