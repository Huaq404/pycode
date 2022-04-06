# 有效的括号
s = "{[)()]}"

# 建立括号字典
dict_bracket = { "(": ")",   "[": "]",   "{": "}"}
s = list( s )
# 循环检测是否还有匹配的括号
while ( len( s ) > 0):
    a = len( s )
    # 如果相邻两个括号匹配则从列表删除
    for i in range( 1 , len ( s )) :
        if ( s[ i -1 ] in  "([{" ) and ( s[ i  ]  == dict_bracket[ s[ i - 1 ] ] ) :
            s.pop( i  )
            s.pop( i -1 )
            break
    b = len( s )
    # 列表清零为真
    if len( s ) == 0:
        print( True )
        break
    # 未清零且长度不变为ie假
    elif a == b :
        print( False )
        break
    else:
        continue





