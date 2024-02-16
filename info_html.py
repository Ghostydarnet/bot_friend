def generar_pagina_html():
    # Contenido HTML básico con CSS para el fondo
    contenido_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Información sobre el Bot</title>
        <style>
            body {
                background-image: url('bot_background.jpg'); /* Ruta de la imagen de fondo */
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
            .container {
                max-width: 800px;
                margin: auto;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.7); /* Color de fondo con transparencia */
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); /* Sombra */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Información sobre el Bot</h1>
            <p>Este es un bot simple creado con Python.</p>
            <h2>Actualizaciones Recientes</h2>
            <ul>
                <li>Versión 1.0 - Fecha: 2024-02-15: Implementación inicial del bot.</li>
                <li>Versión 1.1 - Fecha: 2024-02-20: Agregado comando /info_html para generar una página web básica.</li>
                <li>Versión 1.2 - Fecha: 2024-02-25: Agregado comando /up_server para iniciar un servidor web.</li>
            </ul>
        </div>
    </body>
    </html>
    """

    # Guardar el contenido HTML en un archivo
    with open("informacion_bot.html", "w") as archivo:
        archivo.write(contenido_html)

# Ejecutar la función al recibir el comando
generar_pagina_html()