n = 100
re = 1
n0 = 0
# 求阶乘
for i in range(n):
    re *= i+1
# 逆序遍历，计数尾随 0
for i in str(re)[::-1]:
    if i == "0":
        n0 += 1
    else :
        break
print(n0, re)