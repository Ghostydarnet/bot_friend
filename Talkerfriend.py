import pyfiglet
import time
import datetime
import platform
import pygame
import pytz
from termcolor import colored
import os


pygame.init()


pygame.mixer.music.load("X2Download.app - Ark Patrol - Let Go (ft. Veronika Redd) [Heroic] (128 kbps).mp3")
pygame.mixer.music.play(-1)


print(pyfiglet.figlet_format("BOT_FRIEND"))

print(colored("\nCargando bot, por favor espere...", "light_green"))

time.sleep(4)

while True:
    saludar = "\nHola, soy koner, un bot simple. Estoy en beta, lo que significa que algunos comandos pueden no funcionar. Puedes usar los siguientes comandos:\n\n/list: para ver la lista de comandos disponibles.\n/url: para obtener enlaces relacionados con música.\n/time: para conocer la hora local en una ubicación específica.\n/anime_url: para obtener enlaces relacionados con anime.\n/download: para obtener enlaces de descarga de anime, música y videos.\n/IA_web: para obtener enlaces relacionados con IA.\n/minecraft_download: para descargar la última versión de Minecraft para Android y PC.\n/whatsapp_links: para obtener enlaces de descarga de versiones modificadas de WhatsApp.\n/series_links: para obtener enlaces de descarga de aplicaciones para ver series gratis.\n/tools: para obtener enlaces de herramientas como Pydroid y Termux.\n/infersys: para obtener información sobre el dispositivo en uso.\n/generar_contraseña: Genera mas de 800  mil contraseña.\n/key_windows: llaves funcionales  para poder hacer funcionar el windos.\n/up_server: un servidor simple con python\n/info_html: codigo HTML sobre el bot.\nEn caso de errores, contáctame en el IG: botf_riend\n"
    print(saludar)

    while True:
        comando = input("Coloque el comando aquí: ").lower()
        if comando == "/list":
            print(colored("""
            Comandos
            /info_html
            /key_windows
            /up_server
            /generar_contraseña
            /url
            /time
            /anime_url
            /download
            /IA_web
            /minecraft_download
            /guardar_credenciales
            /whatsapp_links
            /series_links
            /tools
            /infersys
            /help
            """, "light_red"))
        elif comando == "/help":
            print(saludar)
        elif comando == "/url":
            print(colored("""
            1. Spotify - https://www.spotify.com/
            2. Apple Music - https://www.apple.com/apple-music/
            3. YouTube Music - https://music.youtube.com/
            4. SoundCloud - https://soundcloud.com/
            5. Bandcamp - https://bandcamp.com/
            6. Deezer - https://www.deezer.com/
            7. Tidal - https://tidal.com/
            8. Pandora - https://www.pandora.com/
            9. Amazon Music - https://music.amazon.com/
            10. Google Play Music (ahora YouTube Music) - https://music.youtube.com/""", "light_green"))
        elif comando == "/time":
            ubicacion = input("Ingrese su ubicación para conocer la hora (ej. 'America/Montevideo'): ")
            try:
                hora_local = datetime.datetime.now(datetime.timezone.utc).astimezone(pytz.timezone(ubicacion)).strftime("%Y-%m-%d %H:%M:%S")
                print(f"Hora local en {ubicacion}: {hora_local}")
            except pytz.exceptions.UnknownTimeZoneError:
                print("Ubicación no válida.")
        elif comando == "/anime_url":
            print(colored("""
            1. Crunchyroll - https://www.crunchyroll.com/
            2. Funimation - https://www.funimation.com/
            3. Netflix - https://www.netflix.com/
            4. Hulu - https://www.hulu.com/
            5. Amazon Prime Video - https://www.amazon.com/Prime-Video/
            """, "light_blue"))
        elif comando == "/download":
            print(colored("""
            1. Nyaa - https://nyaa.si/
            2. HorribleSubs - https://horriblesubs.info/
            3. AniDL - https://anidl.org/
            4. 9anime - https://9anime.to/
            5. The Pirate Bay - https://thepiratebay.org/
            6. YTS - https://yts.mx/
            7. 1337x - https://1337x.to/
            8. Internet Archive - https://archive.org/
            """, "yellow"))
        elif comando == "/ia_web":
            print(colored("""
            1. OpenAI - https://openai.com/
            2. DeepMind - https://deepmind.com/
            3. IBM Watson - https://www.ibm.com/watson
            4. Microsoft Azure AI - https://azure.microsoft.com/en-us/services/cognitive-services/
            5. Google AI - https://ai.google/
            """, "magenta"))
        elif comando == "/minecraft_download":
            print(colored("""
            Para Android: https://play.google.com/store/apps/details?id=com.mojang.minecraftpe
            Para PC: https://www.minecraft.net/es-es/download""", "cyan"))
        elif comando == "/guardar_credenciales":
            correo = input("Ingrese su correo electrónico: ")
            contrasena = input("Ingrese su contraseña: ")
            try:
                with open("credenciales.txt", "a") as archivo:
                    archivo.write(f"Correo: {correo}, Contraseña: {contrasena}\n")
                    print("Credenciales guardadas correctamente.")
            except Exception as e:
                print(f"Error al guardar las credenciales: {str(e)}")
        elif comando == "/whatsapp_links":
            print(colored("""
            WhatsApp Plus (Android): https://whatsapp-plus.uptodown.com/android
            WhatsApp Aero (Android): https://whatsaero.com/download/
            WhatsApp GB (Android): https://gbapps.net/whatsapp-plus-apk/
            """, "blue"))
        elif comando == "/series_links":
            print(colored("""
            Aplicaciones para ver series gratis:
            1. Popcorn Time: https://popcorntime.app/
            2. Stremio: https://www.stremio.com/
            3. TeaTV: https://teatv.net/
            """, "cyan"))
        elif comando == "/tools":
            print(colored("""
            Herramientas:
            1. Pydroid - IDE para Python en dispositivos Android: https://play.google.com/store/apps/details?id=ru.iiec.pydroid3
            2. Termux - Emulador de terminal para Android: https://play.google.com/store/apps/details?id=com.termux
            """, "green"))
        elif comando == "/infersys":
         print(colored(f"""
    Información del sistema:
    - Sistema operativo: {platform.system()}
    - Versión: {platform.version()}
    - Arquitectura: {platform.architecture()}
    - Nombre del equipo: {platform.node()}
    - Procesador: {platform.processor()}
    """, "cyan"))
        elif comando == "/generar_contraseña":
            os.system("python3 passwordh4.py")
        elif comando == "/up_server":
            os.system("python3 server.py")
        elif comando == "/info_html":
            os.system("python3 info_html.py")
        elif comando == "/key_windows":
            print(colored(
                """\nWindows 10 Home:

TX9XD-98N7V-6WMQ6-BX7FG-H8Q99

KTNPV-KTRK4-3RRR8-39X6W-W44T3

YTMG3-N6DKC-DKB77-7M9GH-8HVX7

4CPRK-NM3K3-X6XXQ-RXX86-WXCHW

AKJUS-WY2CT-JWBJ2-T68TQ-YBH2V

BT79Q-G7N6G-PGBYW-4YWX6-6F4BT

Windows 10 Pro:

VK7JG-NPHTM-C97JM-9MPGT-3V66T

8N67H-M3CY9-QT7C4-2TR7M-TXYCV

2B87N-8KFHP-DKV6R-Y2C8J-PKCKT

DXG7C-N36C4-C4HTG-X4T3X-2YV77

WYPNQ-8C467-V2W6J-TX4WX-WT2RQ

AKSIU-WY2CT-JWBJ2-T68TQ-YBH2V

AJUYS-8C467-V2W6J-TX4WX-WT2RQ

Windows 10 Home Single Language:

7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH

NKJFK-GPHP7-G8C3J-P6JXR-HQRJR

Windows 10 Enterprise:

NPPR9-FWDCX-D2C8J-H872K-2YT43

CKFK9-QNGF2-D34FM-99QX2-8XC4K

DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4

WNMTR-4C88C-JK8YV-HQ7T2-76DF9

2F77B-TNFGY-69QQF-B8YKP-D69TJ

XGVPP-NMH47-7TTHJ-W3FW7-8HV2C

RW7WN-FMT44-KRGBK-G44WK-QV7YK

FW7NV-4T673-HF4VX-9X4MM-B4H4T

WGGHN-J84D6-QYCPR-T7PJ7-X766F

NK96Y-D9CD8-W44CQ-R8YTK-DYJWX

JAHSU-QMPVW-D7KKK-3GKT6-VCFB2

SJUY7-NFMTC-H88MJ-PFHPY-QJ4BJ

AJSU7-GRT3P-VKWWX-X7T3R-8B639

ALSOI-MHBT6-FXBX8-QWJK7-DRR8H

8UY76-TNFGY-69QQF-B8YKP-D69TJ

AJSUY-NPHTM-C97JM-9MPGT-3V66T

ALSOI-4C88C-JK8YV-HQ7T2-76DF9

Windows 10 Education:

NW6C2-QMPVW-D7KKK-3GKT6-VCFB2

2WH4N-8QGBV-H22JP-CT43Q-MDWWJ

YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY

6TP4R-GNPTD-KYYHQ-7B7DP-J447Y

84NGF-MHBT6-FXBX8-QWJK7-DRR8H

8PTT6-RNW4C-6V7J2-C2D3X-MHBPB

GJTYN-HDMQY-FRR76-HVGC7-QPF8P

YVWGF-BXNMC-HTQYQ-CPQ99-66QFC

Windows 10 S:

3NF4D-GF9GY-63VKH-QRC3V-7QW8P\n""","light_red"))
    