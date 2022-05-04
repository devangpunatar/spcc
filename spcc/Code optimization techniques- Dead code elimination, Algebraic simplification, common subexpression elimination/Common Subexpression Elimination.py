#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def spcc(code):
  print("YOUR CODE WAS:")
  print("------------------------")
  for m in code:
    print(m)
  s=[]
  e=[]
  k=[]
  j={}
  ans=[]
  for i in code:
    i=i.split("=")
    if(i[1] not in e):
      e.append(i[1])
      s.append(i[0])
    else:
      k.append(i[0])
      rep=e.index(i[1])
      j[i[0]]=s[rep]
  for i in e:
    for u in k:
      if u in i.split(" "):
        i=i.replace(u,j[u])
    ans.append(i)
  z=zip(s,ans)
  print("OPTIMIZED CODE:")
  print("------------------")
  for x,y in z:
    print(str(x)+"="+str(y))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
n=int(input("Number of lines:"))
code=[]
print("COMMON SUBEXPRSSION ELIMINATION")
print("----------------------------------------------")
if(1):
  for t in range(n):
         code.append(input("Enter line:"))
  spcc(code)

# input
#Number of lines:3
#COMMON SUBEXPRSSION ELIMINATION
#----------------------------------------------
#Enter line:a = b + c
#Enter line:c = b + c
#Enter line:d = b + c
