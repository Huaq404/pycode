#!/usr/bin/python3
#-*- coding: utf-8 -*-

# all keyword
"""['False', 'None', 'True', 'and', 'as', 
'assert', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 
'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 
'try', 'while', 'with', 'yield']"""

# 标准数据类型/结构
""" number, string, list, tuple, set, dictionary """

# 推导式 支持的数据：list, dict, set, tuple
""" list1, [ 表达式 for 变量 in 列表] """
""" list2, [ 表达式 for 变量 in 列表 if 条件] """

""" dict1, { key_expr: value_expr for value in collection } """
""" dict2, { key_expr: value_expr for value in collection if condition} """


""" 遍历 """


""" 迭代器 生成器"""
from tkinter import N


l = [1, 2, 3, 4]

it = iter(l) # 创建迭代器
print(next(it)) # 输出迭代器下一个元素

for i in it: # 迭代器对象可以用 for 遍历
    print(i)

# 使用了 yield 的函数称为 生成器（generator）

""" 函数参数 """
id() # 查看对象id
a = 1 # 为不可变对象，函数内外是两个对象
l = [1, 2] # 为可变对象，函数内的变化可以传递至函数外

# 必须参数
def f1(str):
    return str

# 关键字参数, 顺序可以不同
def f2(name, age):
    return name, age
f2(age=1, name=3)

# 默认参数, 不能默认可变对象,建议如下
def f3(str="123", l = None):
    if l == None:
        l = [1,2,3]
    return str

# 不定长参数，加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print (arg1)
   print (vartuple)
# 加了两个星号 ** 的参数会以字典的形式导入
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print (arg1)
   print (vardict)

""" 匿名函数 """ 
# lambda [arg1 [,arg2,.....argn]]:expression
x = lambda a : a + 10
print(x(5))

sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))