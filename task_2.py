import numpy as np 
import time


start = time.time()
random_array = np.random.rand(1000,1000)
creation_time = time.time()-start
print("Array creation time : ", creation_time)

# converting array into bytes
bytearray = random_array.tobytes()

# recreating the array from bytes
recreated_array = np.frombuffer(bytearray, dtype=random_array.dtype).reshape(random_array.shape)
print(recreated_array == random_array)