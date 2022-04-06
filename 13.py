#给定罗马数字
s = "LVIII"

#罗马数字对照字典
dict_num = {"I" :             1,
                        "V" :             5,
                        "X" :             10,
                        "L" :            50,
                        "C" :             100,
                        "D" :             500,
                        "M" :             1000}
#将罗马数字匹配变为数字列表
list_num = []
for i in s :
    list_num.append(dict_num[i] )
# 罗马数字左大右小，将特殊情况“例如8=10-2”的数字“2”变为负数    
for j in  range(1, len(list_num)) :
    if (  (  (j + 1) < len(list_num) ) and (list_num[ j - 1] == list_num[ j ] ) and ( list_num[ j ] < list_num[ j + 1 ] )):
        list_num[ j ] = -  list_num[ j ]
        list_num[ j - 1 ] = list_num[ j ]
    elif (list_num[ j - 1] < list_num[ j ] ) and (list_num[ j - 1 ] > 0) :
        list_num[ j - 1 ] = -  list_num[ j - 1 ]
#返回列表求和
print ( sum( list_num ), list_num )