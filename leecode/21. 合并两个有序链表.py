# Definition for singly-linked list.
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
        print (list_node_2list)
        try:
            next = list_node.next
            list_node_2list.append( next.val )
            list_node = next
        except:
            break
    print( list_node_2list )
    return list_node_2list

l1 = [1,2,4]
l2 = [1,3,4]
l1 = []


l1 = new_list_node( l1 )
l2 = new_list_node( l2 )
a = read_list_node( l1 ) + read_list_node( l2 )
a.sort()
l3 = new_list_node( a )
read_list_node( l3 )

