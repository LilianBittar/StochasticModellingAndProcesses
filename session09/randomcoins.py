import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import scipy.stats as stats
import time

def simulate_coin_tosses(n_flips, n_trials, seed=None, sleep_time = 1):
    if seed is not None:
        np.random.seed(seed)

    # Simulate coin tosses for each trial
    coin_tosses = np.random.choice([-1, 1], size=(n_trials, n_flips))

    # Calculate the sum of coin tosses for each trial
    coin_sums = np.sum(coin_tosses, axis=1)

    return coin_sums

def plot_frequency(max_n_flips, n_trials, seed=None, sleep_time=10**-10):
    for n_flips in range(1, max_n_flips + 1):
        # Simulate coin tosses and calculate sums
        coin_sums = simulate_coin_tosses(n_flips, n_trials, seed)

        # Calculate the frequencies of each sum
        frequencies = Counter(coin_sums)

        # Calculate the probabilities
        probabilities = {k: v / n_trials for k, v in frequencies.items()}

        # Create the bar plot
        plt.bar(probabilities.keys(), probabilities.values(), alpha=0.75)
        plt.title(f"Frequency Plot of Coin Tosses Sum with Normal Distribution (n_flips = {n_flips})")
        plt.xlabel("Sum")
        plt.ylabel("Probability")
        plt.grid(True)

        # Calculate the mean and standard deviation of coin_sums
        mean = np.mean(coin_sums)
        std_dev = np.std(coin_sums)

        # Generate x values for the normal distribution
        x = np.linspace(min(coin_sums), max(coin_sums), 100)

        # Calculate the normal distribution probability density function (PDF) values
        y = stats.norm.pdf(x, mean, std_dev)

        # Plot the smooth normal distribution
        plt.plot(x, y, 'r', linewidth=2)

        # Set x-axis ticks and limits
        #plt.xticks(np.arange(-10, 11, step=1))
        #plt.xlim(-10, 10)

        # Show the plot and pause for a specified time
        plt.draw()
        plt.pause(sleep_time)

        # Clear the plot for the next iteration, but not after the last n
        if n_flips != max_n_flips:
            plt.clf()

    plt.show()

# Parameters
max_n_flips = int(input("Trials: "))
n_trials = 10000
seed = 42

# Plot the frequency plot of the coin tosses sum with normal distribution overlay in real-time
plot_frequency(max_n_flips = max_n_flips, n_trials = n_trials)
