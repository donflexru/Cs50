class Room():
    def __init__(self,capacity):
       self.capacity=capacity
       self.room=[]
    def add_room(self, name):
     self.availability=self.capacity-len(self.room)
     if not self.availability:
       return False 
     self.room.append(name)
     return self.availability
Rooms=Room(1)
people=['Anderson','garry','Dean']
for person in people:
   if Rooms.add_room(person):
      print(f"{person} is added to the room")
   else:   
     print(f"{person} is  not added to the room")  