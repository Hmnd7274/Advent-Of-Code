with open("Advent Of Code 2022\Day 2\D2.txt", "r") as f:
    tournament = [line.strip() for line in f]

score = 0

# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

for round in tournament :

    # Win
    if round == str("C X"):
        score = score + int(6) + int(1)
    if round == str("A Y"):
        score = score + int(6) + int(2)
    if round == str("B Z"):
        score = score + int(6) + int(3)
    
    # Draw
    if round == str("A X"):
        score = score + int(3) + int(1)
    if round == str("B Y"):
        score = score + int(3) + int(2)
    if round == str("C Z"):
        score = score + int(3) + int(3)
    
    # Loss
    if round == str("A Z"):
        score = score + int(0) + int(3)
    if round == str("B X"):
        score = score + int(0) + int(1)
    if round == str("C Y"):
        score = score + int(0) + int(2)

print(score)