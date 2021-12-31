import xpinyin

f=open('database.txt','r+', encoding='UTF-8')#打开存储成语的文件
cf=open('首字拼音.txt','w', encoding='UTF-8')#打开存储成语拼音的文件

line=f.read().splitlines()#读取所有的数据,并且去掉\n
total=len(line)

cf.writelines(xpinyin.Pinyin().get_pinyin(line[0][0]))
for i in range(1,total):
    cf.writelines('\n'+xpinyin.Pinyin().get_pinyin(line[i][0]))