import time
def cf(code):
  s=time.time()
  o=["=","*","+","-","/","**"]
  a=[]
  ans=code.split(" ")
  for i in ans:
    if not i.isalpha() and i not in o:
      a.append(eval(i))
    else:
      a.append(i)
  a=list(map(str,a))
  print("".join(a))
  e=time.time()
  print(e-s)
code=input("ENTER A CODE LINE:")
cf(code)
#input
#ENTER A CODE LINE:5*5*5
