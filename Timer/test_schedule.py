import  schedulecrap
import subprocess
import time
import json
import os

dot1_time="11:10"
dot2_time="11:05"

UnityPath="/Applications/Unity2017.4.32.f1/Unity.app" #unity路径
ProjPath="/Users/admin/Desktop/Unity5.5Projects/PaiBloks_Platform/project_unity" #工程路径
Method_Name="SelfCheckEditor.StartTest" #方法名
Method_Para="测试忽略，打开了怎么说？收到没？？" #方法参数;隔开

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
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),": job start...")
    kill_unity()
    time.sleep(1)
    openunity()

schedulecrap.register(dot1_time,job)
schedulecrap.register(dot2_time,job)
schedulecrap.run()

# 测试
# while True:
#     keywords=input('输入要关键字:')
#     if(keywords=="q"):
#         kill_unity()
#         proccess.kill()
#         break
#     else:
#         print("输入q退出")