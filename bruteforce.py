import csv
import time
import psutil
import os
from itertools import combinations


def make_dict(datafile):
    """Create a dictionary with the data of a csv file"""
    stocks_dict = {}
    with open(f"data_set/{datafile}.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            stocks_dict.update({row[0]: [row[1], row[2]]})
    return stocks_dict


def find_best_invest(max_invest, stocks):
    """
    Find the best combination of investments from the stocks to maximize gain.

    Args:
        max_invest (float): The maximum amount available for investment.
        stocks (dict): A dictionary containing investment options.
                       Each entry is of the form: {investment_name: [price, two_year_gain]}

    Returns:
        tuple: A tuple containing the best investment combination, maximum gain, and total investment.
    """
    max_gain = 0  # Initialize the maximum gain
    all_invest = 0  # Initialize the total investment amount
    best_invest = []  # Initialize the best investment combination

    # Iterate through different numbers of investments to consider (from 0 to len(stocks))
    for i in range(len(stocks) + 1):
        # Generate all possible combinations of investments for the current number (i)
        for combis in combinations(stocks, i):
            combi_gain = 0  # Initialize gain for the current combination
            total_invest = 0  # Initialize total investment for the current combination

            # Calculate gain and total investment for each investment in the combination
            for combi in combis:
                # print(combi)
                action_price = float(stocks[combi][0])
                two_year_gain = float(stocks[combi][1])
                action_gain = (action_price * two_year_gain) / 100
                combi_gain += action_gain
                total_invest += action_price

            # Check if the total investment is within the limit and gain is higher
            if total_invest <= max_invest and combi_gain > max_gain:
                max_gain = combi_gain
                all_invest = total_invest
                best_invest = combis
            else:
                pass
    return (
        f"La meilleure combinaison d'action est: {best_invest} \n\n"
        f"Pour un gain estimé de: {max_gain} € \n\n"
        f"Pour un investissement de: {all_invest} € \n"
    )


def main():
    """Principal function"""
    print("----------------------------------------------")
    print("             Programme Force Brute             ")
    print("----------------------------------------------")
    print("1: Dataset 0   2: Dataset 1   3: Dataset 2")

    # Get user's choice of dataset
    algo = input("Entrez votre choix et appuyez sur entrée: \n")
    if algo == "1":
        csv_file = "dataset0"  # Update with the actual file name for Dataset 0
    elif algo == "2":
        csv_file = "dataset1"  # Update with the actual file name for Dataset 1
    elif algo == "3":
        csv_file = "dataset2"  # Update with the actual file name for Dataset 2
    else:
        print("Invalid choice")
        return

    process = psutil.Process(os.getpid())
    max_invest = 500
    start_time = time.time()

    # make_dict function to read the CSV and return a stocks dictionary
    stocks = make_dict(csv_file)

    best_invest = find_best_invest(max_invest, stocks)

    print(best_invest, " \n")
    end_time = time.time()
    print("Temps d'execution:", (end_time - start_time), "secondes")
    print("Memoire utilisée ", str(process.memory_info().rss), " bytes")


if __name__ == "__main__":
    main()
