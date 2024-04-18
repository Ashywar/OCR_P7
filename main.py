import bruteforce
import optimised
import sys


def main():
    """
    Displays a menu for choosing between different investment trading algorithms.
    """
    while True:
        print("------------------------------------------------------")
        print("                   AlgoInvestTrade                    ")
        print("------------------------------------------------------")
        print("1: Force Brute     2: Dynamique     3: Quitter")
        choix = input("Entrez votre choix et appuyez sur entrée : ")
        print("------------------------------------------------------")

        if choix == "1":
            print("Vous avez choisi le programme Force Brute")
            bruteforce.main()
        elif choix == "2":
            print("Vous avez choisi le programme Dynamique")
            optimised.main()
        elif choix == "3":
            print("Fermeture d'AlgoInvestTrade. Au revoir !")
            sys.exit()
        else:
            print("Choix invalide. Veuillez entrer une option valide (1, 2 ou 3).")


if __name__ == "__main__":
    main()
