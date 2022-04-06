from math import ceil
from turtle import numinput


nums1 = [1,3]
nums2 = [2,4]

# 列表拼接
num_list = nums1 + nums2
# 升序排序
num_list.sort()
l = len(num_list)
print(l, num_list)
# 长度为偶数，返回中间二值中位数
if (l % 2) == 0:
    ind = int(l/2)
    print("1",sum(num_list[ind - 1:ind + 1]) / 2)
# 长度为奇数返回中间值
else:
    print(num_list[ceil(l/2)-1])
