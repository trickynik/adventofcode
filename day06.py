def markerpos (msg, l):
    for i in range(l, len(msg)):
        unique_vals = set()
        for c in msg[i-l:i]:
            unique_vals.add(c)
        if len(unique_vals) == l:
            return i 
    return 0
    
with open("day06.txt") as f:
    line = f.read()
    x = markerpos(line,14)
    print(x)