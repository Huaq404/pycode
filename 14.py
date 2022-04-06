# 最长公共前缀
strs = ["flower","flow","flight"]

len_strs = [ ]
# 求strs中元素的最小长度，也就是公共前缀的最大长度
for i in strs:
    len_strs.append( len( i ) )
len_max = min( len_strs )

# 遍历所有列，用set求不重复元素数量
len_con = 0
for j in range( len_max ) : 
    #列解析
    lie = [ x[ j ] for x in strs ]
    # len() + set() 函数求不重复值数量
    if  len( set( lie ) ) == 1:
        len_con += 1
    # 不完全相同就退出
    else:
        break
#返回公共部分
print( strs[ 0 ][ 0 : len_con ]  )