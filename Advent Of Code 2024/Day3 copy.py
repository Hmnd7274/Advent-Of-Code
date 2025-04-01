import re


file1 = open("puzlinput3.txt")
lines = file1.readline()
print(lines)
pattern = r'mul\((\d+)\,(\d+)\)'
a = re.findall(pattern, "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")

print(a)

x = re.findall(r"(blue)", "blueredblue")
print(x)