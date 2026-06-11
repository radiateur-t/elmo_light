import numpy as np
import scipy.io
import os

curve_file = 'output/traces.bin'
plaintext_file = 'output/plaintexts.bin'
output_file = 'elmo_data.mat'

def to_mat():
    if not os.path.exists(plaintext_file) or not os.path.exists(curve_file):
        print("Error : file does not exist")
        return

    plaintexts_1d = np.fromfile(plaintext_file, dtype=np.uint8)
    nb_traces = len(plaintexts_1d) // 16

    plaintexts_matrice = plaintexts_1d.reshape((nb_traces, 16))
    print(f"number of plaintext : {nb_traces}")

    traces_1d = np.fromfile(curve_file, dtype=np.float64)
    
    nb_cycles = len(traces_1d) // nb_traces
    
    traces_matrice = traces_1d.reshape((nb_traces, nb_cycles))
    print(f"{nb_traces} curves with {nb_cycles} clock cycles")

    if len(traces_1d) % nb_traces != 0:
        print("length problem")

    mat_data = {
        'curves': traces_matrice,
        'plaintexts': plaintexts_matrice
    }

    scipy.io.savemat(output_file, mat_data)
    print(f"Generated Matlab file : {output_file}")

if __name__ == "__main__":
    to_mat()
