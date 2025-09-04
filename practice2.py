guess = 0
x = int(input("enter an integer:"))
while guess**2 < x:
    guess = guess + 1
if guess**2 == x:
    print("square root of",x , "is", guess)
else:
    print(x, "is not a perfect square")