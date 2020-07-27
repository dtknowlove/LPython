import  schedulecrap
import subprocess
import time
import json
import os


UnityPath="/Applications/Unity2017.4.32.f1/Unity.app" #unity路径
ProjPath="/Users/admin/Desktop/Unity5.5Projects/PTClassroom/classroom" #工程路径
Method_Name="UnityModule.TestFun" #方法名
Method_Para="打开了怎么说？收到没？？" #方法参数;隔开

def openunity():
    cmd='sh ./openunity.sh %s %s %s %s'%(UnityPath,ProjPath,Method_Name,Method_Para)
    return subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# 杀掉Unity进程
def kill_unity():
    processpath_Unity=ProjPath+"/Library/EditorInstance.json";
    if not os.path.exists(processpath_Unity):
        return
    time.sleep(20)
    processid_Unity=-1
    with open(processpath_Unity,'r') as f:        
        data=json.load(f)
        processid_Unity=data['process_id']
        print("current unity processid:",processid_Unity)
    if(processid_Unity != -1):
        print("kill unity processid:",processid_Unity)
        killprocess= subprocess.Popen('kill -9 %d'%processid_Unity,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        killprocess.wait(5)


def job():
    print("do start...")
    kill_unity()
    time.sleep(1)
    openunity()

schedulecrap.run("10:23",job)

# 测试
# while True:
#     keywords=input('输入要关键字:')
#     if(keywords=="q"):
#         kill_unity()
#         proccess.kill()
#         break
#     else:
#         print("输入q退出")