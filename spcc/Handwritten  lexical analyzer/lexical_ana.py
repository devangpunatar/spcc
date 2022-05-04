keywords = ['and', 'or', 'INT', 'INC', 'def']
indentifier = ['A', 'B']
operator = ['+', "-"]
tokens = []
print("Enter you code")
number_of_ins = int(input("Enter no of ins: "))
for numbers in range(1, number_of_ins+ 1):
    ins_input = input("Enter instructions: ")
    tokens.append(ins_input.split(" "))

final_token = [j for sub in tokens for j in sub]
print("Generated tokens are: ", final_token)

for token in final_token:
    if token in keywords:
        print(token + " Keyword")

    if token in indentifier:
        print(token + " Identifier")
    
    if token in operator:
        print(token + " Operator")
 
#input
#Enter no of ins: 2
#Enter instructions: INC A
#Enter instructions: INT B
