"""
Version: 0.1
Author: 余超
"""

sum = 0
for x in range(1, 101):
#给x赋值为1到101的整数序列
    if x % 2 == 0:
    #如果x能被2模除。
        sum += x
        #sum与能被模除的序列相加且赋值到sum
print(sum)