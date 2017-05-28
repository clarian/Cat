#build v0.2
import discord, sys, json, aiohttp, asyncio, calendar, logging, random, shelve, datetime, time
from discord.ext import commands
##
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='cat.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
##
Vitals = shelve.open("Catvitals")
build = Vitals['build']
admins = Vitals['admins']
botvitals = Vitals['botdetails']

bot = commands.Bot(prefix=botvitals['prefix'], description=botvitals['description'])
bot.remove_command("help")
client = discord.Client()
######
#on_ready displays bot information
@bot.event
async def on_ready():
    print ("%s Bot with build version: %s\nLogged in as: %s\nWith id: %s\nCurrently operating on %s server(s)"%(bot.user.name,build['version'],bot.user.name,bot.user.id,len(bot.servers)))
    await bot.change_presence(game=discord.Game(name=('Type %shelp for a help list.'%(botvitals['prefix']))))
    print("Description:\n%s"%(botvitals['description']))
    pass
#on_member_join greets a user upon server join
@bot.event
async def on_member_join(member):
    server = member.server
    await client.send_message(message.channel,'**{0.name}** joined in **{0.server}** Welcome {0.mention}! :) Read the rules to avoid getting banned!'.format(member))
    pass
#on_member_remove displays goodbye message in channel user left server
@bot.event
async def on_member_remove(member):
    server = member.server
    await bot.send_message(message.channel, '**{0.name}** left **{0.server}** :( Goodbye.'.format(member))
    pass
#on_message uses scanned messages to issue a response
@bot.event
async def on_message(message):
    if message.content.startswith('<@317955240542470154>'):
        await bot.send_message(message.channel, "I'm an bot :)")

    elif message.content.startswith('sup'):
        await bot.send_message(message.channel, 'Wassup!')

    elif message.content.startswith('Sup'):
        await bot.send_message(message.channel, "Waz crackalackin!")
    elif message.content.startswith("simon says"):
        await bot.send_message(message.channel, ("simon: "+str(message.content[10:])))    
    pass
##########
#Commands#
##########
@bot.command()
async def ud(*,message):
    """Urban dictionary lookup"""
    await bot.say('https://www.urbandictionary.com/define.php?term={}'.format(str(message)))
    pass
##
@bot.command()
async def time():
    """Say the time"""
    time = datetime.now()
    current_time = "It's **%s:%s:%s**" % (time.hour, time.minute, time.second)
    current_date = "It's the **%sth of %s %s**" % (time.day, str(calendar.month_name[int(time.month)]), time.year)
    await bot.say(str(current_time))
    await bot.say(str(current_date))
    pass
##
@bot.command()
async def changelog():
    """View the changelog"""
    try:
        changefile = open('changelog.txt', 'r')
    except FileNotFoundError:
        await bot.say("There has been and error and the developers have been informed.\nApologies for the disruption")
        print ("'changelog.txt' has not been found in the local directory or in any connected directories")
    await bot.say(changefile.read())    
    pass
##
@bot.command()
async def help():
    """help list"""
    try:
        helpfile = open('help.txt', 'r')
    except FileNotFoundError:
        await bot.say("There has been and error and the developers have been informed.\nApologies for the disruption")
        print ("'help.txt' has not been found in the local directory or in any connected directories")
    await bot.say(helpfile.read())
    pass
##
@bot.command()
async def lmgtfy(*,message):
    """lmgtfy generator"""
    await bot.say('http://lmgtfy.com/?q={}'.format(str(message)))
    pass
##
@bot.command()
async def google(*,message):
    """google search generator"""
    await client.say('https://www.google.com/search?q={}'.format(str(message)))
    pass
##
@bot.command(pass_context=True)
async def killme(ctx):
    """kys"""
    msg = '{} you are now dead'.format(ctx.message.author.mention)
    await client.say(msg)
    pass
##
@bot.command()
async def credits():
    """View credits"""
    try:
        creditfile = open('credits.txt', 'r')
    except FileNotFoundError:
        await bot.say("There has been and error and the developers have been informed.\nApologies for the disruption")
        print ("'credits.txt' has not been found in the local directory or in any connected directories")
    await bot.say(creditfile.read())
    pass
##
@bot.command(pass_context=True)
async def echo(ctx,*,message):
    """Echoes a message"""
    await bot.delete_message(ctx.message)
    await bot.say(message)
    pass
##
@bot.command()
async def ay():
    """ay command"""
    await bot.say("https://www.youtube.com/watch?v=a2v_zGWawP0")
    pass
