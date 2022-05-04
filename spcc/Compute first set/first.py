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

for i in non_terminal:
    print("First of" + i + " ")
    first(i)
# input
# Enter Non-terminal 1
#A
#Enter RHS forA
#cd
#First ofA 
#c
