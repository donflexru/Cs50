# arr=[]
# add=0
# for n in range(6):
#    pick=arr.append(n)
# print(arr) //[0, 1, 2, 3, 4, 5]
students_height=input("Enter the students height ").split()
total_height=0
number_of_students=0
for height in students_height:
    total_height+=int(height)
for number in students_height:
    number_of_students+=1  
avg_height=round(total_height/number_of_students) 
print(avg_height) 
# print(total_height) 
# print(number_of_students) 



