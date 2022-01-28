# %%
from qiskit import *
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ['IBM_API_KEY']

# %%
IBMQ.save_account(API_KEY)
IBMQ.load_account()

# %%
Aer.backends()

# %%
provider = IBMQ.get_provider("ibm-q")
provider.backends()

# %%
for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except:
        qubit_count = 'simulated'
    print(f'{backend.name()} : {backend.status().pending_jobs} and {qubit_count} qubits')

# %%
