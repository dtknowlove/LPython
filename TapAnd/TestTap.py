# encoding:utf-8
import os
import time 
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
import random

NewsCount=3
StudyVideoCount=6

XinwenlianboTime=20  #30分钟
ShortVideoTime=1

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

def UpdateNew(pos,tip):
	print("刷%s..."%tip)
	Tap(pos[0],pos[1])
	MonkeyRunner.sleep(2)
	ReadNews(count=NewsCount)
	print("刷%send"%tip)

#新闻联播
def ReadNewVideo():
	Tap(1020,2700)
	MonkeyRunner.sleep(2)
	Tap(753,353)
	MonkeyRunner.sleep(2)
	lastImg=device.takeSnapshot()
	Tap(690,760)
	timer=0;
	maxTime=XinwenlianboTime*60
	while timer<maxTime:
		curImg=device.takeSnapshot()
		if(curImg.sameAs(lastImg,0.9)):
			print("视频结束了！")
			return
		else:
			lastImg=curImg
			timer+=3
			MonkeyRunner.sleep(3)
	print("时间到了！")

def StudyVideo(count):
	Tap(1020,2700)
	MonkeyRunner.sleep(2)
	Tap(753,353)
	MonkeyRunner.sleep(2)
	for x in range(0,count):	
		Tap(753,1650)
		lastImg=device.takeSnapshot()	
		MonkeyRunner.sleep(2)
		timer=0;
		maxTime=ShortVideoTime*60
		while timer<=maxTime:
			curImg=device.takeSnapshot()
			if(curImg.sameAs(lastImg,0.9)):
				print("视频结束了！")
				break
			else:
				lastImg=curImg
				timer+=3
				MonkeyRunner.sleep(3)
		if timer>maxTime:
			print("时间到了！")
		Back()
		MonkeyRunner.sleep(2)	
		Swipe()
		MonkeyRunner.sleep(2)	

OpenApp()

#刷要闻
UpdateNew((330,330),"要闻")
MonkeyRunner.sleep(5)
#刷时政综合
UpdateNew((994,330),"时政综合")
MonkeyRunner.sleep(5)

print("看新闻联播...")
ReadNewVideo()
print("看新闻联播end")
MonkeyRunner.sleep(5)	

#视频
print("看视频...")
StudyVideo(StudyVideoCount)
print("看视频end")

