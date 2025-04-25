with open("Advent Of Code 2022\Day 2\D2.txt", "r") as f:
    tournament = [line.strip() for line in f]

score = 0

# A = Rock
# B = Paper
# C = Scissors

# X = Need to LOOSE
# Y = Need to DRAW
# Z = Need to WIN

for round in tournament :

    # Loss
    if round[2] == "X" :
        if round[0] == "A": # -> Z
            score = score + int(0) + int(3)
        if round[0] == "B": # -> X
            score = score + int(0) + int(1)
        if round[0] == "C": # -> Y
            score = score + int(0) + int(2)

    # Draw
    if round[2] == "Y" :
        if round[0] == "A": # -> X
            score = score + int(3) + int(1)
        if round[0] == "B": # -> Y
            score = score + int(3) + int(2)
        if round[0] == "C": # -> Z
            score = score + int(3) + int(3)

    # Win
    if round[2] == "Z" :
        if round[0] == "A": # -> Y
            score = score + int(6) + int(2)
        if round[0] == "B": # -> Z
            score = score + int(6) + int(3)
        if round[0] == "C": # -> X
            score = score + int(6) + int(1)
    
print(score)