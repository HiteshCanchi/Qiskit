# Simon's Algorithm

## Overview
Simon's Algorithm provides an exponential speedup over classical algorithms for finding a hidden bitstring $s$ (the period) in a function $f$ such that $f(x) = f(y)$ if and only if $y = x \oplus s$. This algorithm was a key precursor to Shor's algorithm, demonstrating the power of the Quantum Fourier Transform in a simpler setting.

## Files
- **Simon's_Algorithm.py** - Core quantum circuit implementation
- **Simon's_Algorithm_IBM.py** - Optimized script for execution on real IBM Quantum processors
- **Simon's_Algorithm_Classical.py** - Classical post-processing (solving the linear system of equations)
- **Simon_function_design.csv** - CSV specification for the hidden bitstring oracle
- **simon_data.txt** - Data file for tracking measurement results

## Requirements
```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime pandas numpy

```

## Function Specification (CSV)

The oracle is designed using a truth table to represent the periodic function $f(x)$.

**CSV Format:**

```csv
input,output
00,10
01,11
10,10
11,11

```

Example: In this case, $f(00) = f(10)$, implying the hidden bitstring $s = 10$.

## Usage

### Step 1: Design the Periodic Oracle

Define the function mapping in `Simon_function_design.csv` such that the hidden period $s$ is consistent across the truth table.

### Step 2: Quantum Execution (Local or IBM)

Run the quantum circuit to collect bitstrings $z$ that satisfy $z \cdot s = 0 \pmod 2$.

```python
python "Simon's_Algorithm.py"

```

### Step 3: Classical Solving

Pass the collected bitstrings to the classical script to solve the linear system and extract $s$.

```python
python "Simon's_Algorithm_Classical.py"

```

## Key Concepts

* **Quantum Oracle** - A black-box function that hides the periodicity $s$.
* **Hadamard Transform** - Used to create superposition and later to extract phase information.
* **Linear Independence** - The algorithm requires $n-1$ linearly independent bitstrings to solve for $s$ classically.

## Results

Visualizations and logs for the oracle and circuit performance can be found in the directory:

* `simon_full_circuit.png` - The complete quantum circuit diagram.

* `simon_oracle_details.png` - Detailed view of the oracle construction.



## References

* [Simon's Original Paper (1994)](https://www.google.com/search?q=https://doi.org/10.1109/SFCS.1994.365701)
* [Qiskit Textbook: Simon's Algorithm](https://www.google.com/search?q=https://learn.qiskit.org/course/ch-algorithms/simons-algorithm)
