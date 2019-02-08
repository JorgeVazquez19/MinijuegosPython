import random
import sys

from pip._vendor.distlib.compat import raw_input

user1 = raw_input("Escribe el nombre del jugador 1")
primera_carta = random.randint(1,10)
segunda_carta = random.randint(1,10)
tercera_carta = random.randint(1,10)
print (user1 + " has sacado un " + str(primera_carta) + ",un " + str(segunda_carta) +  ",y un " + str(segunda_carta))
user1_cartas = primera_carta + segunda_carta + tercera_carta

user2 = raw_input("Escribe el nombre del jugador 2: ")
primera_carta = random.randint(1,10)
segunda_carta = random.randint(1,10)
tercera_carta = random.randint(1,10)
print (user2 + " has sacado un " + str(primera_carta) + ",un " + str(segunda_carta) +  ",y un " + str(segunda_carta))
user2_cartas = primera_carta + segunda_carta + tercera_carta

if user1_cartas > 15 and user2_cartas > 15:
    print ("Los dos habeis perdido")
    sys.exit()
elif user1_cartas > 15 and user2_cartas < 15:
    print ("Has ganado " + user2)
    sys.exit()
elif user1_cartas < 15 and user2_cartas > 15:
    print ("Has ganado " + user1)
    sys.exit()
elif user1_cartas >  user2_cartas:
    print ("Has ganado " + user1)
    sys.exit()
else:
    print ("Has ganado " + user2)