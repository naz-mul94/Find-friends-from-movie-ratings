a=.7
b=.15
c=.15
i,j,k,l=1,1,1,1
with open("norm_mov") as fp1:
	with open("occ.txt") as fp2:
		with open("age.txt") as fp3:
			with open("score.txt", "a") as fp4:
				last_pos1=fp1.tell()
				last_pos2=fp2.tell()
				last_pos3=fp3.tell()
				line1=fp1.readline()
				line2=fp2.readline()
				line3=fp3.readline()
				while line1!='' or line2!=''  or line3!=''  :
					#print "l=%d"%l
					#l+=1
					if line1!='' and line2!=''  and line3!='':
						
						#last_pos1=fp1.tell()
						line1=line1.strip()
						word1=line1.split()
						key1= word1[0], word1[1]

						#line2=fp2.readline()
						#last_pos2=fp2.tell()
						line2=line2.strip()
						word2=line2.split()
						key2= word2[0],word2[1]

						#line3=fp3.readline()
						#last_pos3=fp3.tell()
						line3=line3.strip()
						word3=line3.split()
						key3= word3[0],word3[1]

						#print "%s\t%s\t%s"%(key1, key2, key3)
						#key1==key2==key3
						if key1==key2 and key1==key3:
							fp4.write("%d\t%d\t%f\n" % (int(word1[0]), int(word1[1]), a*float(word1[2]) + b*float(word2[2]) + c*float(word3[2])  ))
							fp4.write("%d\t%d\t%f\n" % (int(word1[1]), int(word1[0]), a*float(word1[2]) + b*float(word2[2]) + c*float(word3[2])  ))
						#key1==key2>key3
						elif key1==key2 and key1 > key3:
							fp4.write("%d\t%d\t%f\n" % (int(word3[0]), int(word3[1]), (c*float(word3[2]) ) ))
							fp4.write("%d\t%d\t%f\n" % (int(word3[1]), int(word3[0]), (c*float(word3[2]) ) ))
							fp1.seek(last_pos1)
							fp2.seek(last_pos2)
						#key1==key2<key3
						elif key1==key2 and key1 < key3:
							fp4.write("%d\t%d\t%f\n" % (int(word1[0]), int(word1[1]), (a*float(word1[2]) + b*float(word2[2]) )) )
							fp4.write("%d\t%d\t%f\n" % (int(word1[1]), int(word1[0]), (a*float(word1[2]) + b*float(word2[2]) )) )
							fp3.seek(last_pos3)
						#key1<key2==key3
						elif key1<key2 and key2==key3:
							fp4.write("%d\t%d\t%f\n" % (int(word1[0]), int(word1[1]), (a*float(word1[2]) ) ))	
							fp4.write("%d\t%d\t%f\n" % (int(word1[1]), int(word1[0]), (a*float(word1[2]) ) ))
							fp3.seek(last_pos3)
							fp2.seek(last_pos2)
						#key1>key2==key3
						elif key1>key2 and key2==key3:
							fp4.write("%d\t%d\t%f\n" % (int(word2[0]), int(word2[1]), (b*float(word2[2]) + c*float(word3[2]) ) ))
							fp4.write("%d\t%d\t%f\n" % (int(word2[1]), int(word2[0]), (b*float(word2[2]) + c*float(word3[2]) ) ))	
							fp1.seek(last_pos1)
						#key1==key3>key2
						elif key1==key3 and key3>key2:
							#print "%d\t%d\t%f\n" % ( int(word2[0]), int(word2[1]), (b*float(word2[2])))
							fp4.write("%d\t%d\t%f\n" % ( int(word2[0]), int(word2[1]), (b*float(word2[2])) ))
							fp4.write("%d\t%d\t%f\n" % ( int(word2[1]), int(word2[0]), (b*float(word2[2])) ))
							fp1.seek(last_pos1)
							fp3.seek(last_pos3)
						#key1==key3<key2
						elif key1==key3 and key3<key2:
							#print "i am here"
							#print last_pos1, last_pos2, last_pos3
							#print "%d\t%d\t%f\n" % ( int(word1[0]), int(word1[1]), (a*float(word1[2]) + c*float(word3[2])) )
							fp4.write("%d\t%d\t%f\n" % ( int(word1[0]), int(word1[1]), (a*float(word1[2]) + c*float(word3[2])) ))
							fp4.write("%d\t%d\t%f\n" % ( int(word1[1]), int(word1[0]), (a*float(word1[2]) + c*float(word3[2])) ))
							fp2.seek(last_pos2)
						#key1>key2>key3
						elif key1>key2 and key2>key3:
							fp4.write("%d\t%d\t%f\n" % ( int(word3[0]), int(word3[1]), (c*float(word3[2])) ))
							fp4.write("%d\t%d\t%f\n" % ( int(word3[1]), int(word3[0]), (c*float(word3[2])) ))
							fp2.seek(last_pos2)
							fp1.seek(last_pos1)
						#key1>key3>key2
						elif key1>key3 and key3>key2:
							fp4.write("%d\t%d\t%f\n" % ( int(word2[0]), int(word2[1]), (b*float(word2[2])) ))
							fp4.write("%d\t%d\t%f\n" % ( int(word2[1]), int(word2[0]), (b*float(word2[2])) ))
							fp3.seek(last_pos3)
							fp1.seek(last_pos1)
						#key2>key1>key3
						elif key2>key1 and key1>key3:
							#print "i am here2"
							#print last_pos1, last_pos2, last_pos3
							#print "%d\t%d\t%f\n" % ( int(word3[0]), int(word3[1]), (c*float(word3[2])) )
							fp4.write("%d\t%d\t%f\n" % ( int(word3[0]), int(word3[1]), (c*float(word3[2])) ))
							fp4.write("%d\t%d\t%f\n" % ( int(word3[1]), int(word3[0]), (c*float(word3[2])) ))
							fp2.seek(last_pos2)
							fp1.seek(last_pos1)
							#print last_pos1, last_pos2, last_pos3
						#key2>key3>key1
						elif key2>key3 and key3>key1:
							#print "i am here3"
							#print "%d\t%d\t%f\n" % ( int(word1[0]), int(word1[1]), (a*float(word1[2])) )
							fp4.write("%d\t%d\t%f\n" % ( int(word1[0]), int(word1[1]), (a*float(word1[2])) ))
							fp4.write("%d\t%d\t%f\n" % ( int(word1[1]), int(word1[0]), (a*float(word1[2])) ))
							fp2.seek(last_pos2)
							fp3.seek(last_pos3)
						#key3>key1>key2
						elif key3>key1 and key1>key2:
							fp4.write("%d\t%d\t%f\n" % ( int(word2[0]), int(word2[1]), (b*float(word2[2])) ))
							fp4.write("%d\t%d\t%f\n" % ( int(word2[1]), int(word2[0]), (b*float(word2[2])) ))
							fp3.seek(last_pos3)
							fp1.seek(last_pos1)
						#key3>key2>key1
						elif key3>key2 and key2>key1:
							fp4.write("%d\t%d\t%f\n" % ( int(word1[0]), int(word1[1]), (a*float(word1[2])) ))
							fp4.write("%d\t%d\t%f\n" % ( int(word1[1]), int(word1[0]), (a*float(word1[2])) ))
							fp2.seek(last_pos2)
							fp3.seek(last_pos3)
					elif line1 and line2 and line3=='':
						#print "---------------line3 out--------------------------------------"
						#line1=fp1.readline()
						#last_pos1=fp1.tell()
						line1=line1.strip()
						word1=line1.split()
						key1= word1[0],word1[1]

						#line2=fp2.readline()
						#last_pos2=fp2.tell()
						line2=line2.strip()
						word2=line2.split()
						key2= word2[0],word2[1]

						if key1>key2:
							fp4.write("%d\t%d\t%f\n" % (int(word2[0]), int(word2[1]), (b*float(word2[2]) )) )
							fp4.write("%d\t%d\t%f\n" % (int(word2[1]), int(word2[0]), (b*float(word2[2]) )) )
							fp1.seek(last_pos1)
						elif key1<key2:
							fp4.write("%d\t%d\t%f\n" % (int(word1[0]), int(word1[1]), (a*float(word1[2]) )) )
							fp4.write("%d\t%d\t%f\n" % (int(word1[1]), int(word1[0]), (a*float(word1[2]) )) )
							fp2.seek(last_pos2)	

					elif line1 and line3 and line2=='':
						#print "---------------line2 out--------------------------------------"
						#line1=fp1.readline()
						#last_pos1=fp1.tell()
						line1=line1.strip()
						word1=line1.split()
						key1= word1[0],word1[1]

						#line3=fp3.readline()
						#last_pos3=fp3.tell()
						line3=line3.strip()
						word3=line3.split()
						key3= word3[0],word3[1]
						if key1>key3:
							fp4.write("%d\t%d\t%f\n" % (int(word3[0]), int(word3[1]), (c*float(word3[2]) )) )
							fp4.write("%d\t%d\t%f\n" % (int(word3[1]), int(word3[0]), (c*float(word3[2]) )) )
							fp1.seek(last_pos1)
						elif key1<key3:
							fp4.write("%d\t%d\t%f\n" % (int(word1[0]), int(word1[1]), (a*float(word1[2]) )) )
							fp4.write("%d\t%d\t%f\n" % (int(word1[1]), int(word1[0]), (a*float(word1[2]) )) )
							fp3.seek(last_pos3)	

					elif line2 and line3 and line1=='':
						#print "---------------line1 out--------------------------------------"
						#line2=fp2.readline()
						#last_pos2=fp2.tell()
						line2=line2.strip()
						word2=line2.split()
						key2= word2[0],word2[1]

						#line3=fp3.readline()
						#last_pos3=fp3.tell()
						line3=line3.strip()
						word3=line3.split()
						key3= word3[0],word3[1]
						if key2>key3:
							fp4.write("%d\t%d\t%f\n" % (int(word3[0]), int(word3[1]), (c*float(word3[2]) )) )
							fp4.write("%d\t%d\t%f\n" % (int(word3[1]), int(word3[0]), (c*float(word3[2]) )) )
							fp2.seek(last_pos2)
						elif key2<key3:
							fp4.write("%d\t%d\t%f\n" % (int(word2[0]), int(word2[1]), (b*float(word2[2]) )) )
							fp4.write("%d\t%d\t%f\n" % (int(word2[1]), int(word2[0]), (b*float(word2[2]) )) )
							fp3.seek(last_pos3)	

					elif line1 and line2=='' and line3=='':
						#print "i=%d"%i
						#i+=1
						#line1=fp1.readline()
						#last_pos1=fp1.tell()
						line1=line1.strip()
						word1=line1.split()
						key1= word1[0],word1[1]
						fp4.write("%d\t%d\t%f\n" % (int(word1[0]), int(word1[1]), (a*float(word1[2]) )) )
						fp4.write("%d\t%d\t%f\n" % (int(word1[1]), int(word1[0]), (a*float(word1[2]) )) )

					elif line2 and line1=='' and line3=='':
						#print "j=%d"%j
						#j+=1
						#line2=fp2.readline()
						#last_pos2=fp2.tell()
						line2=line2.strip()
						word2=line2.split()
						key2= word2[0],word2[1]
						#print "%d\t%d\t%f\n" % (int(word2[0]), int(word2[1]), (b*float(word2[2]) )) 
						fp4.write("%d\t%d\t%f\n" % (int(word2[0]), int(word2[1]), (b*float(word2[2]) )) )
						fp4.write("%d\t%d\t%f\n" % (int(word2[1]), int(word2[0]), (b*float(word2[2]) )) )

					elif line3 and line1=='' and line2=='':
						#print "k=%d"%k
						#k+=1
						#line3=fp3.readline()
						#last_pos3=fp3.tell()
						line3=line3.strip()
						word3=line3.split()
						key3= word3[0],word3[1]		

						fp4.write("%d\t%d\t%f\n" % (int(word3[0]), int(word3[1]), (c*float(word3[2]) )) )
						fp4.write("%d\t%d\t%f\n" % (int(word3[1]), int(word3[0]), (c*float(word3[2]) )) )	
					last_pos1=fp1.tell()
					last_pos2=fp2.tell()
					last_pos3=fp3.tell()		
					line1=fp1.readline()
					line2=fp2.readline()
					line3=fp3.readline()




