import pyfiglet
import time
import datetime
import pytz
from termcolor import colored
from PIL import Image
import pygame

pygame.init()

pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play(-1)

print(pyfiglet.figlet_format("BOT_FRIEND"))

print(colored("\nCargando bot, por favor espere...", "light_green"))

time.sleep(4)

while True:
    saludar = "\nHola, soy koner, un bot simple. Estoy en beta, lo que significa que algunos comandos pueden no funcionar. Puedes usar los siguientes comandos:\n\n/list: para ver la lista de comandos disponibles.\n/url: para obtener enlaces relacionados con música.\n/time: para conocer la hora local en una ubicación específica.\n/anime_url: para obtener enlaces relacionados con anime.\n/download: para obtener enlaces de descarga de anime, música y videos.\n/IA_web: para obtener enlaces relacionados con IA.\n/minecraft_download: para descargar la última versión de Minecraft para Android y PC.\n/guardar_credenciales: para guardar contraseñas y correos electrónicos en un archivo de texto.\n/whatsapp_links: para obtener enlaces de descarga de versiones modificadas de WhatsApp.\n/noticias_now: url sobre noticas de ultimas horas.\n\nEn caso de errores, contáctame en el número +59893495015.\n"
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
            /noticias_now
            /image_from_text
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
                timezone = pytz.timezone(ubicacion)
                hora_local = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
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
            Para PC: https://www.minecraft.net/es-es/download""","light_red"))
        elif comando == "/noticias_now":
            print(colored("""
                1. [BBC News](https://www.bbc.com/news)
2. [CNN](https://edition.cnn.com/)
3. [The New York Times](https://www.nytimes.com/)
4. [The Guardian](https://www.theguardian.com/international)
5. [Al Jazeera](https://www.aljazeera.com/)
6. [Reuters](https://www.reuters.com/)
7. [Associated Press (AP) News](https://apnews.com/)
8. [BBC Mundo (para noticias en español)](https://www.bbc.com/mundo)
9. [El País](https://elpais.com/)
10. [CNN en Español](https://cnnespanol.cnn.com/""", "light_cyan"))
        elif comando == "/image_from_text":
            texto = input("ingrese el texto para generar la imagen:")
            img = Image.new('RGB', (100, 30), color = (255, 255, 255))
            img.save('imagen_generada.png')
            print('imagen creada con exito !! ')