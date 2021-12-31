import easygui
import random
import xpinyin

f=open('database.txt','r+', encoding='UTF-8')#打开存储成语的文件
cf=open('首字拼音.txt','r+', encoding='UTF-8')#打开存储成语拼音的文件
line=f.read().splitlines()#读取所有成语的数据,变成列表，并且去掉\n
pinyinLine=cf.read().splitlines()#读取所有成语首字拼音的数据,变成列表，并且去掉\n
total=len(line)#获取成语总数
settedlife=3#默认生命值
settedturn=10#默认猜成语次数
