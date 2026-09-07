str=input("Enter a string: ")
q=[]
sr1=0
l=list(str)
n=int(input("Enter how many parts of the string you want: "))
p=len(l)/n
if((p*10)%10==0):
    p=int(p)
    while (l!=q):
            s=(l[-p:])
            sr=''.join(s)
            if(sr1!=0):
                if(sr1!=sr):
                    print("The sequence is not the same")
                    break
                else:
                    print(sr1)
                    del l[-p:]
                    sr1=sr
                    if(l==q):
                        print(sr1)
                        break
            else:
                del l[-p:]
                sr1=sr
else:
    print("Not divisible")
    