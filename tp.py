a = float(input("Entrez le premier nombre : "))
op = input("Choisissez (+, -, *, /) : ")
b = float(input("Entrez le deuxième nombre : "))

if op == "+":
    print("Résultat :", a + b)
elif op == "-":
    print("Résultat :", a - b)
elif op == "*":
    print("Résultat :", a * b)
elif op == "/":
    if b != 0:
        print("Résultat :", a / b)
    else:
        print("Erreur : division par zéro !")
else:
    print("Opération invalide !")