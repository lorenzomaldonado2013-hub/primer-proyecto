import random
character ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ask = int(input("poner la longitud de la contrasena"))
contrasena =""
for i in range(ask):
    contrasena+=random.choice(character)
    print("la contrasena es:",contrasena)