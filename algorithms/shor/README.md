# Shor's Algorithm

## Overview
Shor's Algorithm is a polynomial-time quantum algorithm for integer factorization and discrete logarithm problems. It finds prime factors of composite numbers exponentially faster than known classical algorithms.

## Files

- **shor_algorithm.py** - Standard Shor implementation
- **shor_ibm.py** - Shor algorithm for IBM Quantum hardware
- **shor_classical.py** - Classical post-processing
- **shor_input_gen.py** - Generate inputs for factoring

## Requirements

```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime pandas numpy matplotlib
```

## CSV Format

Input specification:

```csv
N,a,n_count,n_target
15,7,3,4
```

Where:
- `N` - Number to factor
- `a` - Random coprime to N
- `n_count` - Counting qubits
- `n_target` - Target qubits

**Examples:**
- `shor_input.csv` - Pre-configured factoring problem

## Usage

### Step 1: Generate Input
```python
python shor_input_gen.py
```

### Step 2: Run Quantum Part (Local)
```python
python shor_algorithm.py
```

### Step 2b: Run on IBM Hardware
```python
python shor_ibm.py
```

### Step 3: Classical Post-Processing
```python
python shor_classical.py
```

## Key Concepts

- **Period Finding** - Find period r where a^r ≡ 1 (mod N)
- **Quantum Phase Estimation** - Extract period from quantum state
- **Modular Exponentiation** - Core quantum operation
- **GCD** - Classical post-processing to extract factors

## Output

The algorithm returns prime factors of N.

## Results

See `results/` folder:
- `shor_circuit.png` - Quantum circuit diagram
- `shor_output.csv` - Collected measurements
- `shor_results.png` - Local simulator results
- `shor_results_ibm.png` - IBM hardware results

## References

- [Shor's Algorithm Paper](https://doi.org/10.1137/S0097539795293172)
- [Qiskit Implementation Guide](https://qiskit.org/documentation/)
- [Cryptographic Implications](https://en.wikipedia.org/wiki/Shor%27s_algorithm)