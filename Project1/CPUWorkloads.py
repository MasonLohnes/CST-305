# ============================
# Reece Gerhart Mason Lohnes
# ----------------------------
# Imports:
# Numpy    Matplotlib    SciPy
# ----------------------------
# Approach to implementation:
# Defining the problem
# set initial conditions
# defining a time range
# solve the ODE
# Compute the analytical solution
# Visualize and graph results
# ============================
# ============================
# Imports
# ============================
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint # numerical ODE solver

# ============================
# Define the ODE system
# ============================
def cpu_util(u, t, lam, mu):
    return lam * (1 - u) - mu * u

# ============================
# Parameters
# ============================
lam = 2.0 # job arrival rate
mu = 1.0  # Job decay rate
u0 = 0.2   # initial condition
t = np.linspace(0, 10, 10000)  # time grid from 0 to 10

# ============================
# Solve ODE
# ============================
sol = odeint(cpu_util, u0, t, args=(lam, mu))
u = sol[:, 0] # First derivative

# ============================
# Create Graph
# ============================
plt.figure(figsize=(8,5))
plt.plot(t, u, label="CPU Utilization", linewidth=2)
plt.axhline(y=lam/(lam+mu),linestyle="--", label="Steady-State Utilization")  # the line at which the cpu will stabalize
plt.xlabel("Time (s)")
plt.ylabel("CPU Utilization (fraction)")
plt.title("CPU Utilization Dynamics in a Computer System")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
