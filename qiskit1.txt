from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Create a simple quantum circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

print(qc)
