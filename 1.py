import random

from pip._vendor.distlib.compat import raw_input

carmen = raw_input("Erecribe el nombre del jugador 1: ")
primer_dado = random.randint(1,6)
segundo_dado = random.randint(1,6)
print (carmen + " has sacado un " + str(primer_dado) + " y un " + str(segundo_dado))
carmen_dados = primer_dado + segundo_dado

david = raw_input("Escribe el nombre del jugador 2: ")
primer_dado = random.randint(1,6)
segundo_dado = random.randint(1,6)
print (david + " has sacado un " + str(primer_dado) + " y un " + str(segundo_dado))
user2_dados = primer_dado + segundo_dado

if carmen_dados > user2_dados:
    print ("Has ganado " + carmen)
elif carmen_dados == user2_dados:
    print ("Empate!")
else:
    print ("Has ganado " + david)