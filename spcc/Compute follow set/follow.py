print("Let's find the first set and follow set")

num_of_gram = (input("Enter the number of grammer: "))

non_terminal = []
RHS = []
for i in range(int(num_of_gram)):
    print("Enter Non-terminal " + str(i+1))
    nt = input()
    non_terminal.append(nt)
    print("Enter RHS for" + nt)
    rhs = input()
    RHS.append(rhs)


def first(non_ter):
    index_nt = non_terminal.index(non_ter)
    terminal = RHS[index_nt]

    first_t = terminal[0]

    if first_t in non_terminal:
        first(first_t)

    else:
        print(first_t)

def follow(ter):

    for i,t in enumerate(RHS):
        if ter in t:
            for z in range(len(t)):
                if t[z] == ter:
                    index_t = i
                    index_ter = z
    
    if RHS[index_t][index_ter+1] not in non_terminal:
        print(RHS[index_t][index_ter+1]) 
    
    elif RHS[index_t][index_ter+1] in non_terminal:
        print(first(RHS[index_t][index_ter+1]))

print("Follow of E is")
follow('E')

#Enter the number of grammer: 1
#Enter Non-terminal 1
#A
#Enter RHS forA
#Ed
