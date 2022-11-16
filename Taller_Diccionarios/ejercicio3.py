usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

for i in range(1,4):
    usuario = input("Escriba su usuario: ")
    clave = input("Escriba su password: ")
    if usuario in usuarios and clave == usuarios[usuario]['password']:
        print("Bienvenido", usuarios[usuario]['nombre'], usuarios[usuario]['apellido'])
    else:
        print("Usuario y/o clave no identificado, intente de nuevo")