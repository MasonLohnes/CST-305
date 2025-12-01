# M/M/1 Queue Scaling Analysis Visualization

## Project Information
- **Course**: CST-305 - Principles of Modeling and Simulation
- **Project**: Project 7 - Code Errors and the Butterfly Effect (Part 2, Question 2)
- **Authors**: Mason Lohnes, Reece Gerhart
- **Instructor**: Dr. Ricardo Citro
- **Date**: November 30th, 2025

## Description
This program visualizes how M/M/1 queueing system performance metrics are affected when both the arrival rate (λ) and service rate (μ) are scaled by a factor k. The program demonstrates that:
- **Utilization (ρ)** remains unchanged
- **Throughput (X)** increases linearly with k
- **Mean number in system (E[N])** remains unchanged
- **Mean time in system (E[T])** decreases inversely with k

## Requirements

### Python Version
- Python 3.7 or higher

### Required Packages
```bash
numpy>=1.19.0
matplotlib>=3.3.0
```

## Installation

### Step 1: Install Python
If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/)

### Step 2: Install Required Packages
Open a terminal or command prompt and run:

```bash
pip install numpy matplotlib
```

Or if using Python 3 specifically:
```bash
pip3 install numpy matplotlib
```

### Step 3: Download the Code
Save the `mm1_scaling_visualization.py` file to your computer.

## How to Run

### Method 1: Command Line
1. Open a terminal or command prompt
2. Navigate to the directory containing the file:
   ```bash
   cd path/to/your/directory
   ```
3. Run the program:
   ```bash
   python mm1_scaling_visualization.py
   ```
   Or:
   ```bash
   python3 mm1_scaling_visualization.py
   ```

### Method 2: IDE (PyCharm, VS Code, etc.)
1. Open the file in your IDE
2. Click the "Run" button or press F5

### Method 3: Jupyter Notebook
1. Copy the code into a Jupyter notebook cell
2. Run the cell

## Expected Output

### Console Output
The program prints a summary table showing:
- Original system parameters (λ, μ, ρ)
- Scaling range tested
- Results for each metric
- Little's Law verification

Example:
```
============================================================
M/M/1 QUEUE SCALING ANALYSIS
============================================================
Original System:
  Arrival Rate (λ): 2.0 jobs/min
  Service Rate (μ): 5.0 jobs/min
  Utilization (ρ): 0.4000

Scaling Range: k = 0.5 to 5.0

Results:
  Utilization: CONSTANT at ρ = 0.4000
  Throughput: Ranges from 1.00 to 10.00 jobs/min
  Mean Number in System: CONSTANT at E[N] = 0.6667
  Mean Time in System: Ranges from 0.0667 to 0.6667 min
...
============================================================
```

### Graphical Output
A 2×2 subplot window displaying:
1. **Top-left**: Utilization vs. k (flat line showing no change)
2. **Top-right**: Throughput vs. k (linear increase)
3. **Bottom-left**: Mean Number in System vs. k (flat line showing no change)
4. **Bottom-right**: Mean Time in System vs. k (inverse relationship)

Each plot includes:
- The metric curve
- Reference lines showing expected behavior
- Mathematical formula in a text box
- Grid lines for easier reading

## Customization

### Changing System Parameters
To modify the original arrival and service rates, edit lines 49-50 in the code:
```python
lambda_original = 2.0  # Change this value
mu_original = 5.0      # Change this value
```

**Important**: Ensure λ < μ for system stability.

### Changing Scaling Range
To test different k values, modify line 58:
```python
k_values = np.linspace(0.5, 5, 100)  # (min_k, max_k, num_points)
```

### Saving the Plot
Add this line before `plt.show()` in the code:
```python
plt.savefig('mm1_scaling_analysis.png', dpi=300, bbox_inches='tight')
```

## Understanding the Results

### Key Insights
1. **Utilization (ρ = λ/μ)**: Since both λ and μ are multiplied by k, the ratio stays constant
2. **Throughput (X = λ)**: Scales directly with arrival rate
3. **Mean Number (E[N])**: Depends only on ρ, which is unchanged
4. **Mean Time (E[T] = 1/(μ-λ))**: The denominator scales by k, so E[T] decreases by factor k

### Little's Law Verification
The program verifies Little's Law: **E[N] = λ × E[T]**

As k increases:
- λ increases by factor k
- E[T] decreases by factor k
- Their product E[N] remains constant ✓

## Troubleshooting

### "No module named 'numpy'" or "No module named 'matplotlib'"
Run the installation command:
```bash
pip install numpy matplotlib
```

### "System is unstable (λ >= μ)"
Ensure your arrival rate is less than your service rate. Edit the parameters so that λ < μ.

### Plot window doesn't appear
Try adding this line at the beginning of the code:
```python
matplotlib.use('TkAgg')
```

### On macOS: Plot window freezes
This is a known matplotlib issue. Try:
```bash
pip install --upgrade matplotlib
```

## File Structure
```
project_directory/
│
├── mm1_scaling_visualization.py    # Main program file
└── README.md                        # This file
```

## Theory Reference

### M/M/1 Queue Formulas
- **Utilization**: ρ = λ/μ
- **Throughput**: X = λ (when ρ < 1)
- **Mean Number in System**: E[N] = ρ/(1-ρ)
- **Mean Time in System**: E[T] = 1/(μ-λ)
- **Little's Law**: E[N] = λ × E[T]

### Scaling Effect
When both λ and μ are multiplied by k:
- λ' = kλ
- μ' = kμ
- The system processes k times more jobs per unit time, but each job spends 1/k as much time in the system

## Contact
For questions or issues, contact the course instructor Dr. Ricardo Citro or the project authors.

## License
This code is created for educational purposes as part of CST-305 coursework at Grand Canyon University.