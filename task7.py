import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_rolls):

    results = {}
    for _ in range(num_rolls):
        roll_sum = roll_dice()
        results[roll_sum] = results.get(roll_sum, 0) + 1  
    return results

def calculate_probabilities(results, num_rolls):
    probabilities = {}
    for roll_sum, frequency in results.items():
        probabilities[roll_sum] = frequency / num_rolls
    return probabilities

def main():
    num_rolls = 100000  

    results = monte_carlo_simulation(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)

    print("Sum\tProbability (Monte Carlo)")
    print("-" * 35) 

    for roll_sum in sorted(probabilities.keys()):
        print(f"{roll_sum}\t{probabilities[roll_sum]:.4f}") 

    analytical_probabilities = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

    print("\nSum\tProbability (Analytical)")
    print("-" * 35)

    for roll_sum in sorted(analytical_probabilities.keys()):
        print(f"{roll_sum}\t{analytical_probabilities[roll_sum]:.4f}")


if __name__ == "__main__":
    main()  