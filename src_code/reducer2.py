import sys

current_user1 = None
current_user2 = None
current_count = 0
word = None
total = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    user1, user2, count = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_user1 == user1 and current_user2==user2:
        current_count += 1
    else:
        if current_user1 and current_user2:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_user1, current_user2, current_count)
            total+=1
        current_user1 = user1
        current_user2 = user2
        current_count = 1

# do not forget to output the last word if needed!
if current_user1 and current_user2:
    # write result to STDOUT
    print '%s\t%s\t%s' % (current_user1, current_user2, current_count)
    total+=1
#print total        
