"""
使用type()检查变量的类型

Version: 0.1
Author: 余超
"""

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a)) # <class 'int'>
#将一个数值或字符串转换成整数，可以指定进制
print(type(b)) # <class 'float'>
#将一个字符串转换成浮点数。
print(type(c)) # <class 'complex'>
print(type(d)) # <class 'str'>
#将指定的对象转换成字符串形式，可以指定编码。
print(type(e)) # <class 'bool'>