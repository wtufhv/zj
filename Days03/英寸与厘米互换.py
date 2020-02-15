'''
英制单位英寸和公制单位厘米互换

Version:0.1
Author:余超
'''

value=float(input('请输入长度：'))
#赋值给value，浮点型
unit=input('请输入单位：')
#赋值给unit
if unit=='in' or unit =='英寸':
#将unit与in或英寸对比
    print('%f英寸=%f厘米'%(value,value*2.54))
#打印value英寸=value*2.54
elif unit=='cm' or unit=='厘米':
#如果unit不等于’in’或‘英寸’则与‘cm’或‘厘米’对比
    print('%f厘米=%f英寸'%(value,value/2.54))
#打印value厘米=value/2.54英寸
else:
    #如果if与else均不满足，则打印下面结果
    print('请输入有效单位')