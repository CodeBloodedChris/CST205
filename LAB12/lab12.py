#Lab 12
#Team Code Blooded
import time

#Class for creating an object that represents a room in a text-based adventure game.
class Room:
    __instances = []
    
    #Initializes room object with optional title and description.
    def __init__(self, title = "", description = "", inventory = ""):
      Room.__instances.append(self)
      self.index = Room.__instances.index(self)
      self.title = title
      self.description = description
      self.connections = {'N':'', 'E':'', 'S':'', 'W':'', 'U':'', 'D':''} #defines moveable directions
      self.inventory = inventory #Defines interactable objects inside the room.
    
    #Generates the string that displays information about where the player can go from the room.
    def __genConString(self):
      connection_string = "You can go "
      if self.connections['N'] != "": connection_string += "North, "
      if self.connections['S'] != "": connection_string += "South, " 
      if self.connections['E'] != "": connection_string += "East, " 
      if self.connections['W'] != "": connection_string += "West, " 
      if self.connections['U'] != "": connection_string += "Up, " 
      if self.connections['D'] != "": connection_string += "Down, "
      connection_string = connection_string[:-2]
      connection_string += ".\n"
      last_comma = connection_string.rfind(",")  
      if last_comma != -1: connection_string = connection_string[:last_comma] + ", and" + connection_string[last_comma + 1:]
      if connection_string.count(",") == 1:
        last_comma = connection_string.rfind(",")
        connection_string = connection_string[:last_comma] + "" + connection_string[last_comma + 1:]    
      return connection_string
    
    #Connects a room object to another room object using the built-in directions N,S,E,W,U,D.            
    def connectRoom(self, index, direction, both_ways = true):
      assert index + 1 <= len(Room.__instances) , "Not a valid connection! Connecting room does not exist!"
      
      direction = direction.upper()
      assert direction in self.connections.keys(), "Not a valid direction!"
      self.connections[direction] = index
      
      if both_ways == true:
        if direction == "N": Room.__instances[index].connections['S'] = self.index
        if direction == "S": Room.__instances[index].connections['N'] = self.index  
        if direction == "E": Room.__instances[index].connections['W'] = self.index  
        if direction == "W": Room.__instances[index].connections['E'] = self.index
        if direction == "D": Room.__instances[index].connections['U'] = self.index  
        if direction == "U": Room.__instances[index].connections['D'] = self.index
    
    #Returns a string containing the room title, description, and possible directions.        
    def outString(self):
      string = self.title + "\n\n"   
      string += self.description + "\n\n"
      string += self.__genConString()
      
      return string
      
    def getRoom(self, index):
      assert index + 1 <= len(Room.__instances) , "Not a valid room index!"
      return Room.__instances[index]     

#Class for the player. Defines player objects and their actions in a text-based adventure game.
class Player:
    
    def __init__(self, location):
      self.location = location #defines starting room. Location parameter requires room object.
      self.inventory = [] #defines the player's inventory.

    #Moves the player object to another room if the room has a connected room in the provided direction.   
    def move(self, direction):
      room = self.location
      direction = direction.upper()
      if direction in room.connections.keys() and room.connections[direction] != "":
        self.location = room.getRoom(room.connections[direction])
        return true
      else:
        return false

#Descriptions for each room stored in a multi-line triple quote string.
d1 = "You are coming home from work and hear something rustling inside. The door is locked, use your key to open the door."
d2 = """You sneak over to the fence that separates your house from the neighbors to the East of you. You've never trusted that strange family. You suspect they are all 
part of a traveling circus. That would explain their bearded mother and the siamese twin sisters. Who knows what else might be living with them. You inspect the fence 
for signs that anyone has climbed over or dug under. You find what appear to be the tracks of a flea, but can't be certain."""
d3 = """You enter the patio area and notice a nice picnic table.  On the northern wall you can see a nice barbecue.  You notice that the charcoal is slightly warm.  
When did I use my barbecue last? You notice windows on the east wall that allow you to see into the dining area.  Below the windows you notice a cooler that is empty.  
What happened to my beer?  To the east is the door back to the entrance of the house."""
d4 = """You enter the front of the house. The lights are off and for now, it is almost completely quiet. The faint sounds of a nearby clock's internal mechanisms are 
the only noise. To the west, the door to the patio is slightly ajar and a mild breeze is coming through. To the north lies the dining area."""
d5 = """Upon the entering the dining room, a sour, stale stench hits your face. What is that? Has some foul smelling creature been in here? Or do I just need to take 
out the garbage? You look around the room and notice what appear to be smudgy tracks leading outside throug the North door of the dining area. There is a bloody knife on the table. You might be able to use it."""
d6 = """You enter the gym.  You are immediately hit with the smell of musty towels.  From the west wall you hear the faint humming sound of a treadmill.  
Could someone have left it on?  Or did I forget to turn it off?  Near the dumbbell rack to the north is a door leading outside.  To the east is a door with a window that leads outside.  
You can see the pool house and the door leading to the dining area through it."""
d7 = """You step outside and notice the dim light of the neighbor's back portch illuminating the ground in front of you. There seems to be some muddy tracks leading into the Dining Area South. 
As you reach to close the door, smudges of what looks like mud are up aggainst it. There are also muddy tracks into the gym to the East. The light of the pool house is illuminating small puddles of water along the walkway leading into it to the North. 
Was someone already wet or just come out of the pool house? You can investigate the fence to the east for any clues regarding the wet floor."""
d8 = """You step outside and see the shed has been left alone to the North. The pool house to the East looks like someone was in there. The gym to the South has hardly been used since it was made a couple of days ago. 
There doesn't seem to be any obvious sign that someone walked through this area."""
d9 = """Upon entering the poolhouse, you notice the air is muggy and reeks of chlorine.  In the center of the room is a large rectangular pool.  
There is a stack of towels next to the northern door which leads outside.  You notice there are inner tubes stacked next to the western door which leads to an area between the gym and the shed.  
You also noticed wet footprints leading to the southern door which leads to the area between the poolhouse and the dining area.  Has someone been swimming in my pool?There seems to be some muffled 
noises coming from the pool house floor. Is that my imagination?"""
d10 = """The door creaks open as you enter a small shed. From the light coming through the door, you can barely make out what looks like a sea of tools filling up the room. 
You notice an old chainsaw sitting on the table in the back. It is clear from the amount of dust on everything that no one has been in here for quite some time."""
d11 = """You take a moment in the fresh breeze to clear your head. Surely you must be imaging all of this. You remember being haunted by something in the dark at camp as a 
little kid. No one else would believe you, but you know what you saw. Those terrible eyes and such sharp fangs. Could it be back? No, of course not. It couldn't possibly be... could it?!"""
d12 = """You approach a chain-link fence. The fence is in disrepair and no longer stands straight, but is still managing to do its job. 
In the distance over the fence, you can almost make out what appears to be a better game. Unfortunately, you have no way to get to it."""

