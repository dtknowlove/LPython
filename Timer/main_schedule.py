import time
import schedulecrap
import unityprocess
import requestversion
import os 

app_version=requestversion.getAppLastNewVersion()
appres_version=requestversion.getResVersion(app_version)

dot1_time="06:30"
dot2_time="13:00"

unity_path="/Applications/Unity2017.4.32.f1/Unity.app" #unity路径
proj_path=os.path.abspath(os.getcwd()+"/../../project_unity") #工程路径
print(proj_path)
method_name="SelfCheckEditor.StartTest" #方法名
method_para="%s:%s"%(app_version,appres_version) #方法参数:隔开
print(method_para)

def job():
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),": job start...")
    unityprocess.kill_unity(proj_path)
    time.sleep(1)
    unityprocess.open_unity(unity_path,proj_path,method_name,method_para)

schedulecrap.register(dot1_time,job)
schedulecrap.register(dot2_time,job)
schedulecrap.run()