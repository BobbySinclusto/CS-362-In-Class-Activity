n = int(input("Enter the number to display divisors for: "))
for i in range(1, n+1):
    if n % (i) == 0:
        print(i)
