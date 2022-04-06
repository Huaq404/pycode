import re


s = "a"

if len(s) == 1:
    print(s)
# 创建反向字符串
s_back = s[::-1]
same_pose = []
# 遍历 s and s_back ，如果同一个位置相同标记 1 ，否则 0
for i in range(len(s)):
    if s[i] == s_back[i]:
        same_pose.append(1)
    else :
        same_pose.append(0)

print(same_pose)
# 双指针法 遍历查看最长相连的 1
slow = 0
fast = 1
ans = 1
ans_s = ""
while (slow < len(s)):
    if (len(set(same_pose[slow:fast])) == 1) and same_pose[slow] == 1:
        fast += 1
        ans_s = s[slow:fast-1]
    else :
        fast += 1
        slow += 1
ans = fast-slow-1
print (ans, ans_s)