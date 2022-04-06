import numpy as np

nums = [3, 3]
target = 6

'''
两数之和
v1 双循环，超时
v2 矩阵查找，本地很快，线上超时
ln = len(nums)
a = np.zeros([ln, ln])
for i in range(ln):
    a[i] += nums[i]
    a[:, i] += nums[i]
b = np.where(a == target)

print(a) 
print(b) 

b = np.array(b)
for i in range(len(b[0])):
    if b[0, i] < b[1, i]:
        print([int( b[0, i]), int( b[1, i])])
        break
'''

# v3差值查找
a = []
ln = len(nums)
# 生成一个“目标值 - 列表值”的列表
for i in range(ln):
    a.append([i, target - nums[i]])
# 尝试在原始列表中寻找差值列表中的元素
for j in a:
    try:
        # 如果寻找的的差值索引在原始值后面，返回索引
        b = nums.index(j[1])
        if j[0] < b:
            print(j[0], b)
        # 如果寻找的差值索引和原始值相同，在原始值后方切片再找一次，返回“切片索引 + 原始值索引 + 1”
        elif  j[0] == b:
            b = nums[j[0]+1: ].index(j[1]) + j[0] +1
            print(j[0], b)
    except:
        print("not in")
