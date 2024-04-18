import csv
import time
import psutil
import os
from itertools import combinations
from tqdm import tqdm


def make_dict(data_file):
    """Create a dictionary with the data from a CSV file."""
    stocks = {}
    with open(f"data_set/{data_file}.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            stocks[row[0]] = [float(row[1]), float(row[2])]
    return stocks


def find_best_investment(max_investment, stocks):
    """
    Find the best combination of investments from the stocks to maximize gain.

    Args:
        max_investment (float): The maximum amount available for investment.
        stocks (dict): A dictionary containing investment options.
                       Each entry is of the form: {investment_name: [price, two_year_gain]}

    Returns:
        tuple: A tuple containing the best investment combination, maximum gain, and total investment.
    """
    max_gain = 0  # Initialize the maximum gain
    total_investment = 0  # Initialize the total investment amount
    best_investment = []  # Initialize the best investment combination

    # Iterate through different numbers of investments to consider (from 0 to len(stocks))
    for i in tqdm(range(len(stocks) + 1), desc="Progress"):
        # Generate all possible combinations of investments for the current number (i)
        for combos in combinations(stocks, i):
            combo_gain = 0  # Initialize gain for the current combination
            total_investment_amount = (
                0  # Initialize total investment for the current combination
            )

            # Calculate gain and total investment for each investment in the combination
            for combo in combos:
                price = stocks[combo][0]
                two_year_gain = stocks[combo][1]
                action_gain = (price * two_year_gain) / 100
                combo_gain += action_gain
                total_investment_amount += price

            # Check if the total investment is within the limit and gain is higher
            if total_investment_amount <= max_investment and combo_gain > max_gain:
                max_gain = combo_gain
                total_investment = total_investment_amount
                best_investment = combos
            else:
                pass
    return (
        f"La meilleure combinaison d'action est: {best_investment} \n\n"
        f"Pour un gain estimé de: {max_gain} € \n\n"
        f"Pour un investissement de: {total_investment} € \n"
    )


def main():
    """Main function"""
    print("----------------------------------------------")
    print("             Programme Force Brute             ")
    print("----------------------------------------------")
    print("1: Dataset 0   2: Dataset 1   3: Dataset 2")

    # Get user's choice of dataset
    choice = input("Entrez votre choix et appuyez sur entrée: \n")
    if choice == "1":
        csv_file = "dataset0"  # Update with the actual file name for Dataset 0
    elif choice == "2":
        csv_file = "dataset1"  # Update with the actual file name for Dataset 1
    elif choice == "3":
        csv_file = "dataset2"  # Update with the actual file name for Dataset 2
    else:
        print("Invalid choice")
        return

    process = psutil.Process(os.getpid())
    max_investment = 500
    start_time = time.time()

    # make_dict function to read the CSV and return a stocks dictionary
    stocks = make_dict(csv_file)

    best_investment = find_best_investment(max_investment, stocks)

    print(best_investment, " \n")
    end_time = time.time()
    print("Temps d'execution:", (end_time - start_time), "secondes")
    print("Memoire utilisée ", str(process.memory_info().rss), " bytes")


if __name__ == "__main__":
    main()
