import random
word_list=["merry","palm","saving","sucess"]
chosen_word=random.choice(word_list)
display=[]
for _ in range(len(chosen_word)):
    display.append("_")
print(display) 
print(chosen_word) 
end_of_game=False
lives=6
while not end_of_game: 
  guess=input("Guess a letter ? ").lower()
  for position in range(len(chosen_word)):
      char=chosen_word[position]  
         #   print(f"current position: {position}\ncurrent letter: {char}  \ncurrent guess: {guess}")
      if char==guess:
          display[position]=char
       #   else:
    #       display[position]='_'    

  if guess not in chosen_word: 
     lives-=1
     
     if lives ==0:
        #   num=len(chosen_word)
        #   num=0
          end_of_game=True   
          print("You lose")
               
    
  print(f"{''.join(display)}")    
  if "_" not in display:
        print(display) 
        end_of_game=True   
        print("You've won")    
  

     

# for _ in range(5):
#     # display.append("_")
#     display+="_"
# print(display) 
# str='jmoss'
# guess="s"
# for char in str:
#     if char == guess:
#      display.append(char)
#     else:
#         display.append("_")   

# print(display)
