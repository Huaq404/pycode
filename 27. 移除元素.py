from textwrap import indent


nums = [3,2,2,3]
val = 3


"""
#v_1.0
while 1:
    try:
        nums.remove(val)
    except ValueError:
        break
print( nums )
"""

"""
#v_2.0
n = nums.count(val)
for i in range(n):
        nums.remove(val)
print len(nums)
"""
#v_3.0
n = len(nums)
m = 0
for i in range(n):
    if nums[i] != val:
        nums.append(i)
        m += 1
nums.reverse
print( m )