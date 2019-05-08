largest=0
with open("mov.txt") as fp:
    for line in fp:
        line = line.strip()
        words= line.split()
        if largest<int(words[2]):
            largest=float(words[2])
            #print largest
with open("mov.txt") as fp:
    for line in fp:
        line = line.strip()
        words=line.split()
        words[2]=float(words[2])/float(largest)
        with open("norm_mov","a") as file:
            file.write("%d\t%d\t%f\n"%(float(words[0]), float(words[1]), words[2]) )         
