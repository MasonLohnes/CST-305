# ============================
# Reece Gerhart Mason Lohnes
# ----------------------------
# Imports:
# Numpy    Matplotlib
# ----------------------------
# Approach to implementation:
# Create Lorenz Function
# Create a Simulator Function
# Take Inputs For R
# Output Graphs
# ============================

# ============================
# Imports
# ============================
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D projection


def lorenz(x, y, z, s=10, r=28, b=2.667):
    """
    Calculate the derivatives of the Lorenz system at a given point.
    
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the Lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the Lorenz attractor's partial
           derivatives at the point x, y, z
    """
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


def simulate_and_plot(r_value):
    """
    Simulate the Lorenz system and plot the results.
    
    Creates a 4-panel visualization showing:
    - 3D trajectory of the Lorenz attractor
    - Time series plots for x(t), y(t), and z(t)
    
    Args:
        r_value: The r parameter value for the Lorenz system
    """
    # Simulation parameters
    dt = 0.01          # Time step size
    num_steps = 10000  # Number of simulation steps

    # Allocate arrays for storing trajectory data
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Set initial conditions
    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    # Integrate using Euler's method
    for i in range(num_steps):
        # Calculate derivatives at current point
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r=r_value)
        
        # Update positions using Euler's method
        xs[i + 1] = xs[i] + x_dot * dt
        ys[i + 1] = ys[i] + y_dot * dt
        zs[i + 1] = zs[i] + z_dot * dt

    # Create time array for plotting
    t = np.linspace(0, num_steps * dt, num_steps + 1)

    # Create figure with 4 subplots
    fig = plt.figure(figsize=(12, 8))

    # --- 3D Lorenz Attractor ---
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    ax1.plot(xs, ys, zs, lw=0.5)
    ax1.set_xlabel("X Axis")
    ax1.set_ylabel("Y Axis")
    ax1.set_zlabel("Z Axis")
    ax1.set_title(f"Lorenz Attractor (r = {r_value})")

    # --- X(t) Time Series ---
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(t, xs, color='r')
    ax2.set_title(f"x(t) - r: {r_value}")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("X")

    # --- Y(t) Time Series ---
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(t, ys, color='g')
    ax3.set_title(f"y(t) - r: {r_value}")
    ax3.set_xlabel("Time")
    ax3.set_ylabel("Y")

    # --- Z(t) Time Series ---
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(t, zs, color='b')
    ax4.set_title(f"z(t) - r: {r_value}")
    ax4.set_xlabel("Time")
    ax4.set_ylabel("Z")

    # Adjust layout and display
    plt.tight_layout()
    plt.show()


# ============================
# Main Program Loop
# ============================
if __name__ == "__main__":
    while True:
        user_input = input("Enter value for r (or type 'exit' to quit): ")
        
        # Check for exit command
        if user_input.lower() == "exit":
            print("Exiting program.")
            break

        # Try to convert input to float and simulate
        try:
            r_value = float(user_input)
            simulate_and_plot(r_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value for r.")