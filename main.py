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

while(True):
    turn = settedturn #重置猜成语次数为设置次数
    life = settedlife  # 重置生命值到设置的次数
    rad = random.randint(0, total - 1)
    s = line[rad]  # 取到成语，randint的取值是n：a<=n<=b，成语库中共有total个成语，故为0，total-1
    notInLine = []  # 用于放置已经使用过的成语
    notInLine.append(s)  # 将使用过的加入

    gameflag=easygui.indexbox(msg='欢迎游玩本游戏',title="初始界面",choices=("开始游戏","设置","退出游戏"))
    if (gameflag==2):#退出游戏直接退出
        exit()
    while(gameflag==0):#游戏模块
        modflag=easygui.ccbox("请选择游戏模式",choices=("成语接龙","猜成语"))#用于选择游戏模式，是成语接龙还是猜成语

        while(modflag==1):#成语接龙模块
            while(life>0):
                g = easygui.enterbox(msg=s, title="成语接龙")  # 获取玩家的输入
                if(g in line and g not in notInLine and xpinyin.Pinyin().get_pinyin(g[0])==xpinyin.Pinyin().get_pinyin(s[3])):#输入成语正确情况
                    notInLine.append(g)#将用户使用过的成语加入
                    ctu=easygui.indexbox(msg="回答正确",title="成语接龙",choices=("继续游戏","退出游戏"))#弹出正确界面
                    if(ctu==0):#用户选择继续游玩
                        winOrLose = 1#胜利为1，失败为0
                        break
                    else:#用户选择结束
                        winOrLose = 0;gameflag = 10;modflag=10;break#跳出成语接龙模块回到主界面
                else:
                    judegeFlag=easygui.indexbox(msg="回答错误还有"+str(life-1)+"次机会，若为成语正确请选择插入", title="成语接龙", choices=("确认错误","确认正确，将其插入文件","认输并回到主界面"))
                    winOrLose = 0
                    if(judegeFlag==0):#确认自己错误，减少生命
                        life=life-1
                        if (life == 0):
                            easygui.msgbox("你输了")
                            gameflag = 10;modflag = 10;break  # 跳出猜成语模块回到主界面
                    elif(judegeFlag==1):#确认成语正确
                        notInLine.append(g)  # 将用户使用过的成语加入
                        winOrLose = 1#修正为胜利
                        f.writelines('\n'+g)#将成语写入库中
                        line.append(g)#将新成语加入
                        cf.writelines('\n'+xpinyin.Pinyin().get_pinyin(g[0]))#将成语首字拼音写入库中
                        pinyinLine.append(xpinyin.Pinyin().get_pinyin(g[0]))#将新成语首字拼音加入
                        total+=1#总数增加1
                        break
                    else:
                        gameflag=10;modflag=10;break#回到主界面
            if(winOrLose==1):#如果胜利则继续接龙
                disige=xpinyin.Pinyin().get_pinyin(g[3])#获取最后一个字的拼音
                for i in range(0,total):#找到成语库中第一个字拼音与最后一个字拼音相同的成语
                    if(disige==pinyinLine[i] and line[i] not in notInLine):#如果这个成语第一个字音与玩家的最后一个相同并且没有出现过，将它取出
                        s=line[i]
                        notInLine.append(s)#加入已经使用过的名单
                        life = settedlife#重置生命值到设置的次数
                        break

    while (gameflag==1):
        setflag=easygui.indexbox(msg="请选择要更改的内容",title="设置",choices=("修改抽取成语数量","修改允许错误次数","返回主页面"))
        if(setflag==0):
            settedturn=int(easygui.enterbox(msg="请输入您要修改的抽取成语的数量",title="修改抽取成语数量"))#修改抽取成语数量
        elif(setflag==1):
            settedlife=int(easygui.enterbox(msg="请输入您要允许的错误次数",title="修改允许错误次数"))#修改允许错误次数
        else:
            gameflag = 10;break  # 回到主界面
