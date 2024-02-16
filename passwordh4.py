import random 
import string 

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña


while True:
    longitud = input("Ingrese la longitud de la contraseña: ")
    try:
        longitud = int(longitud)
        break  
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")


for i in range(800000):
    print(f"Contraseña {i+1}: {generar_contraseña(longitud)}")