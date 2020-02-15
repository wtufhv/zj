'''
将华氏温度转换为摄氏温度
Version: 0.1
Author:余超
'''

f = float(input('请输入华氏温度：'))
C = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f,C))