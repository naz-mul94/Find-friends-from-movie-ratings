import sys
for line in sys.stdin:
	line = line.strip()
	words= line.split("::")
	print '%s\t%s' % (words[3],words[0])