##
@bot.command()
async def shrug():
    """have a shrug"""
    await bot.say("�\_(0_0)_/�")
    pass
##
@bot.command()
async def smash():
    """smash it"""
    answers = ["Nah, you're too ugly.", "Ofcourse, you're hot.", "Let me pass.", "I want to smash that fat ass.", "I'd rip that pussy apart.",
               "I'm suprised you don't have a fuckbuddy. Here's your new one.", "*slaps dat fatass* I'd deffo smash."]
    think = "Thinking..."
    modify = await bot.say(think)
    for i in range(3):
        await asyncio.sleep(1)
        await bot.edit_message(modify, think[:-(i+1)])
        pass
    await bot.edit_message(modify, random.choice(answers))
    pass
##
@bot.command()
async def roll():
    """roll a dice"""
    roll = "Rolling..."
    modify = await bot.say(roll)
    for i in range(3):
        await asyncio.sleep(1)
        await bot.edit_message(modify, roll[:-(i+1)])
        pass
    await bot.edit_message(modify, str(random.randint(1,6)))
    pass
##
@bot.command()
async def vids(selection):
    """view a vid"""
    global botvitals
    total = {'1738':"https://www.youtube.com/watch?v=i_kF4zLNKio",'panda':"https://www.youtube.com/watch?v=E5ONTXHS2mM",
             'logic':"I don't wanna be alive..\nhttps://www.youtube.com/watch?v=cycUHgg0zzU",'kys':"I don't wanna be alive..\nhttps://www.youtube.com/watch?v=cycUHgg0zzU",
             'kms':"I don't wanna be alive..\nhttps://www.youtube.com/watch?v=cycUHgg0zzU",'bobby':"http://ima.ulximg.com/image/src/artist/1409260459_bd1d432bb741f8243ae6a85c39e4e4da.jpg/6b18f95c2a6666bd688b56db11e4ff60/1409260459_bobby_shmurda_29.jpg\nFree my nigga Bobby Shmurda "}
    if selection in total:
        await bot.say(total[selection])
    elif selection not in total:
        await bot.say(("%s Was not a valid selection to play.\nTo view the selections use '%svids list'"%(selection,botvitals['prefix'])))
    else:
        await bot.say("An Error has occured the developers have been notified")
    pass
##
@bot.command()
async def sleep(time):
    """sleep command"""
    try:
        x = time/10
    except TypeError:
        await bot.say("Please enter and integer between 1-60")
        return
    if time > 60 or time < 1:
        time = 5
        pass
    roll = "zzz"
    modify = await bot.say(roll)
    for i in range(3):
        await asyncio.sleep(time)
        await bot.edit_message(modify, roll[:-(i+1)])
        pass
    await bot.edit_message(modify, "Done sleeping :)")
    pass
##
@bot.command(pass_context=True)
async def suggest(ctx,title,purpose,example):
    homeserver = discord.utils.get(bot.servers, id="317960480696172544")
    suggestionschan = discord.utils.get(homeserver, name="suggestions")
    allist = [title,purpose,example]
    if "" in allist or " " in allist:
        await bot.say("Please make sure to fill out all aplicable entries")
        return
    else:
        em = discord.Embed(title=("Suggestion from %s"%(ctx.message.author))
                           ,description=("Title:\n%s\nPurpose:\n%s\nExample (including libs):\n%s"%(title,purpose,example))
                           ,colour=(255 << 16) + (255 << 8) + 255, timestamp=datetime.datetime.now())
        em = em.set_thumbnail(url=ctx.message.author.avatar_url)
        await bot.send_message(suggestionschan,embed=em)
        await bot.say("Your suggestion has been submitted successfully :white_check_mark:")
    pass
##
@bot.command()
async def support():
    await bot.say("**Hey there!**\n\nThe official/support server is <https://discord.gg/euFUepb> | <http://discord.me/catbot\n\nMeow>,\n**Developers**.")
    pass
##
@bot.command()
async def maintenance():
    await bot.say("**Hey there!**\n\nPlease note that if the bot is not responding/offline that it's under maintenance.\nWe are constantly improving **Cat**, to be more efficent, faster, cooler.\n\nMeow,\n**Developers**.")
    pass
##
@bot.command(pass_context=True)
async def test(ctx):
    counter = 0
    await client.say('Calculating messages...')
    async for log in bot.logs_from(ctx.message.channel, limit=100):
        if log.author == message.author:
            counter += 1
    await bot.say(('In the last 100 messages You have posted {} of them.'.format(counter)))
    pass
