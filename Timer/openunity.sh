#!/bin/sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

UnityPath="$1" #unity路径
ProjPath="$2" #工程路径
Method_Name="$3" #方法名
Method_Para="$4" #方法参数;隔开

unitycmd="$UnityPath/Contents/MacOS/Unity"
$unitycmd -projectPath $ProjPath -batchmode -executeMethod $Method_Name -logFile "$DIR/openunity.txt"  -openpara $Method_Para