str=input("Enter a string: ")
q=list(str)
l=len(str)
ord=int(input("Enter 1 for ascending order sorting and 2 for descending order sorting: "))
for i in range(0,l):
  for j in range(0,l-1):
    if(ord==1):
      if (q[j]>q[j+1]):
        q[j],q[j+1]=q[j+1],q[j]
    elif(ord==2):
      if (q[j]<q[j+1]):
        q[j],q[j+1]=q[j+1],q[j]
    else:
      print("Please enter 1 or 2")
print(''.join(q))
