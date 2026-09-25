number = int(input("Enter the first number."))
number2 = int(input("Enter the second number."))

factor = []
factor2 = []
gcf = []

for i in range(1, number + 1):
    if number % i ==0:
        factor.append(i)


for i in range(1, number2 + 1):
    if number % i ==0:
        factor2.append(i)

x = 0 
for i in range(len(factor)):
    for i in range(len(factor2)):
        if factor[x] == factor2[i]:
            gcf.append(factor2[x])
    x+=1

print(f"The greatest common factor is {gcf[-1]}.")