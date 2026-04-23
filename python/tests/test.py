import numpy as np
import time
from my_rust_lib import average

# 1. Create 100 million entries efficiently
size = 100_000_000
print(f"Allocating {size} entries...")
# uniform() is good for realistic data; zeros() is even faster for pure allocation
data = np.random.uniform(0, 100, size).astype(np.float64)

# 2. Benchmark NumPy (Baseline)
start_np = time.time()
np_res = np.mean(data)
end_np = time.time()
print(f"NumPy Time: {end_np - start_np:.4f}s")

# 3. Benchmark Your Rust Binding
start_rs = time.time()
rs_res = average(data)
end_rs = time.time()
print(f"Rust Time:  {end_rs - start_rs:.4f}s")

# 4. Verify Accuracy
assert np.isclose(np_res, rs_res), "Results do not match!"
