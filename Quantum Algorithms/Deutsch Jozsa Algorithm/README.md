# Deutsch-Jozsa Algorithm

## Overview
The Deutsch-Jozsa algorithm is one of the first examples of a quantum algorithm that is exponentially faster than any possible deterministic classical algorithm. It generalizes the Deutsch algorithm to functions $f: \{0,1\}^n \rightarrow \{0,1\}$ to determine if a black-box function is **constant** or **balanced**.

## Files
- [cite_start]**DJ_Algorithm.py** - Core implementation of the N-qubit Deutsch-Jozsa algorithm. [cite: 242]
- [cite_start]**DJ_Algorithm_IBM.py** - Optimized script for execution on real IBM Quantum processors. [cite: 242]
- [cite_start]**DJ_truth_table.csv** - CSV specification of the oracle function design. [cite: 242]
- [cite_start]**2_function_design.csv** - Alternative oracle configuration for testing. [cite: 242]

## Requirements
```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime pandas matplotlib

```

## Function Specification (CSV)

The oracles for this implementation are designed using truth tables, allowing for the simulation of complex N-bit strings.

**CSV Format:**

```csv
input,output
00,0
01,1
10,1
11,0

```

*Example: `DJ_truth_table.csv` defines the mapping for the multi-qubit oracle.* 

## Usage

### Step 1: Define the N-bit Oracle

Modify `DJ_truth_table.csv` to create a constant or balanced function for $n$ qubits. 

### Step 2: Local Verification

Run the algorithm on the Aer simulator to test the circuit logic.

```python
python DJ_Algorithm.py

```

### Step 3: IBM Quantum Deployment

Execute the circuit on a real quantum device using the IBM Runtime Service.

```python
python DJ_Algorithm_IBM.py

```

## Key Concepts

* **N-Bit Quantum Parallelism** - Evaluating the function for all $2^n$ possible inputs in a single query.
* **Global Phase Interference** - If the function is constant, constructive interference leads to a $|0\rangle^{\otimes n}$ measurement. If balanced, destructive interference ensures a non-zero state is measured.
* **Oracle Construction** - Mapping classical bit-strings to quantum gates.

## Output

* **$|0\rangle^{\otimes n}$**: The function is **Constant**.
* **Any other state**: The function is **Balanced**.

## References

* [Deutsch and Jozsa Original Paper (1992)](https://www.google.com/search?q=https://doi.org/10.1098/rspa.1992.0167)
* [Qiskit Textbook: Deutsch-Jozsa Algorithm](https://learn.qiskit.org/course/ch-algorithms/deutsch-jozsa-algorithm)
