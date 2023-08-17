print("Welcome to love calculator!")
partner=input("What is your name!").lower()
partner_2=input("What is your partner name!").lower()
# name_check="TRUE".lower()
# name_check_2="LOVE".lower()
combine_name=partner+partner_2
t=combine_name.count('t')
r=combine_name.count('r')
u=combine_name.count('u')
e=combine_name.count('e')

l=combine_name.count('l')
o=combine_name.count('o')
v=combine_name.count('v')
e=combine_name.count('e')
true=t+r+u+e
love=l+o+v+e
match_score=str(true)+str(love)
match_score=int(match_score)
if match_score < 10 or match_score > 90:
  print(f" Your score:{match_score} you go like coke and mentos")
elif match_score >= 40 or match_score <= 50:   
   print(f"Your score:{match_score} you are alright to go")
else:
    print(f"Your score:{match_score}")