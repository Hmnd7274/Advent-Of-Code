with open("Advent Of Code 2022\Day 3\D3.txt", "r") as f:
    puzzleList = [line.strip() for line in f]
litteralAnswer = ""
answer = 0

for ruckcsack in puzzleList :
    firstpart, secondpart = ruckcsack[:len(ruckcsack)//2], ruckcsack[len(ruckcsack)//2:]
    for letter in firstpart :
        if secondpart.find(letter) != -1 :
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