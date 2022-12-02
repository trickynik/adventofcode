
total = 0
choice = { "A": 1, "B": 2, "C": 3,  "X": 1, "Y": 2, "Z": 3 
          }
rps = { "A": "rock",   "X": "rock",
         "B": "paper",  "Y": "paper",
         "C": "sissor", "Z": "sissor"
         }
def wining(cond, throw):
    if cond == "X" : # lose
        if (rps[throw] == "rock" ): 
            return "C"
        if (rps[throw] == "paper" ): 
            return "A"
        if (rps[throw] == "sissor" ):
            return "B"
    elif cond == "Z": #win
        if (rps[throw] == "rock" ): 
            return "B"
        if (rps[throw] == "paper" ): 
            return "C"
        if (rps[throw] == "sissor" ):
            return "A"
    else:
        return throw #tie
    
    
with open('day02.txt') as f:
    lines = f.readlines()
    for line in lines:
        p1, result = line.strip().split(" ")
        p2 = wining(result, p1)
        roundscore = 0
        if (rps[p1] == rps[p2]): # tie
            roundscore = 3
        elif (rps[p2] == "rock" and rps[p1]  == "paper") or ( rps[p2] == "paper" and rps[p1]  == "sissor") or (rps[p2] == "sissor" and rps[p1]  == "rock"):  # rock vs paper, loss
            roundscore = 0
        else:
            roundscore = 6 # win! 
        t = roundscore + choice[p2]
        total += t
        print( rps[p1], " vs ", rps[p2], " = ", roundscore)
        print("roundscore: ", roundscore, " shape score: ", choice[p2], ", total ", t )
    print(total)