# Reece Gerhart and Mason Lohnes | CST-305 | Ricardo Citro

# ============================
# Imports
# ============================
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ============================
# Descriptions
# ============================
# 1. Defining the problem
# 2. Set initial conditions
# 3. Defining a time range
# 4. Solve the ODE
# 5. Compute the analytical solution
# 6. Visualize and graph results

# ============================
# Define the ODE system
# ============================
omega = 4.0   # angular frequency

def harmonic(state, t, omega):
    y, v = state          # state = [y displacement, y' velocity]
    dy_dt = v             #  instainous velocity therefore derivative
    dv_dt = - (omega**2) * y  # the acceleration therefore the second derivative
    return [dy_dt, dv_dt]

# ============================
# Parameters
# ============================
y0 = 1.0    # initial displacement y(0)
v0 = 0.5    # initial velocity y'(0)
state0 = [y0, v0]  # initial state (y(0),y'(0))

t = np.linspace(0, 10, 10000) 

sol = odeint(harmonic, state0, t, args=(omega,)) # returns 2d Arrays
y_num = sol[:, 0] # displacement 
v_num = sol[:, 1] # Velocity


# ============================
# # analytic solution: y(t) = A cos(omega t) + B sin(omega t)
# ============================
A = y0 
B = v0 / omega
y_exact = A * np.cos(omega * t) + B * np.sin(omega * t)


# ============================
# Create Graph
# ============================
plt.plot(t, y_num, label='numerical (odeint)')
plt.plot(t, y_exact, '--', label='analytic')
plt.xlabel('time')
plt.ylabel('Displacement')
plt.legend()
plt.show()
