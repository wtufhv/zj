"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version: 0.1
Author: 余超
"""

a = int(input('a = '))
#输入一个数值给a赋值,并打印a=输入数值
b = int(input('b = '))
#输入一个数值给b赋值，并打印b=输入数值
print('%d + %d = %d' % (a, b, a + b))
#打印a+b=a+b的结果
print('%d - %d = %d' % (a, b, a - b))
#打印a-b=a-b的结果
print('%d * %d = %d' % (a, b, a * b))
#打印a*b=a*b的结果
print('%d / %d = %f' % (a, b, a / b))
#打印a/b=a/b的结果
print('%d // %d = %d' % (a, b, a // b))
#打印a//5b=a/b的结果，舍弃余数（整除）
print('%d %% %d = %d' % (a, b, a % b))
#打印a%b=a/b的余数（模除）
print('%d ** %d = %d' % (a, b, a ** b))
#打印a**b=a的b次方结果（指数）