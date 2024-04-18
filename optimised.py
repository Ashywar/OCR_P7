import csv
import time
import psutil
import os
from tqdm import tqdm


class Action:
    """Create the Action object"""

    def __init__(self, name, price, profit):
        self.name = name
        self.price = int(round(float(price) * 100))  # Convert euros to cents
        self.profit = int(round(float(profit) * 100))  # Convert euros to cents
        self.gain = int(
            ((self.price * self.profit) / 100) * 100
        )  # Calculate gain in cents

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Profit: {self.profit}, Gain: {self.gain}"


def read_csv_data(datafile):
    """Open and read the csv file to create a list of Action objects"""
    actions = []
    with open(f"data_set/{datafile}.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if float(row[1]) <= 0.0 or float(row[2]) <= 0.0:
                del row
            else:
                actions.append(Action(row[0], row[1], row[2]))
    return actions


def create_empty_matrix(actions, max_investment):
    """Generate an empty matrix"""
    matrix = []
    for _ in range(len(actions) + 1):
        row = [0] * (max_investment + 1)
        matrix.append(row)
    return matrix


def dynamic_programming_algorithm(actions, max_investment):
    """Fill the empty matrix with the best possible gain"""
    matrix = create_empty_matrix(actions, max_investment)

    for i in tqdm(range(1, len(actions) + 1), desc="Progress"):
        for j in range(1, max_investment + 1):
            if actions[i - 1].price <= j:
                best_pos = actions[i - 1].gain + matrix[i - 1][j - actions[i - 1].price]
                matrix[i][j] = max(best_pos, matrix[i - 1][j])
            else:
                matrix[i][j] = matrix[i - 1][j]
    return matrix


def find_best_portfolio(actions, max_investment, matrix):
    """Search for the best optimized action solution in the matrix"""
    invest = max_investment
    actions_index = len(actions)
    best_portfolio = []

    while invest >= 0 and actions_index >= 0:
        current_action = actions[actions_index - 1]
        if (
            matrix[actions_index][invest]
            == matrix[actions_index - 1][invest - current_action.price]
            + current_action.gain
        ):
            best_portfolio.append(current_action)
            invest -= current_action.price

        actions_index -= 1

    return best_portfolio


def display_solution(best_portfolio):
    """Display the optimized result"""
    action_names = []
    total_gain = 0
    total_investment = 0

    for action in best_portfolio:
        total_gain += action.gain
        total_investment += action.price
        action_names.append(action.name)

    return (
        f"La meilleure combinaison d'action est: {action_names}\n\n"
        f"Pour un gain estimé de: {total_gain/1000000} €\n\n"
        f"Pour un investissement de:{total_investment/100} €\n"
    )


def main():
    """"""

    print("----------------------------------------------")
    print("             Programme Dynamique             ")
    print("----------------------------------------------")
    print("1:dataset 0   2:dataset 1   3:dataset 2")

    algo = input("Entrez votre choix et appuyez sur entrée: ")
    if algo == "1":
        csv_file = "dataset0"
    elif algo == "2":
        csv_file = "dataset1"
    elif algo == "3":
        csv_file = "dataset2"

    process = psutil.Process(os.getpid())
    max_investment = 50000  # Conversion from euros to cents *100
    actions = read_csv_data(csv_file)
    start_time = time.time()
    matrix = dynamic_programming_algorithm(actions, max_investment)
    best_portfolio = find_best_portfolio(actions, max_investment, matrix)
    solution = display_solution(best_portfolio)
    print(solution)
    end_time = time.time()
    print("Temps d'execution:", (end_time - start_time), "secodes")
    print("Memoire utilisée ", str(process.memory_info().rss), " bytes")


if __name__ == "__main__":
    main()
