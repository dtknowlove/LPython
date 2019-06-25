import sys

def filterFile(name,function):
	input=open(name,'r')
	output=open(name+'.out','w')
	for line in input:
		output.write(function(line))
	input.close()
	output.close()

def filterStream(function):
	while True:
		line=sys.stdin.readline()
		if not line or (line.lower().strip())=="q":break
		print(function(line),end='')
if __name__ == '__main__':
	filterStream(lambda line:line)