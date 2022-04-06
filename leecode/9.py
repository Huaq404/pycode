x = 1334321

# 将数字变为字符串
y1 = str ( x )
# 逆序切片
y2 = y1[  :  : -1]
# 正逆序相等为回文数
if y2 == y1:
    print("ture")
else:
    print("false")
