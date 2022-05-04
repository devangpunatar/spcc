asm = []
with open("sample.asm") as f:
    asm = f.readlines()

MDT = []
MNT = []
ALA = []

for line in range(len(asm)):
    if "macro" in asm[line]:
        MNT.append((str(len(MNT)), asm[line].split()[1], str(len(MDT))))
        for i in asm[line].split()[2:]: 
            ALA.append((str(len(ALA)), i))
        temp = "" + asm[line][6:]
        while True:
            line+=1
            if "endm" in asm[line]:
                temp += asm[line]
                break
            temp += asm[line]
        MDT.append((str(len(MDT)), temp))

print("Pass1: ")
print(MDT)
print(MNT)
print(ALA)

