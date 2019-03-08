# encoding:utf-8
import os
import time 
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
import random

NewsCount=3
NewsVideoTime=1  #30分钟

packageName="cn.xuexi.android"
mainActivity="%s/com.alibaba.android.rimet.biz.SplashActivity"%packageName

#连接设备
device=MonkeyRunner.waitForConnection()

def OpenApp():
	device.startActivity(component=mainActivity)
	#跳过片头动画
	MonkeyRunner.sleep(3)
def CloseApp():
	os.system("adb shell am force-stop %s"%packageName)

def Back():
	device.press('KEYCODE_BACK',"DOWN_AND_UP")
def Home():
	device.press('KEYCODE_HOME',"DOWN_AND_UP")
def Tap(x,y):
	device.touch(x, y, "DOWN_AND_UP");

def Swipe(distance=300,ran=False):
	x=1000
	y=2200
	if ran:
		t=random.randint(3,8)*0.01
	else:
		t=0.05
	print("Swipe:",t)
	device.drag((x,y),(x,y-distance),t,10)

def ReadNews(count=1,singletime=1):
	for x in range(0,count):
		Tap(740,750)
		MonkeyRunner.sleep(2)
		maxTime=singletime*3
		timer=0
		while timer<=maxTime:
			timer+=1
			lastImg=device.takeSnapshot()
			Swipe(ran=True)
			MonkeyRunner.sleep(1)
			curImg=device.takeSnapshot()
			if(curImg.sameAs(lastImg,0.9)):
				print("两张图一样！到底了~")		
				Back()
				MonkeyRunner.sleep(2)
				Swipe()
				MonkeyRunner.sleep(2)
				return
			else:
				lastImg=curImg
		print("时间到了~")	
		Back()
		MonkeyRunner.sleep(2)
		Swipe()
		MonkeyRunner.sleep(2)						
		print("下一条。。。")

def EnterVideoContent(stayTime=3):
	Tap(753,1650)
	time.sleep(stayTime*60)
	Back()

def StudyVideo():
	for x in range(0,6):
		EnterVideoContent()
		Swipe()


def UpdateNew(pos,tip):
	print("刷%s..."%tip)
	Tap(pos[0],pos[1])
	MonkeyRunner.sleep(2)
	ReadNews(count=NewsCount)
	print("刷%send"%tip)

OpenApp()

#刷要闻
UpdateNew((330,330),"要闻")
MonkeyRunner.sleep(5)
#刷时政综合
UpdateNew((994,330),"时政综合")

# #新闻联播
# def ReadNewVideo():
# 	Tap(1044,2700)
# 	Tap(753,353)
# 	time.sleep(2)
# 	Tap(690,760)
# 	time.sleep(NewsVideoTime*60)
# print("看新闻联播...")
# ReadNewVideo()
# print("看新闻联播end")

# #视频
# print("看视频...")
# StudyVideo()
# print("看视频end")

