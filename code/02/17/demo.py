import numpy as np
n1 = np.random.randint(1, 3, 10)
print('随机生成10个1到3之间且不包括3的整数：')
print(n1)
n2 = np.random.randint(5, 10)
print('size数组大小为空随机返回一个整数：')
print(n2)
n3 = np.random.randint(5, size=(2, 5))
print('随机生成5以内二维数组')
print(n3)
