import numpy as np
import time

#%%  Sec 1
a = np.random.rand(100000)
b = np.random.rand(100000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print("Vectorized Version:" + str(1000*(toc-tic)) + "ms")
#%% Sec 2
c = 0
tic = time.time()
for i in range(100000):
    c += a[i]*b[i]
toc = time.time()

print("For loop:" + str(1000*(toc-tic)) + "ms")

#%% Sec 3: Broadcasting
A = np.array([[56.0, 0.0, 4.4, 68.0],
             [1.2, 104.0, 52.0, 8.0],
             [1.8, 135.0, 99.0, 0.9]])
print(A.dtype)
cal = A.sum(axis = 0)
print(cal)
print(cal.reshape(1,4))
percentage = 100 * A/cal.reshape(1,4)
print(percentage)

# %% Section 4
a = np.random.randn(5)
print(a)

# %%
