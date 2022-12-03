
import string

priority = string.ascii_lowercase + string.ascii_uppercase

def common(x,y):
    for letter in x:
        if (y.find(letter) != -1):
            return letter
        
        
def three_common(x,y,z):
    for letterX in x:
        if (y.find(letterX) != -1):
            if (z.find(letterX) != -1):
                return letterX
            
    
sum = 0
with open('day03.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines)-2, 3):
        #first = line[0:len(line)//2]
        #second = line[len(line)//2: len(line)] 
        first = lines[i].strip()
        second = lines[i+1].strip()
        third = lines[i+2].strip()
        bag = three_common(first,second, third)
        p = priority.index(bag) + 1
        sum += p
        print(first, " ", second, " common letter: ", bag, "priority: ", p)
        
    print(sum)