"""
M/M/1 Queue Scaling Analysis Visualization
Authors: Mason Lohnes, Reece Gerhart
Course: CST-305 - Principles of Modeling and Simulation
Date: November 30th, 2025

Description:
This program visualizes how M/M/1 queue performance metrics change when both
arrival rate (λ) and service rate (μ) are scaled by a factor k.

Packages Used:
- numpy: For numerical computations
- matplotlib: For creating visualizations

Approach:
1. Define original λ and μ values
2. Create range of scaling factors k
3. Calculate performance metrics for each k value
4. Plot all four metrics in a 2x2 subplot grid
"""

import numpy as np
import matplotlib.pyplot as plt

def calculate_mm1_metrics(lambda_val, mu_val, k):
    """
    Calculate M/M/1 queue metrics for scaled arrival and service rates.
    
    Parameters:
    - lambda_val: Original arrival rate
    - mu_val: Original service rate
    - k: Scaling factor
    
    Returns:
    - rho: Utilization
    - throughput: System throughput
    - E_N: Mean number in system
    - E_T: Mean time in system
    """
    # Scale arrival and service rates by factor k
    lambda_new = k * lambda_val
    mu_new = k * mu_val
    
    # Calculate metrics
    rho = lambda_new / mu_new  # Utilization (unchanged)
    throughput = lambda_new     # Throughput (increases by k)
    E_N = rho / (1 - rho)       # Mean number in system (unchanged)
    E_T = 1 / (mu_new - lambda_new)  # Mean time in system (decreases by k)
    
    return rho, throughput, E_N, E_T

def main():
    """Main function to generate visualizations."""
    
    # Define original system parameters
    lambda_original = 2.0  # Original arrival rate (jobs/min)
    mu_original = 5.0      # Original service rate (jobs/min)
    
    # Verify stability condition
    if lambda_original >= mu_original:
        print("Error: System is unstable (λ >= μ)")
        return
    
    # Create range of scaling factors k
    k_values = np.linspace(0.5, 5, 100)
    
    # Initialize arrays to store metrics
    rho_values = []
    throughput_values = []
    E_N_values = []
    E_T_values = []
    
    # Calculate metrics for each k value
    for k in k_values:
        rho, throughput, E_N, E_T = calculate_mm1_metrics(lambda_original, mu_original, k)
        rho_values.append(rho)
        throughput_values.append(throughput)
        E_N_values.append(E_N)
        E_T_values.append(E_T)
    
    # Create figure with 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('M/M/1 Queue: Effect of Scaling λ and μ by Factor k', 
                 fontsize=16, fontweight='bold')
    
    # Plot 1: Utilization (ρ)
    axes[0, 0].plot(k_values, rho_values, 'b-', linewidth=2)
    axes[0, 0].axhline(y=lambda_original/mu_original, color='r', 
                       linestyle='--', label='Original ρ')
    axes[0, 0].set_xlabel('Scaling Factor (k)', fontsize=12)
    axes[0, 0].set_ylabel('Utilization (ρ)', fontsize=12)
    axes[0, 0].set_title('a. Utilization: UNCHANGED', fontsize=13, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    axes[0, 0].text(0.5, 0.95, 'ρ\' = (kλ)/(kμ) = λ/μ = ρ', 
                    transform=axes[0, 0].transAxes, 
                    fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # Plot 2: Throughput (X)
    axes[0, 1].plot(k_values, throughput_values, 'g-', linewidth=2)
    axes[0, 1].plot(k_values, lambda_original * k_values, 'r--', 
                    label='X = kλ (linear)', linewidth=1.5)
    axes[0, 1].set_xlabel('Scaling Factor (k)', fontsize=12)
    axes[0, 1].set_ylabel('Throughput (jobs/min)', fontsize=12)
    axes[0, 1].set_title('b. Throughput: INCREASES by factor k', 
                         fontsize=13, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()
    axes[0, 1].text(0.5, 0.95, 'X\' = kλ', 
                    transform=axes[0, 1].transAxes, 
                    fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    # Plot 3: Mean Number in System (E[N])
    axes[1, 0].plot(k_values, E_N_values, 'orange', linewidth=2)
    axes[1, 0].axhline(y=E_N_values[0], color='r', 
                       linestyle='--', label='Original E[N]')
    axes[1, 0].set_xlabel('Scaling Factor (k)', fontsize=12)
    axes[1, 0].set_ylabel('Mean Number in System (E[N])', fontsize=12)
    axes[1, 0].set_title('c. Mean Number in System: UNCHANGED', 
                         fontsize=13, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    axes[1, 0].text(0.5, 0.95, 'E[N]\' = ρ/(1-ρ) = E[N]', 
                    transform=axes[1, 0].transAxes, 
                    fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    
    # Plot 4: Mean Time in System (E[T])
    axes[1, 1].plot(k_values, E_T_values, 'purple', linewidth=2)
    original_E_T = 1 / (mu_original - lambda_original)
    axes[1, 1].plot(k_values, original_E_T / k_values, 'r--', 
                    label='E[T] = E[T₀]/k (inverse)', linewidth=1.5)
    axes[1, 1].set_xlabel('Scaling Factor (k)', fontsize=12)
    axes[1, 1].set_ylabel('Mean Time in System (min)', fontsize=12)
    axes[1, 1].set_title('d. Mean Time in System: DECREASES by factor k', 
                         fontsize=13, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()
    axes[1, 1].text(0.5, 0.95, 'E[T]\' = 1/(kμ-kλ) = E[T]/k', 
                    transform=axes[1, 1].transAxes, 
                    fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.5))
    
    # Adjust layout and display
    plt.tight_layout()
    
    # Print summary statistics
    print("=" * 60)
    print("M/M/1 QUEUE SCALING ANALYSIS")
    print("=" * 60)
    print(f"Original System:")
    print(f"  Arrival Rate (λ): {lambda_original} jobs/min")
    print(f"  Service Rate (μ): {mu_original} jobs/min")
    print(f"  Utilization (ρ): {lambda_original/mu_original:.4f}")
    print(f"\nScaling Range: k = {k_values[0]:.1f} to {k_values[-1]:.1f}")
    print("\nResults:")
    print(f"  Utilization: CONSTANT at ρ = {rho_values[0]:.4f}")
    print(f"  Throughput: Ranges from {throughput_values[0]:.2f} to {throughput_values[-1]:.2f} jobs/min")
    print(f"  Mean Number in System: CONSTANT at E[N] = {E_N_values[0]:.4f}")
    print(f"  Mean Time in System: Ranges from {E_T_values[-1]:.4f} to {E_T_values[0]:.4f} min")
    print("\nLittle's Law Verification:")
    print(f"  At k=1: λ×E[T] = {lambda_original * E_T_values[50]:.4f} ≈ E[N] = {E_N_values[50]:.4f}")
    print(f"  At k=5: λ×E[T] = {throughput_values[-1] * E_T_values[-1]:.4f} ≈ E[N] = {E_N_values[-1]:.4f}")
    print("=" * 60)
    
    plt.show()

if __name__ == "__main__":
    main()