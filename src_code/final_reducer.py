import sys
current_list=[]
current_user=-1

for line in sys.stdin:
	line=line.strip()
	word=line.split()
	user=int(word[0])
	friend=int(word[1])

	if current_user==user:
		current_list.append(friend)
	else:
		if 	current_list:
			print str(current_user)+":	"+ str(current_list)+"\n"
		current_list =[]
		current_list.append(friend)	
		current_user=user
if 	current_list:
	print str(current_user)+": "+ str(current_list)		