##
@bot.command()
async def lunch():
    LUNCH_OPTIONS = ["In-N-Out", "Panda Express", "Canes", "Chipotle", "McDonalds", "Jack in the Box", "Kentucky Fried Chicken", "Burger King", "Domino's Pizza", "New York Pizza"]
    await bot.say(('I think you should go to %s for lunch.' % LUNCH_OPTIONS[random.randint(0,len(LUNCH_OPTIONS))]))
    pass
##
@bot.command(pass_context=True)
async def dot(ctx,status):
    global admins
    if ctx.message.author.id in admins:
        if switch.lower() == "online":
            await bot.change_presence(status=None, game=discord.Game(name='Type !help for help.'))
            await bot.say(":ok: I've set status to: **Online**.")
        elif switch.lower() == "dnd":
            await bot.change_presence(status=discord.Status.dnd, game=discord.Game(name='Type !help for help.'))
            await bot.say(":ok: I've set status to: **Do Not Disturb**.")            
        elif switch.lower() == "ninja" or switch.lower() == "invis" or switch.lower() == "invisible":
            await bot.change_presence(status=discord.Status.invisible, game=discord.Game(name='Type !help for help.'))
            await bot.say(":ok: I've set status to: **Invisible**.")
        elif switch.lower() == "idle":
            await bot.change_presence(status=discord.Status.idle, game=discord.Game(name='Type !help for help.'))
            await bot.say(":ok: I've set status to: **Idle**.")
        else:
            await bot.say(("Please include a status <@%s>"%(ctx.message.author.id)))
    else:
        await bot.say(":no_entry: - no perms 4 u.")
    pass
##
@bot.command(ctx)
async def servers(ctx):
    global admins
    if ctx.message.author.id in admins:
        serverList = {}
        for server in bot.servers:
            serverList[server.name] = server.id
        compiledmessage = ""
        for entry in serverList:
            compiledmessage+=str(entry)+" : "+str(serverList[entry])+"\n"
        await bot.send_message(ctx.message.author.id,compiledmessage)
        await bot.say(":ok_hand:")
    else:
        await bot.say("Access denied")
    pass
##
@bot.command(pass_context=True)
async def updateimage(ctx):
    global admins
    if ctx.message.author.id in admins:
        print("Updating image now...")
        try:
            file = "logo.png"
        except FileNotFoundError:
            print ("No logo.png found")
            await bot.say("Failed to find 'logo.png' please fix")
            return
        print("Updating profile image...")
        logo = open(file,"rb")
        await bot.say(":clock1: - Processing image from assets server...")
        await bot.edit_profile(avatar=logo.read())
        await bot.say(":white_check_mark: - Updated image!")
    else:
        await bot.say("Not enough perms.")
    pass
##
@bot.command(pass_context=True)
async def serverinfo(ctx):
    server = ctx.message.server
    online = len([m.status for m in server.members
                  if m.status == discord.Status.online or
                  m.status == discord.Status.idle])
    total_users = len(server.members)
    text_channels = len([x for x in server.channels
                         if x.type == discord.ChannelType.text])
    voice_channels = len(server.channels) - text_channels
    passed = (ctx.message.timestamp - server.created_at).days
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
        await client.send_message(ctx.message.channel, embed=data)
    except discord.HTTPException:
        await client.send_message(ctx.message.channel, "I need the `Embed links` permission "
                                  "to send this")
    pass
##
@bot.command()
async def ball(*,question):
    answers = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
               "Signs point to yes", "Without a doubt", "Yes", "Yes Ã¢â‚¬â€œ definitely", "You may rely on it",
               "Reply hazy, try again",
               "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
               "Very doubtful"]
    await asyncio.sleep(1)
    await bot.say(("%s"%(random.choice(answers))))
    pass
##
@bot.command()
async def load():
    a = "-------------------"
    x = await bot.say("`0%   -------------------`")
    for i in range (20):
        await bot.edit_message(x("`"+(str(i)+"%  "+(i)*(i+1)+a[(i+1):])+"`"))
        await asyncio.sleep(1)
    await bot.say('Loading Complete!')
    pass
##
@bot.command()
async def info():
    global build
    build = build['version']
    author_repo = "<https://github.com/timmyturnah>"
    server_url = "<https://discord.me/catbot>"
    python_url = "<https://www.python.org/>"
    dpy_repo = "<https://github.com/Rapptz/discord.py>"
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
        await bot.say(embed=embed)
    except discord.HTTPException:
        await bot.say("I need the `Embed links` permission to send this")
        
bot.run("token")