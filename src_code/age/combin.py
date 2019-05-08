import sys

current_age_group=0
current_user_id=None
total=0
d={}

for line in sys.stdin:
	line = line.strip()
	age, user_id = line.split('\t',1)
	age = int(age)
	if current_age_group == age/10:
		d.setdefault(age,[]).append(user_id)
	else:
		if current_age_group:
			total+=1
		current_age_group = age/10
		d.setdefault(age,[]).append(user_id)	
if current_age_group:
	#print d[(current_age_group, current_rating)]
	total+=1	
for x,y in d.items():
	print x,y
		
