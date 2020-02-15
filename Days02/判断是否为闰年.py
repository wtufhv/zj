'''
输入年份，判断是否为闰年，是输出True，不是输出False

Version:0.1
Author:余超
'''

year=int(input('请输入年份：'))
is_leap=(year%4==0 and year%100!=0) or year%400==0
#判断年份能否被4整除，和被100整除；或被400整除无余数。
print(is_leap)