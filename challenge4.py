number = int(input("Enter the first number."))
value = int(input("Enter the second number."))

factor = []
factor2 = []
gcf = []

for i in range(1, number + 1):
    if number % i ==0:
        factor.append(i)


for i in range(1, value + 1):
    if number % i ==0:
        factor2.append(i)

