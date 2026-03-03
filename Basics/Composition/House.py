from Room import Room
class House:
    def __init__(self):
        self.rooms=[]
        self.rooms.append(Room("Living Room"))
        self.rooms.append(Room("Kitchen"))
        self.rooms.append(Room("Bedroom"))
    def getRooms(self):
        return self.rooms
    
if __name__=="__main__":
    # Create a house and print the names of its rooms
    # This demonstrates composition, where a house is composed of rooms.
    # without house, rooms cannot exist, and they are part of the house's structure.
    # they are not independent entities, but rather components of the house.
    house=House()
    rooms=house.getRooms()
    for room in rooms:
        print(room.getName())
    