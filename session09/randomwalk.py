import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output

def random_walk_1d_real_time(n_steps, seed=None, pause_time=0.01):
    if seed is not None:
        np.random.seed(seed)

    # Initialize the position
    position = 0

    # Create an empty plot
    plt.figure()
    plt.title("1D Random Walk")
    plt.xlabel("Steps")
    plt.ylabel("Position")

    # Initialize the position history for plotting lines
    position_history = [0]

    # Generate and plot each step
    for i in range(n_steps):
        # Generate a random step: -1 (left) or 1 (right)
        step = np.random.choice([-1, 1])

        # Update the position
        position += step

        # Update the position history
        position_history.append(position)

        # Update the plot
        plt.plot(position_history, c='b')
        plt.xlim(0, n_steps)
        plt.yticks(np.arange(-10, 11, step=1))
        plt.ylim(-10, 10)  # Set the y-axis limits to -10 and 10
        
        if i < n_steps - 1:  # Don't clear the output on the last step
            plt.pause(pause_time)
            clear_output(wait=True)
        else:
            # Print the absolute value of the y position at the end of n steps
            print(f"Absolute position at the end of {n_steps} steps: {abs(position)}")
            plt.pause(pause_time)
            clear_output(wait=True)

    plt.show()

# Parameters
n_steps = 100
pause_time = 0.01

# Simulate and visualize the random walk in real-time without a specific seed
random_walk_1d_real_time(n_steps, pause_time=pause_time)
