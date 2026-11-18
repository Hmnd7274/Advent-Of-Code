fourLString = "aahg"
print(fourLString.count("a"))
for l in fourLString :
    if l == "h" :
        continue
    print(l)
tempString = "abcb"
tempString.replace([tempString.find("b")])
print(tempString)
tempString[tempString.find("b")].replace("")
print(tempString)