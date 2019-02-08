import random

print("PIEDRA, PAPEL , ... ¡TIJERA!")
opcion = random.choice(['Piedra','Papel','Tijera'])
opcion1 = random.choice(['Piedra','Papel','Tijera'])
print("Ines ha elegido "+opcion)
print("Juan ha elegido " + opcion1)
if opcion == "Piedra" and opcion1 == "Piedra":
    print("Empate.")
elif opcion == "Piedra" and opcion1 == "Papel":
    print("Juan Gana.")
elif opcion == "Piedra" and opcion1 == "Tijera":
    print("Ines Gana.")
elif opcion == "Papel" and opcion1 == "Tijera":
    print("Juan Gana.")
elif opcion == "Papel" and opcion1 == "Papel":
    print("Empate.")
elif opcion == "Papel" and opcion1 == "Piedra":
    print("Ines Gana.")
elif opcion == "Tijera" and opcion1 == "Tijera":
    print("Empate.")
elif opcion == "Tijera" and opcion1 == "Papel":
    print("Ines gana.")
elif opcion == "Tijera" and opcion1 == "Piedra":
    print("Juan Gana.")