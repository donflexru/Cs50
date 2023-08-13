print(round(1/3, 2)) # round to two decimal numbers
print(round(3.785605, 3)) # round to two decimal numbers
print(13//7) # flooring  to one significant num 
result=12/6
result/=2 # dividing the numbers  with it's variables 
print(result)
var = 12
var-=3
var+=var
print(var)

yrs_as_int=int(input("Enter your  current age please"))
yrs_rem=120-yrs_as_int
days_rem=yrs_rem*365
weeks_rem=yrs_rem*52
months_rem=yrs_rem*12
message=f"you have {days_rem} days, {weeks_rem} weeks, {months_rem} months, {yrs_rem} years"
print(message)