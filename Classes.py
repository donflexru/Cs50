class piont():
    def __init__(self, input1, input2):
      self.x = input1
      self.y = input2
    
p=piont(3,7)
print(p.x)    
print(p.y)    

class Flight():
   def __init__(self, Capacity):
      self.Capacity=Capacity
      self.passengers=[]
   def add_passenger(self, name):
      if not self.Open_seats():
         return False
      self.passengers.append(name)
      return True
   
   def Open_seats(self):
     return self.Capacity-len(self.passengers)

fight=Flight(3)
people=["Harry","Abraham","Jessica","Monday"]
for person in people:
    success=fight.add_passenger(person)
    if(success):
      print(f"{person} has been succesfully added to the flight")      
    else:
       print(f"{person} no seats available")
   
