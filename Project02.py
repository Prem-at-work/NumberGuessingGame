import random
n = random.randint(1, 100)
a = -1
Guess = 0
while (a!=n):
  a = int(input("Guess the number: "))
  if (a>n):
    print("Lower number please")
    Guess+=1
  else:
    print("Higher number please")
    Guess+=1

print(f"You guess the right number({n}) in {Guess} attempts")