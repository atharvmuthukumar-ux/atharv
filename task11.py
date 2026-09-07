import math
txt=input("Enter the paragraph to be tested: ")
sentence_count=txt.count('.')+txt.count('!')+txt.count('?')
word_count=txt.count(' ')+(txt.count('.')-(sentence_count-1))+txt.count('-')
character_count=len(txt) - txt.count(' ') - txt.count('.') - txt.count('-')
L=(character_count/word_count)
S=(sentence_count/word_count)
CLI=(0.0588*L*100)-(100*0.296*S)-(15.8)
print(CLI)
if (CLI<6):
    print("5th Grade and below. Very easy to read")
elif (6<=CLI<8):
    print("6th to 7th Grade. Fairly easy to read")
elif (8<=CLI<10):
    print("8th to 9th Grade. Plain English")
elif (10<=CLI<13):
    print("10th to 12th Grade. Fairly difficult to read")
elif (13<=CLI<16):
    print("College. Difficult to read")
else:
    print("College Graduate. Very difficult to read")