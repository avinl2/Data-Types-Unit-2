bill = int(input("Please enter your bill value."))
tip = input("Please enter the service value. (bad, okay, good, great)")
bad = (0.00)
okay = (0.15)
good = (0.20)
great = (0.25)
if tip == "bad":
    print(bad*bill)
if tip == "okay":
    print(okay*bill)
if tip == "good":
    print(good*bill)
if tip == "great":
    print(great*bill)