import sys

from pip._vendor.distlib.compat import raw_input

count =1
user1 = raw_input("Eres el primer jugador, escribe tu nombre --> ")
user1_option = input("Escribe el numero de la opcion que quieras elegir" + '\n'  +
               "1 - Piedra" + '\n'  + "2 - Papel" +'\n'  + "3 - Tijera"  +  '\n'+ "4 - Lagarto"  +  '\n'+ "5 - Spock"  +  '\n'+ "--> " )
while user1_option > 5  and count < 3:
    user1_option = input("otra vez,"
                   "recuerda del 1 al 5 si escribes otro numero diferente no sirve " + '\n' +
                   "1 - Piedra" + '\n' + "2 - Papel" + '\n' + "3 - Tijera" +  '\n'+ "4 - Lagarto"  +  '\n'+ "5 - Spock"  +  '\n'+ "--> ")
    count = count + 1
    if count > 2:
        print (
            "Si escribir un numero del 1 al 5 es tan dificil para ti apaga el ordenador y vete a tomar el aire un poco ")
        sys.exit()

count = 1
user2 = raw_input("Eres el segundo jugador, escribe tu nombre --> ")
user2_option = input("Escribe el numero de la opcion que quieras elegir" + '\n'  +
               "1 - Piedra" + '\n'  + "2 - Papel" +'\n'  + "3 - Tijera"  +  '\n'+ "4 - Lagarto"  +  '\n'+ "5 - Spock"  +  '\n'+ "--> " )
while user2_option > 5 and count < 3:
    user2_option = input("otra vez,"
                   "recuerda del 1 al 5 si escribes otro numero diferente no sirve " + '\n' +
                   "1 - Piedra" + '\n' + "2 - Papel" + '\n' + "3 - Tijera" +  '\n'+ "4 - Lagarto"  +  '\n'+ "5 - Spock"  +  '\n'+ "--> ")
    if count > 2:
        print (
            "Si escribir un numero del 1 al 5 es tan dificil para ti apaga el ordenador y vete a tomar el aire un poco ")
        sys.exit()

#1 = piedra
#2 = papel
#3 = tijera
#4 = lagarto
#5 = spock

if user1_option == 1 and user2_option == 3:
    print ("Ha ganado " + user1)
    sys.exit()
elif user1_option == 1 and user2_option == 2:
    print ("Ha ganado " + user2)
    sys.exit()
elif user1_option == 1 and user2_option == 4:
    print ("Ha ganado " + user2)
    sys.exit()
elif user1_option == 1 and user2_option == 5:
    print ("Ha ganado " + user1)
    sys.exit()




elif user1_option == 2 and user2_option == 1:
    print ("Ha ganado " + user1)
    sys.exit()
elif user1_option == 2 and user2_option == 3:
    print ("Ha ganado " + user2)
    sys.exit()
elif user1_option == 2 and user2_option == 4:
    print ("Ha ganado " + user1)
    sys.exit()
elif user1_option == 2 and user2_option == 5:
    print ("Ha ganado " + user2)
    sys.exit()





elif user1_option == 3 and user2_option == 1:
    print ("Ha ganado " + user2)
    sys.exit()
elif user1_option == 3 and user2_option == 2:
    print ("Ha ganado " + user1)
    sys.exit()
elif user1_option == 3 and user2_option == 4:
    print ("Ha ganado " + user2)
    sys.exit()
elif user1_option == 3 and user2_option == 5:
    print ("Ha ganado " + user1)
    sys.exit()

elif user1_option == 4 and user2_option == 1:
    print ("Ha ganado " + user1)
    sys.exit()
elif user1_option == 4 and user2_option == 2:
    print ("Ha ganado " + user2)
    sys.exit()
elif user1_option == 4 and user2_option == 3:
    print ("Ha ganado " + user1)
    sys.exit()
elif user1_option == 4 and user2_option == 5:
    print ("Ha ganado " + user2)
    sys.exit()

elif user1_option == 5 and user2_option == 1:
    print ("Ha ganado " + user2)
    sys.exit()
elif user1_option == 5 and user2_option == 2:
    print ("Ha ganado " + user1)
    sys.exit()
elif user1_option == 5 and user2_option == 3:
    print ("Ha ganado " + user2)
    sys.exit()
elif user1_option == 5 and user2_option == 4:
    print ("Ha ganado " + user1)
    sys.exit()


# Casos de empate
elif user1_option == 1 and user2_option == 1:
    print ("empate!")
    sys.exit()
elif user1_option == 2 and user2_option == 2:
    print ("empate!")
    sys.exit()
elif user1_option == 3 and user2_option == 3:
    print ("empate!")
    sys.exit()
elif user1_option == 4 and user2_option == 4:
    print ("empate!")
    sys.exit()
elif user1_option == 5 and user2_option == 5:
    print ("empate!")
    sys.exit()