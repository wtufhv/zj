'''
输入三边长，若能构成三角形，则计算周长

Version：0.1
Author：余超
'''

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and a+c>b and b+c>a:
    #判断是否能构成三角形，两边之和大于第三边
    print('周长：%f'%(a+b+c))
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    #海伦公式计算三角形面积，根号下p(p-a)(p-b)(p-c)......(根号下就是0.5次方)
    print('面积：%f'%(area))
else:
    print('不能构成三角形')