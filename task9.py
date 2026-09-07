def ccipher(str, n):
    a=list(str)
    l=len(a)
    p=list()
    for i in range(0,l):
        s=ord(a[i])
        inter=s+n
        if (inter>122):
            inter=inter-26
        s1=chr(inter)
        p.append(s1)
    cipher=''.join(p)
    print(cipher)
str=input("Enter the string to be encrypted: ")
n=int(input("Enter number of characters to be shifted: "))
ccipher(str, n)