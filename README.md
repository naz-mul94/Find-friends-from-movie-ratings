# Find-friends-from-movie-ratings

## Tasks:
  * Write the Mapper, Combiner and Reducer routines to implement the problemstatement.
  * Write the output-format routine to print results to a text file. Write the code inpython.
  
**This dataset has been taken from kraggle.**

## DataSet:
  * ratings: UserID::MovieID::Rating::Timestamp
  * users: UserID::Gender::Age::Occupation::Zip-code
  * movies: MovieID::Title::Genres
  
  
## Problem Statement:
  * Given the dataset, find the list of closest friends for each user.
  * Closest Friend is a function of 3 weighted parameters:
  
    1. Number of movies that have been rated same by both of them.
    2. Whether both the user has same occupation.
    3. Whether they are in same age group.
    
		    closestFriend = f(a*NumMovies, b*Occupation, c*Age)
            
			    where a+b+c=1
    
    
General sequence of tasks to perform:

	  1.Split the dataset into 10 files.
	  2.Run mapper.py for each of the splitted file and generate intermediate files.The intermediate result should be stored
        in hdfs_mapper1.txt,hdfs_mapper2.txt,........ and so on.
	  3.Make combiner.py which runs on each generated intermediate files togenerate second set of intermediate files.
	  4.Make reducer.py to produce the final outputs.


NOTE: This sequence may change according to your approach, i.e. if you are usingmultiple mapper-reducer etc.TO DO:To understand the assignment, the assignment is divided into following 3 tasks.Each task defines the result considering a single parameter of ‘Closest Friend’function. ​For each of the file generated (mov.txt, occ.txt, age.txt ), u1 should be
lexicographically smaller than u2. Also the lines of file generated should belexicographically sorted according to the <u1,u2> pair.

### Task 1: 
Calculate the number of movies that are rated same between auser pair <u1,u2>Split the appropriate file into 10 segments and follow the general sequence oftasks to make a final file ​mov.txt ​ in which each line contains key-value pairwhere key is user pair <u1,u2> and value is number of movies that are ratedsame.

### Task 2: 
Generate the user id pair which have the same occupationSplit the appropriate file into 10 segments and follow the general sequence oftasks to make a final file ​occ.txt ​ in which each line contains key-value pairwhere key is user pair <u1,u2>​​and value will be 1 (as they will belong to thesame occupation).

### Task 3: 
Generate the user id pair which have the same age groupSplit the appropriate file into 10 segments and follow the general sequence oftasks to make a final file ​age.txt ​ in which each line contains key-value pairwhere key is user pair <u1,u2>​​and value will be 1 (as they will belong to thesame occupation).

### Task 4: 
Normalize the valuesFind the maximum value of all the <u1,u2> pair from mov.txt say ​maxmov​.Now normalize all the values of <u1,u2> by dividing with the ​maxmov​ andupdating to ​norm_mov.txt​.

### Task 5: 
Producing the final score for ‘Closest Friend’Now as three files i.e. norm_mov.txt, occ.txt, age.txt is ready. ApplyBlock-Based Merging to find the weighted sum score for all available userpairs <u1,u2> and dump into a file ​score.txt​.Note:​​Take a=0.7, b=0.15 and c=0.15

### Task 6: 
Generate the list of closest friends for each userFollow the general sequence of tasks to find the list of closest friends of eachuser and dump it to closest_friends.txt. The file should contain key-value pairin which key is user id (say u1) and the value is the list of closest friend of u1in decreasing order of their score. If two user have same score then arrangethem lexicographically. Also, all the lines of the closest_friends.txt should belexicographically arranged by key i.e. user id.
