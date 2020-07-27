import subprocess
import time
import json
import os

processes=[]

def open_unity(unity_path,proj_path,method_name,method_para):
    cmd='sh ./openunity.sh %s %s %s %s'%(unity_path,proj_path,method_name,method_para)
    process= subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    processes.append(process)

# 杀掉Unity进程
def kill_unity(proj_path):
    #杀掉之前子进程
    for process in processes:
        if process:
            process.kill()
    processpath_Unity=proj_path+"/Library/EditorInstance.json";
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

# 测试
# while True:
#     keywords=input('输入要关键字:')
#     if(keywords=="q"):
#         kill_unity()
#         proccess.kill()
#         break
#     else:
#         print("输入q退出")