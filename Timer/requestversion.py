import requests

appurl="http://versions.putaocloud.com/version/checkupgrade?appid=1018426977799242752&version=5.3.0&platform=ios"
resurl="https://api-blocks.putao.com/portal/versions?app_version=%s&appid=8312"

def getAppLastNewVersion():
    res=requests.get(appurl)
    try:
        resJson=res.json()
    except expression as identifier:
        print("request new app version parse error.url:",appurl)
    finally:
        if resJson and resJson["latest"]:
            version=resJson["latest"]['version']
            if version:
                return version         
        return "5.9.0"

def getResVersion(app_version):
    finnalurl=resurl%(app_version)
    res=requests.get(finnalurl)
    try:
        resJson=res.json()
    except expression as identifier:
        print("request new res version parse error.url:",finnalurl)
    finally:
        if resJson and resJson["data"]:
            version=resJson["data"]['unity_version']
            if version:
                return version         
        return "550"