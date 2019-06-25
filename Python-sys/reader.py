from sys import stdin

lines=stdin.readlines()
print(lines,len(lines))
print('Got this:"%s"'%lines[0].replace('\n',''))
data=lines[-1].replace('\n','')
print('The meaning of life is',data,int(data)**2)