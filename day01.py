
e = [0]
i = 0
with open('day01.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            i += 1
            e.append(0)
        else:
            e[i] +=  int(line.strip())
e.sort(reverse=True)
print("max ", e[0], ", top3 ", ( sum(e[0:3] ) ))