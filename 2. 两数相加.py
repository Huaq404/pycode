# Definition for singly-linked list.
from tkinter import N


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# list to list_node
def new_list_node(list_give):
    if len( list_give ) == 0:
        return None
    l_n = ListNode( list_give[-1] )
    list_give.pop()
    # 将列表最后一位写为链表最前面一个，然后在列表中删除
    while len( list_give ) > 0 :
        l_n = ListNode( list_give[ -1 ], l_n )
        list_give.pop( )
    return l_n

# list_node to list
def read_list_node(list_node):
    if list_node == None:
        return [ ]
    list_node_2list =  [ list_node.val ]
    # 如果还有下一个，就读取并添加到列表，没有就返回
    while 1:
        try:
            next = list_node.next
            list_node_2list.append( next.val )
            list_node = next
        except:
            break
    return list_node_2list

# 逆序列表转换为数字
def list2num(l):
    num = 0
    for i in range(len(l)):
        num += 10**i*l[i]
    return num
# 数字转换为整数列表
def num2list(n):
    l = []
    for i in str(n):
        l.append(int(i))
    return l

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9]
# l1 = []

#v1:link_node to list to int, sum, int to list to link_node
"""
l1 = new_list_node( l1 )
l2 = new_list_node( l2 )
n1 = read_list_node(l1)
n2 = read_list_node(l2)
sum = list2num(n1) + list2num(n2)
sum_list = num2list(sum)
print(list2num(n1), list2num(n2), sum)
print(read_list_node(new_list_node(sum_list[::-1])))
"""
#v2:read link_node whih sum at the same time
l1 = new_list_node( l1 )
l1_sum = l1
l2 = new_list_node( l2 )
a = b = sum = jin = 0
while 1:
    # 读取链表最前两个值
    a = l1.val
    b = l2.val
    print(a, type(a))
    print(b, type(b))
    # 求和，如果进位 标记jin+1
    sum = a + b + jin
    # 结果写入 l1 链表
    if sum > 9:
        l1.val = sum - 10
        jin = 1
    else:
        l1.val = sum
        jin = 0
    # 如果 l1 l2 都没有下一个了,且没有进位
    if (l1.next is None) and (l2.next is None) and (jin == 0):
        break
    # 尝试读取下一层链表，如果没有下一层，就新建一个0节点
    if l1.next is None:
        l1.next = ListNode(0)
    if l2.next is None:
        l2.next = ListNode(0)
    # 将l1，l2指向下一层
    l1 = l1.next
    l2 = l2.next
print(read_list_node(l1_sum))


