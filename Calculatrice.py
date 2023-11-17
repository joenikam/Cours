
def calculatrice():
    print("Bienvenue dans la calculatrice en Python !")
    print("Veuillez entrer deux nombres :")
    nombre1 = float(input("Premier nombre : "))
    nombre2 = float(input("Deuxième nombre : "))
    
    print("Sélectionnez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    
    choix = int(input("Votre choix (1/2/3/4) : "))
    
    if choix == 1:
        resultat = nombre1 + nombre2
        print("Le résultat de l'addition est :", resultat)
    elif choix == 2:
        resultat = nombre1 - nombre2
        print("Le résultat de la soustraction est :", resultat)
    elif choix == 3:
        resultat = nombre1 * nombre2
        print("Le résultat de la multiplication est :", resultat)
    elif choix == 4:
        if nombre2 == 0:
            print("Erreur : division par zéro !")
        else:
            resultat = nombre1 / nombre2
            print("Le résultat de la division est :", resultat)
    else:
        print("Choix invalide !")
    
    print("Merci d'avoir utilisé la calculatrice en Python. À bientôt !")

calculatrice()