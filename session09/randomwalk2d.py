import numpy as np
import matplotlib.pyplot as plt
import time

def random_walk_2d_step(x, y):
    step = np.random.choice(['up', 'down', 'left', 'right'])

    if step == 'up':
        y += 1
    elif step == 'down':
        y -= 1
    elif step == 'left':
        x -= 1
    elif step == 'right':
        x += 1

    return x, y

def plot_random_walk_2d_realtime(n_steps, seed=None, sleep_time=0.3):
    if seed is not None:
        np.random.seed(seed)

    x_positions = [0]
    y_positions = [0]

    plt.ion()  # Enable interactive mode
    plt.title("2D Random Walk")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    # Set fixed axis limits
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Add "Start" text at the starting point
    plt.text(x_positions[0], y_positions[0], "Start", fontsize=12, color='red')

    for i in range(n_steps):
        x, y = random_walk_2d_step(x_positions[-1], y_positions[-1])
        x_positions.append(x)
        y_positions.append(y)

        plt.plot(x_positions[-2:], y_positions[-2:], marker='o', markersize=5, linestyle='-')
        plt.draw()
        plt.pause(sleep_time)

    # Add "Finish" text at the ending point
    plt.text(x_positions[-1], y_positions[-1], "Finish", fontsize=12, color='green')

    plt.ioff()  # Disable interactive mode
    plt.show()

# Parameters
n_steps = 50
seed = 42

# Simulate and plot the 2D random walk in real-time
plot_random_walk_2d_realtime(n_steps)
