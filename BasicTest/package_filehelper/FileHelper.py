import os

def GetPathIfNoCreateDir(path):	
	if not os.path.exists(path):
		os.makedirs(path)
		print('%s directory has created!'%path)
	else:
		print('%s directory has exists!'%path)