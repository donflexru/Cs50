import random
names=input("Give everybody a name ")
names_split = names.split(", ")
name_len=len(names_split)
name_chosen = random.randint(0, name_len - 1)
# print(name_chosen)
person_to_pay=names_split[name_chosen]
print(f"{person_to_pay} is going to pay the meals")