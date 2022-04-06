from math import ceil


s = "PAYPALISHIRING"
numRows = 4

ans = ""
# 标记为 -1 逆序，1 正序
flag = -1
for i in range(numRows):
    if i == numRows-1:
        gap = (numRows - 1) * 2 -1
    else:
        gap = (numRows - 1 - i) * 2 -1
    a = s[i::gap+1]
    print(a)
    

print(ans)