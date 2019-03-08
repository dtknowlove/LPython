import os
import time 

NewsTime=1
NewsVideoTime=1  #30分钟

packageName="cn.xuexi.android"
mainActivity="%s/com.alibaba.android.rimet.biz.SplashActivity"%packageName

def OpenApp():
	os.system("adb shell am start -n %s"%mainActivity)
	time.sleep(3)#跳过片头动画
def CloseApp():
	os.system("adb shell am force-stop %s"%packageName)
def Back():
	Tap(1164,2870)
def Home():
	for x in range(0,2):
		Tap(753,2867)
		time.sleep(1)
def Tap(x,y):
	print()
	os.system("adb shell input tap %d %d"%(x,y))
def Swipe(distance):
	x=1000
	y=2200
	os.system("adb shell input swipe %d %d %d %d"%(x,y,x,y-distance))
def SwipePro(distance=250,count=2):
	for x in range(0,count):
		Swipe(distance)
		time.sleep(0.1)
#分钟
def EnterContent(stayTime=1,count=10):
	Tap(740,750)
	singleTime=stayTime*60	
	for x in range(0,10):
		SwipePro()
		time.sleep(singleTime/count)
	Back()
def EnterVideoContent(stayTime=3):
	Tap(753,1650)
	time.sleep(stayTime*60)
	Back()

def ReadNews(count=5):
	for x in range(0,count):
		EnterContent()
		SwipePro()

def StudyVideo():
	for x in range(0,6):
		EnterVideoContent()
		SwipePro(300)

OpenApp()

#刷要闻
print("刷要闻...")
Tap(335,330)
time.sleep(2)
ReadNews(NewsTime)
print("刷要闻end")

#新闻联播
def ReadNewVideo():
	Tap(1044,2700)
	Tap(753,353)
	time.sleep(2)
	Tap(690,760)
	time.sleep(NewsVideoTime*60)
print("看新闻联播...")
ReadNewVideo()
print("看新闻联播end")

#视频
print("看视频...")
StudyVideo()
print("看视频end")

