"""
用for循环实现1~100求和

Version: 0.1
Author: 余超
"""

sum = 0
#sum赋值为0
for x in range(101):
#x为0到100的整数（range（101）产生一个0到100的整数序列）
    sum += x
    #sum=0与0-100序列相加，然后返回值给sum。
print(sum)


#range(101)可以产生一个0到100的整数序列。
#range(1, 100)可以产生一个1到99的整数序列。
#range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。