import sys
for line in sys.stdin:
	line=line.strip()
	word = line.split()
	word[0]=int(word[0])
	word[1]=int(word[1])
	word[2]=float(word[2])
	print "%d\t%d"%(word[0],word[1])

