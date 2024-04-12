import bruteforce
import optimised


def main():
    """"""
    algo = "0"
    while algo != "4":
        print("------------------------------------------------------")
        print("                   AlgoInvestTrade                    ")
        print("------------------------------------------------------")
        print("1:Brute_Force     2:Dynamique     3:Exit")
        algo = input("Entrez votre choix et appuyez sur entrée:      ")
        print("------------------------------------------------------")
        if algo == "1":
            print("Vous avez choisi le programme Brute force")
            bruteforce.main()
        elif algo == "2":
            print("Vous avez choisi le programme Dynamique")
            optimised.main()
        elif algo == "3":
            exit


if __name__ == "__main__":
    """"""
    main()
