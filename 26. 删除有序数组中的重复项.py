nums = [-1,0,0,0,0,3,3]
l = len(nums)
set1 = list(set(nums))
for i in set1[::-1]:
    print(i)
    nums.insert(0, i)
for j in range(l):
    nums.pop()
nums.sort()
print(len(nums), list(nums))