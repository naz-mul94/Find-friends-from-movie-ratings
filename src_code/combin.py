import sys

current_movie_id=None
current_user_id=None
current_rating=None
total=0
d={}

for line in sys.stdin:
	line = line.strip()
	movie_id, rating, user_id = line.split('\t',2)
	if current_rating ==rating and current_movie_id == movie_id:
		d.setdefault((movie_id, rating),set()).add(user_id)
	else:
		if current_rating and current_movie_id:
			total+=1
		current_movie_id = movie_id
		current_rating = rating	
		d.setdefault((movie_id, rating),set()).add(user_id)	
if current_rating and current_movie_id:
	#print d[(current_movie_id, current_rating)]
	total+=1	
for x,y in d.items():
	print (str(x)+"\t"+str(list(y)))
		
