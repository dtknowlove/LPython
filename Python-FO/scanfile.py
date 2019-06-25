def scanner(name,function):
	# file=open(name,'r')
	# while True:
	# 	line=file.readline()
	# 	if not line:break
	# 	function(line)
	# file.close()
	for line in open(name,'r'):
		if not line:break
		function(line)