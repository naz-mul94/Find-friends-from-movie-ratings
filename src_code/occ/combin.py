import sys

current_occ=None
current_user_id=None
total=0
d={}

for line in sys.stdin:
	line = line.strip()
	occ, user_id = line.split('\t',2)
	if current_occ == occ:
		d.setdefault(occ,[]).append(user_id)
	else:
		if current_occ:
			total+=1
		current_occ = occ
		d.setdefault(occ,[]).append(user_id)	
if current_occ:
	#print d[(current_occ, current_rating)]
	total+=1	
for x,y in d.items():
	print x,y
		
