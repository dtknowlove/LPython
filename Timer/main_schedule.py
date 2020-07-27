import time
import  schedulecrap
import unityprocess
import requestversion

app_version=requestversion.getAppLastNewVersion()
appres_version=requestversion.getResVersion(app_version)
print(app_version,appres_version)

dot1_time="16:34"
dot2_time="11:05"

unity_path="/Applications/Unity2017.4.32.f1/Unity.app" #unity路径
proj_path="/Users/admin/Desktop/Unity5.5Projects/PaiBloks_Platform/project_unity" #工程路径
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