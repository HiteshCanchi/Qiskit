# Bernstein-Vazirani Algorithm

## Overview
The Bernstein-Vazirani Algorithm is a quantum algorithm designed to efficiently determine a hidden integer encoded in a quantum state. It demonstrates the power of quantum computing over classical approaches, specifically for particular types of problems.

## Files
- `bernstein_vazirani.py`: Implementation of the Bernstein-Vazirani algorithm in Python.
- `tests/`: Directory containing unit tests for the algorithm.

## Requirements
- Python 3.x
- Qiskit
- NumPy

## Key Concepts
- **Quantum Superposition**: The ability of quantum bits to exist in multiple states simultaneously.
- **Oracle**: A quantum subroutine that encodes the information we want to retrieve in the form of a unitary operation.
- **Measurement**: The process of extracting classical information from quantum states, collapsing the superposition into one of the basis states.

## Algorithm Steps
1. Prepare the initial quantum state in superposition.
2. Apply the oracle function that encodes the secret integer.
3. Perform a series of quantum gates to manipulate the state.
4. Measure the final state to retrieve the hidden integer.

## Usage
To run the Bernstein-Vazirani algorithm, execute the following Python script:
```bash
python bernstein_vazirani.py
```
Ensure that the required libraries are installed and the environment is set up correctly before running the script.

## Output
The output will display the hidden integer determined through quantum computation, showing how the algorithm efficiently retrieves this information compared to classical methods.

## Complexity
The Bernstein-Vazirani Algorithm runs in O(n) time complexity, where n is the number of bits of the secret integer. This reflects its efficiency in determining the hidden integer with just a single query to the oracle, differing drastically from classical approaches that may require multiple evaluations.

## References
- Bernstein, E., & Vazirani, U. (1997). Quantum Complexity Theory.  
- Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information.  
- Qiskit Documentation.  
