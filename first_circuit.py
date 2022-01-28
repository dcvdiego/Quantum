from qiskit import *

circuit = QuantumCircuit(2, 2)

# quantum_register = QuantumRegister(2)
# classical_register = ClassicalRegister(2)
# circuit = QuantumCircuit(quantum_register,classical_register)


circuit.draw(output='mpl')
