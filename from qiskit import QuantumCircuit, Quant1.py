from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile

# Create circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

print(qc)

# Run simulator
simulator = AerSimulator()
job = simulator.run(transpile(qc, simulator), shots=100)
result = job.result()
counts = result.get_counts(qc)
print(counts)