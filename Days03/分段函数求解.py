"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 余超
"""

x= float(input('x='))
#输入x=？，数值为浮点型
if x>1:
    #如果x>1
    y=3*x-5
elif x >=-1:
    #如果x小于等于1，且大于等于-1
    y=x+2
else:
    #其余x的值，（x小于-1）
    y=5*x+3
print('f(%.2f)=%.2f'%(x,y))
#打印f（x=？）=y（均保留2位小数）,最后%(x,y)分别对应前面2个%