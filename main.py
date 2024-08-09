import random 
turns = 1
r = random.randint(0,100)
v1 = int(input("pick a number between 0-100:"))
while v1 != r:
    turns = turns + 1
    if v1 < r:
        print("Too low, again")
    else:   
        print("Too high, again")
    v1 = int(input())
print("Congrats!!")
print("you took"+ str(turns))
