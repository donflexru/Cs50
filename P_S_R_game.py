import random
user_choice=int(input("what do you choose type 0 for Rock, 1 for Paper or 2 for Scissors ? "))
if user_choice == 1:
    print("Paper")
elif user_choice == 2:
    print("Scissors")
elif user_choice == 0:
    print("Rock") 
else:
    print("you typed an invalid number")  

system_choice = random.randint(0,2) 
if system_choice == 1:
    print("Paper")        
elif system_choice == 2:
    print("Scissors")
else:
    print("Rock")    
if user_choice > 2:
    print("you lose")  
elif user_choice == 1 and system_choice == 2 or user_choice == 0 and system_choice == 1 or user_choice == 2 and system_choice == 0:
    print("you lose")
elif user_choice == 1 and system_choice == 0 or user_choice == 2 and system_choice == 1 or user_choice == 0 and system_choice == 2:
     print("you win")
else:
    print("play again")           
