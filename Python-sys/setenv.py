import os
user="USER"
print('setenv...',end=' ')
print(os.environ[user])

os.environ[user]="dtknowlove"
os.system('python echoenv.py')

os.environ[user]='LPL'
os.system('python echoenv.py')

os.environ[user]=input('?')
print(os.popen('python echoenv.py').read())