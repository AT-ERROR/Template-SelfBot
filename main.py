from json import dumps
from time import sleep
from os import system, name
from discord.ext import commands


if name  == "nt":
    system("color 1")
    def clear():
        system("cls")
else:
    def clear():
        system("clear")

    
try:
    import discord
    import requests
except:
    print("Les modules nécessaires ne sont pas installés.")
    sleep(1.5)
    clear()
    print("Tentative d'installation des modules...\n")
    sleep(0.5)
    try :
        system("pip install discord")
        system("pip install requests")
        clear()
        print("Les modules sont maintenant installés.")
        sleep(1)
        clear()
        import discord
        import requests
    except Exception as e :
        print("Erreur lors de la tentative d'installation des modules.")
        sleep(1.5)
        print(f"Code d'erreur : {e}")
        input()
        quit()


token = input("Token > ")

ping = False

lien_pdp_webhook = requests.get("https://pastebin.com/raw/Dgqx6vAg").text

bot = commands.Bot(
    description="AT. Selfbot",
    command_prefix="&",
    self_bot=True
)

bot.remove_command('help') 

"""
"Content-Type" : "application/x-www-form-urlencoded",
"""

headers = {
    "Content-Type" : "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Cherrys Tools 🍒", url="https://www.twitch.tv/at_error"))
    print("Bot is ready!")

@bot.event
async def on_message(message):
    id = bot.user.id
    liste_message = message.content.split(" ")

    channel = message.channel
    guild = message.guild
    
    
    if message.author.id == id:

        if message.content == "&test":
            await message.edit(content=":)")

        if message.content == "&github":
            embed=discord.Embed(title="Mon Github", url="https://github.com/AT-ERROR", color=0xfffffd)
            embed.set_author(name="AT.", icon_url="https://media.discordapp.net/attachments/762390237988257812/856941278540464188/AT-removebg-preview.png?width=494&height=494", url="https://github.com/AT-ERROR")
            embed.set_footer(text="https://github.com/AT-ERROR")
            embed.set_image(url="https://media.discordapp.net/attachments/762390237988257812/856941278540464188/AT-removebg-preview.png?width=494&height=494")
            await message.edit(content="",embed=embed)

while True:
    try :
        bot.run(token, bot=False)
    except:
        clear()
        input("Le token est invalide :/")
        quit()
