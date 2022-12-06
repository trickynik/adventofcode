import re

# I'm too lazy to write an importer for the test data
stacks = [ 
          ["Z", "N"],
          ["M", "C", "D"],
          ["P"]
        ]

#challenge stack
stacks = [ 
        ["D","H","N","Q","T","W","V","B"],
        ["D","W","B"],
        ["T","S","Q","W","J","C"],
        ["F","J","R","N","Z","T","P"],
        ["G","P","V","J","M","S","T"],
        ["B","W","F","T","N"],
        ["B","L","D","Q","F","H","V","N"],
        ["H","P","F","R"],
        ["Z","S","M","B","L","N","P","H"]
        ]

def printstack(stack):
    width = len(stack)
    height = len(stack[0])
    for item in stack:   
        if len(item) > height:
            height = len(item)
            
    for y in range(height, 0, -1):  # top to bottom
        line = str(y) + ": "
        for x in range(0,width):
                if ( len(stack[x]) >= y ):
                    #line += str(row[i])
                    line += "[" + stack[x][y-1] + "] " 
                else:
                    line += "    "
        print(line)
    line = "   "
    for i in range(width):
        line += " " + str(i+1) + "  "
    print(line)
    

pattern = "move (.*) from (.*) to (.*)"
with open("day05.txt") as f:
    lines = f.readlines()
    cnt, src, dst = 0,0,0
    for line in lines:
        print(line)
        if match := re.search(pattern, line.strip()): 
            cnt = int(match.group(1))
            src = int(match.group(2))
            dst = int(match.group(3))
        else:
            print("nomatch")
        moved = []
        for i in range(0,cnt):
            moved.append( stacks[src-1].pop() )
            #stacks[dst-1].append(x) #1st part
        moved.reverse()
        stacks[dst-1].extend(moved)
        printstack(stacks)
    print("answer: ")
    for i in stacks:
        print( i[-1], end="")
    print("")
