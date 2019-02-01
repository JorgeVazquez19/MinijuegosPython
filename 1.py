import random

from pip._vendor.distlib.compat import raw_input

user1 = raw_input("Eres el primer jugador, escribe tu nombre para lanzar los dados --> ")
primer_dado = random.randint(1,6)
segundo_dado = random.randint(1,6)
print (user1 + " has sacado un " + str(primer_dado) + " y un " + str(segundo_dado))
user1_dados = primer_dado + segundo_dado

user2 = raw_input("Eres el segundo jugador, escribe tu nombre para lanzar los dados --> ")
primer_dado = random.randint(1,6)
segundo_dado = random.randint(1,6)
print (user2 + " has sacado un " + str(primer_dado) + " y un " + str(segundo_dado))
user2_dados = primer_dado + segundo_dado

if user1_dados > user2_dados:
    print ("Has ganado " + user1)
elif user1_dados == user2_dados:
    print ("Empate!")
else:
    print ("Has ganado " + user2)