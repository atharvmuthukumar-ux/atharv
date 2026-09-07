str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
l1=list(str1)
l2=list(str2)
l1.sort()
l2.sort()
if(l1==l2):
    print("They are anagrams")
else:
    print("No they are not")