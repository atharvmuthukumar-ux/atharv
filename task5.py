n=int(input("Enter the number of terms: "))
def fibonacci():
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
for i in range(n):
    print(fibonacci())