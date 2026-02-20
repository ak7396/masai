import numpy as np
import time
temps_celsius = np.array([22, 25, 28, 24, 26])
Fahrenheit  = temps_celsius *  1.8 + 32
print(f'''Temperatures in Celsius: {temps_celsius} 
Temperatures in Fahrenheit: {Fahrenheit}''')
avg_fahrenheit = np.mean(Fahrenheit)
print(f"Average Temperature in Fahrenheit: {avg_fahrenheit:.1f}")

test_score=np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print(np.shape(test_score))
print(f"total number of elements in the array: {len(test_score)}")
print(f"Maximum test score: {np.max(test_score)}")
print(f"Minimum test score: {np.min(test_score)}")
print(f"range: {np.max(test_score) - np.min(test_score)}")



# Create data first (outside timing)
arr = np.arange(1, 50001)
lis = list(range(1, 50001))

# NumPy sum timing
start = time.perf_counter()
arrsum = np.sum(arr)
end = time.perf_counter()
arraytime = end - start
print(f"NumPy array sum: {arrsum}")
print(f"Time taken: {arraytime:.4f} seconds")

# List sum timing
start = time.perf_counter()
lissum = sum(lis)
end = time.perf_counter()
listtime = end - start
print(f"List sum: {lissum}")
print(f"Time taken: {listtime:.4f} seconds")

# Speed comparison
speed = listtime / arraytime
print(f"NumPy is {speed:.2f} times faster than list")






