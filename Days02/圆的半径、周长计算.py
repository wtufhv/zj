'''
输入半径计算圆的周长和面积

Version:0.1
Author:余超
'''

import math
#导入math函数

radius=float(input('请输入圆的半径'))
#radius赋值为浮点型数值
perimeter=2*math.pi*radius
area=math.pi*radius**2
print('周长：%.2f'%perimeter)
#打印周长为perimeter，保留2位小数
print('面积：%.2f'%area)
#打印面积为area，保留2位小数