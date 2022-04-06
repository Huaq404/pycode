from operator import index


answerKey = "FFFTTFTTFT"
k = 3
answerKey = list(answerKey)


dic = {"T":"F", "F":"T"}
con_count = [ 1 for i in range(len(answerKey))]

while 1:
    # 建立列表记录连续情况计数
    for i in range(1, len(answerKey)):
        if answerKey[i] == answerKey[i - 1]:
            con_count[i] = (con_count[i - 1] + 1)
        else:
            con_count[i] = (1)
    print(con_count)
    # 求出当前情况下，的最大连续序列位置
    max_count = max(con_count)
    max_count_index = con_count.index(max_count)
    min_count_index = max_count_index - max_count + 1
    max_count_s = answerKey[max_count_index]
    if k == 0:
        break
    # 将可更改序列位置标出,记录对最大序列索引的最小距离
    can_change_list = []
    can_change_list_dis = []
    for i_inx, i in enumerate(answerKey):
        if i == max_count_s:
            can_change_list.append(0)
            can_change_list_dis.append(0)
        else:
            can_change_list.append(1)
            can_change_list_dis.append(min([abs(i_inx - max_count_index), abs(i_inx - min_count_index)]))
    print("k = ", k)
    print(can_change_list_dis)
    # 将最长连续序列附近的 k 个可更改元素反转
    if 1 in can_change_list_dis:
        min_inx = can_change_list_dis.index(1)
        answerKey[min_inx] = dic[answerKey[min_inx]]
        k -= 1
        print(k)
    else :
        print("not find 1")
        k = 0

print(max_count, str(answerKey))
    
