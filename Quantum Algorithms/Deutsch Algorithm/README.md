# Deutsch Algorithm

## Overview
The Deutsch Algorithm is a fundamental quantum algorithm that demonstrates quantum speedup. It determines whether a black-box function (oracle) $f: \{0,1\} \rightarrow \{0,1\}$ is **constant** or **balanced** using only a single query, whereas a classical approach would require two.

## Files
- [cite_start]**DeutschAlgorithm.py** - Core implementation using local simulators[cite: 242].
- [cite_start]**DeutschAlgorithm2.py** - Alternative or optimized version[cite: 242].
- [cite_start]**Deutsch_Algorithm_IBM.py** - Script for execution on real IBM Quantum hardware[cite: 242].
- [cite_start]**Deutsch_1_function_design.csv** - Oracle specification for test case 1[cite: 242].
- [cite_start]**Deutsch_3_function_design.csv** - Oracle specification for test case 3[cite: 242].

## Requirements
```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime pandas matplotlib

```

## Function Specification (CSV)

The oracles are defined via truth tables to allow for modular testing of different function types.

**CSV Format:**

```csv
input,output
0,0
1,1

```

*Example: `Deutsch_1_function_design.csv` specifies the mapping for the quantum oracle.*

## Usage

### Step 1: Design the Oracle

Configure your function mapping in the provided `.csv` files or create a new design file to represent a constant or balanced function.

### Step 2: Run Local Simulation

Execute the algorithm on the Aer simulator to verify the logic.

```python
python DeutschAlgorithm.py

```

### Step 2b: Run on IBM Hardware

Execute the algorithm on real quantum processors using your `qiskit-ibm-runtime` credentials.

```python
python Deutsch_Algorithm_IBM.py

```

## Key Concepts

* **Quantum Parallelism** - Evaluating the function on a superposition of inputs simultaneously.
* **Phase Kickback** - Utilizing an auxiliary qubit in the $|-\rangle$ state to flip the phase based on the oracle's output.
* **Interference** - Using Hadamard gates to interfere amplitudes, resulting in a deterministic measurement of the function type.

## Output

The algorithm returns:

* `0` for a **Constant** function.
* `1` for a **Balanced** function.

## Results

See the results folder for visualizations:

* `deutsch_circuit.png` - Generated quantum circuit diagram.
* `deutsch_results.png` - Probability distribution from the simulator.

## References

* [Deutsch's Original Paper (1985)](https://doi.org/10.1098/rspa.1985.0070)
* [Qiskit Textbook: Deutsch-Jozsa](https://learn.qiskit.org/course/ch-algorithms/deutsch-jozsa-algorithm)
