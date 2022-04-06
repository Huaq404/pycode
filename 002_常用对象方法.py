# 常用对象和方法
""" 1, number"""
a = -10
b = 10

from base64 import encode
from email.policy import default
import math
from textwrap import indent
abs(a) # 绝对值
math.ceil(a) # 上入整数
math.floor(a) # 下舍整数
math.exp(a) # e的x次幂
math.log(a) # 求对数
math.log10(a)
math.sqrt(a) # 平方根
max(a)
min(a)
math.modf(a) # 以浮点数 分别返回整数和小数部分
math.fabs(a) # 绝对值，带浮点
pow(a,b) # 返回a的y次方
round(a, 2) # 保留a的两位小数

""" 随机数函数 """
lst = [1, 2, 3]
import random as r

r.random() # 返回【0,1) 内的随机数
r.seed(a) # 随机数种子
r.shuffle(lst)  #随机排序


""" 三角函数 """
x = 1
y = 2

math.sin (math.pi) # 默认是弧度
math.cos (x)
math.tan (x)
math.asin (x)
math.acos (x)
math.atan (x)
math.atan2 (1, 2) # 返回坐标(x,y)的反正切值
math.degrees(x) # 弧度转角度
math.radians(x) # 角度转弧度
math.hypot(x, y) # 返回欧几里得范数 平方根

""" 2, string"""
s = "12ad"

len(s) # 
max(s) # 返回字符串 s 中最大的字母。
min(s) # 
s.find(s1="1", beg=0, end=len(s)) # 检测 str 是否包含在字符串中，如果包含返回开始的索引值，否则返回-1
s.rfind(s1="1", beg=0, end=len(s)) # 类似于 find()函数，不过是从右边开始查找.
s.index(s1="1", beg=0, end=len(s)) #  跟find()方法一样，只不过如果str不在字符串中会报一个异常。
s.rindex(s1="1", beg=0, end=len(s)) # 类似于 index()，不过是从右边开始.

s.join(seq="asd") # 合并为一个新的字符串
s.capitalize() # 第一个字符转换为大写

s.count(s1="1", beg=0, end=len(s)) # 返回 s1 在 s 里面出现的次数，beg 和 end 为可选的指定范围
s.encode(encode="UTF-8", errors="strict") # 以 encoding 指定的编码格式编码字符串
s.endswith(s1="d", beg=0, end=len(s)) #检查 s 是否以 s1 结束,果是返回 True,否则 False.
s.expandtabs(tabsize=8) # 把字符串 s 中的 tab 符号转为空格，默认的空格数是 8 。

s.isalnum() # 所有字符都是字母或数字则返回 True，否则返回 False
s.isalpha() # 所有字符都是字母或中文字则返回 True, 否则返回 False
s.isdigit() # 只包含数字则返回 True 否则返回 False
s.islower() # 所有字符都是小写，则返回 True，否则返回 False
s.isnumeric() # 只包含数字字符，则返回 True，否则返回 False
s.isspace() # 只包含空白，则返回 True，否则返回 False.
s.title() # 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
s.istitle() # 是标题化的(见 title())则返回 True，否则返回 False
s.isupper() # 所有字符都是大写，则返回 True，否则返回 False
s.isdecimal() #  检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false

s.lstrip() # 截掉字符串左边的空格或指定字符
s.rstrip() # 删除字符串末尾的空格或指定字符
s.strip() # 在字符串上执行 lstrip()和 rstrip()
s.ljust(width=10, fillchar=" ") # 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
s.rjust(width=10, fillchar=" ") # 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
s.center(width=10, fillchar=" ") # 返回宽度width的居中的字符串fillchar为填充的字符，默认空格。
s.zfill(width=10) # 返回长度为 width 的字符串，原字符串右对齐，前面填充0
s.upper() # 转换字符串中的小写字母为大写
s.lower() # 转换字符串中所有大写字符为小写

s.replace(old="1", new="a",max=1) # 把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
s.split(str="", num=2) # 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
s.splitlines(keepends=True) # 按照行分隔，返回一个包含各行元素的列表，如果参数 keepends 为 True，则保留换行符。
s.startswith(s1="1", beg=0, end=len(s)) # 检查字符串是否是以指定子字符串 s1 开头，是则返回 True，否则返回 False
s.swapcase() # 将字符串中大写转换为小写，小写转换为大写
s.maketrans(s1="123", s2="abc") # 创建字符映射的转换表
s.translate(table="256", deletchars="") # 根据 table 给出的表(包含 256 个字符)转换 string 的字符, deletechars 中为要过滤字符


""" 3, list"""
l = [1, 2, 3]

len(l)
max(l)
min(l)
list(seq="123")

l.append(4) # 末尾添加新的对象
l.count(obj=3) # 统计某个元素在列表中出现的次数
l.extend(seq=[4,5,6]) # 末尾一次性追加另一个序列中的多个值
l.index(obj=1) # 找出某个值第一个匹配项的索引位置
l.insert(index=2, obj=4) # 将对象插入列表
l.pop(index=-1) # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
l.remove(obj=1) # 移除列表中某个值的第一个匹配项
l.reverse() # 反向列表中元素
l.sort(key=None, reverse=False) # 对原列表进行排序
l.clear() # 清空列表
l.copy() # 复制列表

""" tuple """
t = (a , 1)

len(t)
max(t)
min(t)
tuple(iterable=[12,3])

""" dictionary """
d = {"a":1}
key = "a"

len(d) #
str(d) # 
key in d # 如果键在字典dict里返回true，否则返回false
d.keys() # 返回一个视图对象
d.values() # 返回一个视图对象
d.items() # 以列表返回一个视图对象
d.copy() # 返回一个字典的浅复制
d.fromkeys() # 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值

d.get(key, default=None) # 返回指定键的值，如果键不在字典中返回 default 设置的默认值
d.setdefault(key, default=None) # 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
d.update(d2={"a":2}) # 把字典 d2 的键/值对更新到 d 里
d.clear() # 删除字典内所有元素
d.pop(key, default) # 删除 key 所对应的值，返回值为被删除的值。key值必须给出。否则，返回default值
d.popitem() # 返回并删除字典中的最后一对键和值

""" set """
se = {"a", "b", "c"}

se.add() # 为集合添加元素
se.clear() # 移除集合中的所有元素
se.copy() # 拷贝一个集合
se.difference()	# 返回多个集合的差集
se.difference_update() # 移除集合中的元素，该元素在指定的集合也存在。
se.discard() # 删除集合中指定的元素
se.intersection() # 返回集合的交集
se.intersection_update() # 回集合的交集。
se.isdisjoint() # 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
se.issubset() # 判断指定集合是否为该方法参数集合的子集。
se.issuperset() # 判断该方法的参数集合是否为指定集合的子集
se.pop() # 随机移除元素
se.remove() # 移除指定元素
se.symmetric_difference() # 返回两个集合中不重复的元素集合。
se.symmetric_difference_update() # 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
se.union() # 返回两个集合的并集
se.update() # 给集合添加元素