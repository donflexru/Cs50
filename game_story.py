print("Welcome To Treasure Island! your mission is to find treasure")
direction=input("left or right ?").lower()
if direction=="left":
    action=input("swim or wait?").lower()
    if action=="wait":
      chose=input("Which door? Red, Blue or Yellow ?").lower()
      if chose=="yellow":
        print("congratulation you won!")
      else:
        print("Game over!")  
    else:
        print("Game over!")    
else:
    print("Game over!")
