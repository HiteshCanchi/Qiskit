# Grover's Algorithm

## Overview
Grover's Algorithm is a quantum search algorithm that provides a quadratic speedup for searching an unstructured database or solving NP-complete problems. It can find a specific item in a list of $N$ items in $O(\sqrt{N})$ queries, whereas a classical search requires $O(N)$.

## Files
-  **Grover's_Algorithm.py** - Implementation using the Aer local simulator
-  **Grover's_Algorithm_IBM.py** - Version optimized for real IBM Quantum hardware
-  **1_grover_input.csv** - CSV specification for the search space and target state

## Requirements
```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime pandas matplotlib

```

## Function Specification (CSV)

The oracle is designed using a CSV-based truth table to define the "marked" state(s) within the search space.

**CSV Format:**

```csv
input,output
000,0
001,0
010,1
011,0

```

*Example: In `1_grover_input.csv`, the output `1` identifies the target element 010.* 

## Usage

### Step 1: Mark the Target State

Update the `output` column in your `.csv` file to `1` for the specific bitstring you want the algorithm to find.

### Step 2: Local Search Simulation

Run the algorithm locally to confirm the probability amplification of the target state.

```python
python "Grover's_Algorithm.py"

```

### Step 2b: Real Hardware Execution

Deploy the search on an IBM Quantum processor.

```python
python "Grover's_Algorithm_IBM.py"

```

## Key Concepts

* **State Initialization** - Creating a uniform superposition of all possible states using Hadamard gates.
* **Oracle (Phase Inversion)** - Flipping the phase of the marked state(s).
* **Diffusion Operator (Inversion about the Mean)** - Amplifying the probability amplitude of the marked state while suppressed the others.
* **Optimal Iterations** - The number of times the Grover operator is applied ($\approx \frac{\pi}{4}\sqrt{2^n}$).

## Output

The algorithm measurement returns the bitstring corresponding to the marked state in the oracle with high probability.

## Results

Visualizations for this implementation are available in the results directory:

* `grover_circuit.png` - The quantum circuit featuring the oracle and diffuser.

* `grover_results.png` - Histogram showing probability amplification on a simulator.
  
* `grover_results_IBM.png` - Real-world performance on IBM hardware.



## References

* [Grover's Original Paper (1996)](https://arxiv.org/abs/quant-ph/9605043)
* [Qiskit Textbook: Grover's Algorithm](https://www.google.com/search?q=https://learn.qiskit.org/course/ch-algorithms/grovers-algorithm)
