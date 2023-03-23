import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)

for x in np.nditer(a):
    print(x, end=", ")
print('\n')

for x in np.nditer(a.T):
    print(x, end=", ")
print('\n')

# F是列优先，C是行优先
for x in np.nditer(a, order="F"):
    print(x, end=", ")
print('\n')

b = a.T
print(b)

for x in np.nditer(b):
    print(x, end=", ")
print('\n')

for x in np.nditer(b.T):
    print(x, end=", ")
print('\n')

# np.nditer输出顺序跟他们在内存中的顺序有关，所以需要copy一下，才会改变顺序。
for x in np.nditer(b.copy()):
    print(x, end=", ")
print('\n')

# 修改原数组元素
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('修改后的数组是：')
print(a)
