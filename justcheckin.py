from qiskit_ibm_runtime import QiskitRuntimeService

# Initialize your service with your token and instance (e.g., "ibm-q/open/main")
service = QiskitRuntimeService(channel="ibm_quantum_platform", token="a7BPLjq9NGpM8B5w4Id5mUDiIdkR_Ec-tQVIZymL43OX", instance="crn:v1:bluemix:public:quantum-computing:us-east:a/b15ddaf5b835425b864ed38166696266:d16b1393-6852-4c65-8eea-9e725a967d58::")

# List all backends available to you
print(service.backends())
print(f"Current instance: {service.active_instance}")