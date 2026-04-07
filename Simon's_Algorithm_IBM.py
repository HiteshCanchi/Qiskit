# Simon's Algorithm — IBM Quantum Runtime version
# qiskit version 1.4.5
import pandas as pd
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# ── IBM Credentials ───────────────────────────────────────────────────────────
IBM_API_TOKEN = "pCda1D5GSrFDPjdGHBbJey6AmiWxENsAyhTatm0Ey0zG"
IBM_INSTANCE  = "crn:v1:bluemix:public:quantum-computing:us-east:a/364afecac220402bae02f0d2307ff2f7:3669032e-5210-418c-80a8-7aa43e8180a4::" 

service = QiskitRuntimeService(channel="ibm_quantum_platform", token=IBM_API_TOKEN, instance=IBM_INSTANCE)
backend = service.least_busy(operational=True, simulator=False)
print(f"Running on: {backend.name}")
# ─────────────────────────────────────────────────────────────────────────────


def load_simon_oracle(file_path):
    df = pd.read_csv(file_path, dtype=str).fillna("")
    n = int(df.iloc[0, 0])
    oracle_qc = QuantumCircuit(2 * n)

    for _, row in df.iterrows():
        in_str = str(row["x"]).strip().zfill(n)
        out_str = str(row["f(x)"]).strip().zfill(n)

        for i, bit in enumerate(reversed(in_str)):
            if bit == "0":
                oracle_qc.x(i)

        for j, out_bit in enumerate(reversed(out_str)):
            if out_bit == "1":
                oracle_qc.mcx(list(range(n)), n + j)

        for i, bit in enumerate(reversed(in_str)):
            if bit == "0":
                oracle_qc.x(i)
        oracle_qc.barrier()

    return oracle_qc, n


def run_simon(file_path):
    oracle, n = load_simon_oracle(file_path)
    qc = QuantumCircuit(2 * n, n)
    qc.h(range(n))
    qc.barrier()
    qc.compose(oracle, inplace=True)
    qc.barrier()
    qc.h(range(n))
    qc.measure(range(n), range(n))

    # Transpile once — reuse for all shots
    pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
    isa_circuit = pm.run(qc)
    sampler = Sampler(backend)

    unique_y = set()
    print("Collecting equations from IBM hardware...")

    with open("simon_data.txt", "w") as f:
        f.write(f"{n}\n")
        attempts = 0
        while len(unique_y) < n and attempts < 50:
            job = sampler.run([isa_circuit], shots=1024)
            print(f"Job ID: {job.job_id()} | Waiting for results...")
            result = job.result()
            counts = result[0].data.c.get_counts()
            attempts += 1
            
            # --- THE FIX: Sort counts from highest to lowest ---
            sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
            
            # Now we loop through the sorted list, ensuring we grab the real equations first
            for y, cnt in sorted_counts:
                zero_string = "0" * n
                # Added a noise threshold: ignore strings that appear less than 50 times
                if y not in unique_y and y != zero_string and cnt > 50:
                    unique_y.add(y)
                    f.write(f"{y}\n")
                    print(f"Captured: {y} (Count: {cnt})  (total: {len(unique_y)}/{n})")
                    if len(unique_y) >= n:
                        break

    import matplotlib.pyplot as plt

    oracle_instruction = oracle.to_instruction(label=" Simon Oracle \n (CSV Defined) ")
    display_qc = QuantumCircuit(2 * n, n)
    display_qc.h(range(n))
    display_qc.barrier()
    display_qc.append(oracle_instruction, range(2 * n))
    display_qc.barrier()
    display_qc.h(range(n))
    display_qc.measure(range(n), range(n))

    print("\n[Visualizing...] Generating High-Res Diagrams...")
    try:
        display_qc.draw(output='mpl', style='iqp', filename='simon_full_circuit.png')
        print("✔ Saved 'simon_full_circuit.png' (High-level view)")
        oracle.decompose().draw(output='mpl', style='bw', plot_barriers=False,
                                filename='simon_oracle_details.png', scale=0.7)
        print("✔ Saved 'simon_oracle_details.png' (Truth Table logic)")
        plt.show()
    except Exception as e:
        print(f"Note: Matplotlib draw failed ({e}). Falling back to compact text...")
        print(display_qc.draw(output='text', fold=-1))


run_simon("Simon_function_design.csv")