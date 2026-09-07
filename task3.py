n = input("Enter a number: ")
i = 1
increasing = False
decreasing = False

# Increasing part
while i < len(n) and n[i] >= n[i - 1]:
    if n[i] > n[i - 1]:
        increasing = True
    i += 1

# Decreasing part
while i < len(n) and n[i] <= n[i - 1]:
    if n[i] < n[i - 1]:
        decreasing = True
    i += 1

if i == len(n) and increasing and decreasing:
    print("Hill Number")
else:
    print("Not a Hill Number")