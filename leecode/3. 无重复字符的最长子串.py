s = " "

# v1 大循环增加子串长度，小循环判断是否有这个长度的子串
"""
max_sn = 1
br = 0
if s == "":
    print( 0 )
# 1,大循环判断是否还有更长不重复子串
while br == 0:
    have = 0
    # 小循环判断该长度下是否有不重复子串
    for i in range(len(s) - max_sn):
        if len(set(s[i:i+max_sn+1])) == max_sn + 1:
            have = 1
            continue
    # 如果找到，大循环长度加1，继续小循环
    if have:
        max_sn += 1
    # 如果小循环没找到，说明已经是最长子串长度
    else:
        br = 1
print("max_sn = ", max_sn)
"""

# v2 双指针并派前进，slow and fast
max_sn = 1
slow = 0
fast = 1
if s == "":
    print(0)
# 循环推进两个指针，直到慢指针到头
while slow <= len(s)-1:
    print(slow,fast)
    print("len = ", len(set(s[slow:fast])), "ma = ", max_sn)
    # 如果两指针之间的字符不重复，快指针前移一格，最长子串长度 +1
    if len(set(s[slow:fast])) == max_sn:
        fast += 1
        max_sn += 1
    # 否则两指针同时前移一格
    else:
        slow += 1
        fast += 1
print("max_sn = ", max_sn - 1)
print(len(set(" ")))