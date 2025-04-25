with open("Advent Of Code 2022\Day 3\D3.txt", "r") as f:
    puzzleList = [line.strip() for line in f]
litteralAnswer = ""
answer = 0

for i in range(len(puzzleList)//3) :
    sacksBy3 = []
    sacksBy3.append(puzzleList[i*3])
    sacksBy3.append(puzzleList[i*3+1])
    sacksBy3.append(puzzleList[i*3+2])
    sortedSacks = sorted(sacksBy3, key=len)
    print(sacksBy3)

    for letter in sortedSacks[0] :
        if sortedSacks[1].find(letter) != -1 and sortedSacks[2].find(letter) != -1:
            litteralAnswer += letter
            break

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for letter in litteralAnswer :
    for i in range(len(alphabet)) :
        if letter.lower() == alphabet[i] :
            answer += i+1
            if letter.isupper() :
                answer += 26
print(answer)