#Alternate Room descriptions
alt5 = """Upon the entering the dining room, a sour, stale stench hits your face. What is that? Has some foul smelling creature been in here? Or do I just need to take 
out the garbage? You look around the room and notice what appear to be smudgy tracks leading outside throug the North door of the dining area. 
There was a knife on the table, but now you have it in your hand.  You should probably avoid going back to the front of the house."""
alt6 = """You are now able to enter your house"""
#Game begins here.
#Initiate the 12 room object instances 
r1 = Room("Front Porch", d1, "keys")
r2 = Room("East Fence", d2)
r3 = Room("Covered Patio", d3)
r4 = Room("Inside House", d4)
r5 = Room("Dining Area", d5, "knife")
r6 = Room("Gym", d6)
r7 = Room("Outside South", d7)
r8 = Room("Outside West", d8)
r9 = Room("Pool House", d9)
r10 = Room("Shed", d10, "chainsaw")
r11 = Room("Outside North", d11)
r12 = Room("North Fence", d12)

#Initiate the connections the rooms have with one another.
r1.connectRoom(r2.index,"e")
r1.connectRoom(r4.index,"n")
r4.connectRoom(r3.index,"w")
r4.connectRoom(r5.index,"n")
r7.connectRoom(r5.index,"s")
r7.connectRoom(r6.index,"w")
r7.connectRoom(r9.index,"n")
#r7.connectRoom(r2.index,"e") #Commented out because it won't let you return to the start
r8.connectRoom(r6.index,"s")
r8.connectRoom(r9.index,"e")
r8.connectRoom(r10.index,"n")
r11.connectRoom(r9.index,"s")
r11.connectRoom(r12.index,"n")

def printIntro():
  printNow("""Welcome to The Code Blooded House of Horror!
While in each room, you will be told which direction you can move. You can move in that direction by typing N for North, E for East, W for West and S for South.
Type help to return to these instruction anytime. Type exit to quit the game.\n""")
  time.sleep(1)

#takes an object from a room if applicable and adds it to player inventory
def takeObject(room, player):
  if room.inventory =="knife":
    player.inventory.append("knife")
    room.inventory = ""
    room.description = alt5
    printNow("You take the bloody knife from the table to use later just in case.")
  elif room.inventory == "":
    printNow("There is nothing you can take in this room")
#uses an item in a room
def useObject(room):
  if room.inventory == "":
    printNow("There is nothing to use in this room.")
  elif room.inventory == "chainsaw":
    printNow("After many attempts, you finally get the chainsaw running! It runs out of gas 5 seconds later.")
  elif room.inventory == "keys":
    room.description = alt6
    printNow("You feel a chill as you try to insert the key into the hole.")  
  
#Initate the player object.
player = Player(r1)
end = false #Variable to flag whether the player wishes to end the game and exit.
lose = false #Variable for the lose condition
win = false #Variable for the win condition
correctInput = "NSEW"

printIntro()

player.inventory
#Main while loop.
while end == false and lose == false:
  printNow(player.location.outString())
  command = requestString("What direction would you like to move?\nN = North\nE = East\nW = West\nS = South\n"+
  "'use' = use item in room\n'take' = take an item from the room\n'help' = instructions\n'exit' = quit game")
  if command.upper() == "EXIT":
    end = true
  elif command.upper() == "HELP":
    printIntro()
  elif command.upper() == "USE":
    useObject(player.location)
  elif command.upper() == "TAKE":
    takeObject(player.location, player)
  elif command.upper() in correctInput:
    player.move(command)
  else:
    printNow("I'm sorry, that's not a correct command... Please try again")
  if "knife" in player.inventory and player.location == r9:#the player wins after finding a bum in the hidden room under the pool
    win = true 
    break;
  if "knife" in player.inventory and player.location == r1:#The player loses if they take the knife and go to the front porch
    lose = true
    break; 
  
   
#end while loop check for conditions
if win:
  printNow("You find out there's a hidden room under the area next to the towels. After going down a small flight of stairs you find a " +
  "a mostly naked man saying he lived there before. You threaten him with the knife and he claims squatter's rights. Little did he know you are a lawyer.\n You Win!")
if lose:
  printNow("As you return to the front porch you are tackled by a passerby who sees the knife in your hands and mistakes you for a serial killer."+ 
  "He pins you down and calls the police. You are arrested and sent to jail.\n YOU LOSE.")
else:
  printNow("No one likes a quitter.")


