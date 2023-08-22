import random
guess = input("Guess a letter ? ").lower()
names=["josiah",'mendy','ifeoma','jerry']
str="john"
chosen=random.choice(names)
for m in chosen:
    if guess == m:
        print("right!")
    else:
        print('wrong!')    
