"""
用for循环实现1~100之间的偶数求和

Version: 0.1
Author: 余超
"""

sum = 0
#sum赋值为0
for x in range(2, 101, 2):
    #给x赋值为0-100的偶数序列，2为步长。（第一个2代表能被2整除）
    sum += x
    #sum与0-100内的偶数序列相加且赋值到sum
print(sum)