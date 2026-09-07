def luhns(cardno):
    sum=0
    while(cardno>0):
        digit1=cardno%10
        cardno=cardno//10
        digit2=cardno%10
        cardno=cardno//10
        digit2=digit2*2
        if(digit2>9):
            r=digit2%10
            digit2=digit2//10
            digit2=digit2+r
        sum=digit1+digit2+sum
    if(sum%10==0):
        print("It is a valid card number")
    else:
        print("No, it is not a valid card number")
card=int(input("Enter card number: "))
luhns(card)
