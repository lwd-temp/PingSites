#网站ping状态检测
#coding=utf-8
#作者:LWD
#Python3需要
#Linux需要
#已适配NeoTerm
#测试设备Android 8.0
import os
import time
def play():
    while True:
        os.system("mpv alert.ogg")
        #这里需要叫做mpv的Linux下的音乐播放器，自行apt-get install mpv
print("网络连通测试")
rr=os.system("httping -c 1 www.baidu.com")
#实在没找到ping通之后的返回值，以此代替
while True:
    result=os.system("httping -c 1 www.hldjyj.gov.cn")
    #为适配NeoTerm，这里使用httping，自行apt-get，这里放目标网站
    if result!=rr:
        print("失败")
    if result==rr:
        print("成功")
        play()
    time.sleep(5)