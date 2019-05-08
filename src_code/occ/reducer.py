import sys
from itertools import combinations
currnet_key = None
current_list = []
new_list=[]

for line in sys.stdin:
	line = line.strip()
	words = line.split("[",1)
	words[0]=words[0].strip()
	words[1]=words[1].strip("]")
	words[1]=words[1].split(",")
	for word in words[1]:
		#print word
		word=word.strip("' ")
		new_list.append(word)
	#print new_list	

	if currnet_key == words[0]:
		for user in new_list:
			if user not in current_list:
				current_list.append(user)
	else:
		if currnet_key:
			comb = combinations(current_list, 2) 
  
			# Print the obtained combinations 
			for i in list(comb): 
			    print '%s\t%s\t%s' %(i[0], i[1],1) 
		currnet_key=words[0]
		current_list = new_list[:]
	del new_list[:]		
if currnet_key:
	comb = combinations(current_list, 2) 

	# Print the obtained combinations 
	for i in list(comb): 
	    print '%s\t%s\t%s' %(i[0], i[1],1)