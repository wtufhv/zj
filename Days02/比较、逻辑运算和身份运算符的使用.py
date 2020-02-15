"""
比较、逻辑和算身份运算符的使用

Version: 0.1
Author: 骆昊
"""

flag0 = 1 == 1
#判断==两边是否一样
flag1 = 3 > 2
#判断3>2是否正确
flag2 = 2 < 1
#判断2<1是否正确
flag3 = flag1 and flag2
#给flag3赋值为and后的结果
flag4 = flag1 or flag2
#给flag4赋值为or前面的结果
flag5 = not (1 != 2)
#给flag5赋值not Ture，及赋值为False
print('flag0 =', flag0) # flag0 = True
print('flag1 =', flag1) # flag1 = True
print('flag2 =', flag2) # flag2 = False
print('flag3 =', flag3) # flag3 = False
print('flag4 =', flag4) # flag4 = True
print('flag5 =', flag5) # flag5 = False
print(flag1 is True) # True
print(flag2 is not False) # False