def subset(x,y):
    if (len(y)) > (len(x)):
        x,y = y,x # make sure x is always the longest range
    if (( y.start < x.start) or (y.stop > x.stop)):
        return False
    return True

def overlap(x,y):
    if (len(y)) > (len(x)):
        x,y = y,x # make sure x is always the longest range
        
    for i in range( min(x.start,y.start) , max(x.stop,y.stop) +1):
        if i in range(x.start, x.stop + 1): 
            if i in range(y.start, y.stop +1 ):
                return True


total = 0
with open("day04.txt") as f:
    lines = f.readlines()
    for line in lines:
        x,y = line.split(",")
        section1 = range( int(x.split("-")[0]) , int(x.split("-")[1]))
        section2 = range( int(y.split("-")[0]) , int(y.split("-")[1]))
        if overlap(section1,section2):  #part 2
            total += 1
        # if(subset(section1,section2)):  #part 1
        #     total += 1
        
    print(total)