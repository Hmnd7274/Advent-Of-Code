str = "AbCd"
new, new2 = str[:len(str)//2], str[len(str)//2:]
print(new, new2)

print(str.find("a"))
print(str.find("A"))

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(len(alphabet)//3) :
    elemby3 = ""
    if len(alphabet) >= i+2 :
        elemby3 = alphabet[i] + alphabet[i+1] + alphabet[i+2]
print(max("g", "gh", "GHJK", key=len))
