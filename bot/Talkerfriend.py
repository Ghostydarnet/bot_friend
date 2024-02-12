import pyfiglet
import time
import datetime
import platform
import pygame
import pytz
from termcolor import colored


pygame.init()


pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play(-1)


print(pyfiglet.figlet_format("BOT_FRIEND"))

print(colored("\nCargando bot, por favor espere...", "light_green"))

time.sleep(4)

while True:
    saludar = "\nHola, soy koner, un bot simple. Estoy en beta, lo que significa que algunos comandos pueden no funcionar. Puedes usar los siguientes comandos:\n\n/list: para ver la lista de comandos disponibles.\n/url: para obtener enlaces relacionados con música.\n/time: para conocer la hora local en una ubicación específica.\n/anime_url: para obtener enlaces relacionados con anime.\n/download: para obtener enlaces de descarga de anime, música y videos.\n/IA_web: para obtener enlaces relacionados con IA.\n/minecraft_download: para descargar la última versión de Minecraft para Android y PC.\n/whatsapp_links: para obtener enlaces de descarga de versiones modificadas de WhatsApp.\n/series_links: para obtener enlaces de descarga de aplicaciones para ver series gratis.\n/tools: para obtener enlaces de herramientas como Pydroid y Termux.\n/infersys: para obtener información sobre el dispositivo en uso.\nS\nEn caso de errores, contáctame en el IG: botf_riend\n"
    print(saludar)

    while True:
        comando = input("Coloque el comando aquí: ").lower()
        if comando == "/list":
            print(colored("""
            Comandos
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
       