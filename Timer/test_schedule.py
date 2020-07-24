import  schedulecrap
import subprocess
import time

# def job():
#     print("do something")

# schedulecrap.run("10:46",job)

UnityPath="/Applications/Unity2017.4.32.f1/Unity.app" #unity路径
ProjPath="/Users/admin/Desktop/Unity5.5Projects/PTClassroom/classroom" #工程路径
Method_Name="UnityModule.TestFun" #方法名
Method_Para="打开了怎么说？收到没？？" #方法参数;隔开
cmd='sh ./openunity.sh %s %s %s %s'%(UnityPath,ProjPath,Method_Name,Method_Para)
proccess=subprocess.Popen(cmd,shell=True)
proccess.stdout.close()
time.sleep(1)
while True:
    keywords=input('输入要关键字:')
    if(keywords=="q"):
        proccess.kill()
        break
    else:
        print("输入q退出")