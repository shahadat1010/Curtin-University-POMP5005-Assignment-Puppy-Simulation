import matplotlib.patches as pat
import random

# Function to flip coordinates for plotting purposes
def flip_coords(pos, LIMITS):
    return((pos[1], pos[0]))

# Class representing a Puppy
class Puppy():
    """
    Holds information and behaviour of puppy creature
    """
    
    def __init__(self, name, colour, pos):
        # Initialize puppy attributes: name, colors, position, and hunger level
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
        self.hunger_level = 100

    def get_pos(self):
        # Return the current position of the puppy
        return self.pos

    def plot_me(self, ax, LIMITS):
        # Plot the puppy on the given axis with the specified limits
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0]-0.9, fpos[1]-0.3), height=2.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0]+0.9, fpos[1]-0.3), height=2.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)
        ax.annotate(self.name, (fpos[0]+0.9, fpos[1]-0.3))
        ax.annotate(self.hunger_level, (fpos[0]-2, fpos[1]-2))

    def chase_squirrel(self, creatures):
        # Check for nearby squirrels and chase them if close enough
        for creature in creatures:
            if isinstance(creature, Squirrel):
                if abs(creature.pos[0] - self.pos[0]) <= 3 and abs(creature.pos[1] - self.pos[1]) <= 3:
                    print(f"{self.name} Smells an {creature.name} ")
                    self.pos = creature.pos
                    self.hunger_level = 100
                    print(f"{self.name} caught and ate the squirrel! |Hunger Level:{self.hunger_level}")
                    creatures.remove(creature)
                    return True
        return False

    def run_to_toy(self, toys):
        # Check for nearby toys and run to them if close enough
        for toy in toys:
            if abs(toy.pos[0] - self.pos[0]) <= 3 and abs(toy.pos[1] - self.pos[1]) <= 1:
                self.pos = toy.pos
                Toy.step_change(self)
                self.hunger_level = self.hunger_level - 10
                print(f"{self.name} is chasing the {toy.name}! |Energy level:{self.hunger_level}")
                print(f"{self.name} is playing with the {toy.name}!")
                toy.step_change()
                return True
        return False

    def eat_squirrel(self, creatures):
        # Check if a squirrel is at the same position and eat it
        for creature in creatures:
            if isinstance(creature, Squirrel):
                if creature.pos == self.pos:
                    print(f"{self.name} caught and ate the squirrel!")
                    creatures.remove(creature)
                    return True
        return False

    def play_with_toy(self, toys):
        # Check for nearby toys and play with them if close enough
        for toy in toys:
            if abs(toy.pos[0] - self.pos[0]) <= 3 and abs(toy.pos[1] - self.pos[1]) <= 3:
                self.pos = toy.pos
                return True
        return False

    def step_change(self, smells, creatures, toys):
        # Perform one step of the puppy's behavior
        if self.chase_squirrel(creatures):
            return
        if self.run_to_toy(toys):
            return
        validmoves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        self.hunger_level = self.hunger_level - 5
        print(f"{self.name} is exploring |Energy level:{self.hunger_level}")
        if self.hunger_level < 50:
            print(f"{self.name} is hungry")

    def feed(self):
        # Feed the puppy if it's hungry
        if self.hunger_level > 50:  
            print(f"{self.name} is being fed! |Energy Level:{self.hunger_level}")
            self.hunger_level = 100  
        else:
            print(f"Human is playing with {self.name}")

# Class representing a Squirrel
class Squirrel():
    """
    Holds information and behaviour of squirrel creature
    """
    def __init__(self, name, colour, pos):
        # Initialize squirrel attributes: name, colors, and position
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        # Return the current position of the squirrel
        return self.pos

    def step_change(self, smells=None, animals=None, toys=None):  
        # Perform one step of the squirrel's behavior
        validmoves = [(1,0),(-1,0),(0,-1),(0,1)]
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if smells is not None and animals is not None:
            for c in animals:
                if isinstance(c, Puppy):  
                    dist = abs(self.pos[0] - c.pos[0]) + abs(self.pos[1] - c.pos[1]) 
                    if dist <= 4:   
                        if self.pos[0] < c.pos[0]:
                            move = (-1, 0)  
                        else:
                            move = (1, 0)  
                        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
                        print(f"{self.name} smells Dog Nearby , He is running away!")

    def plot_me(self, ax, LIMITS):
        # Plot the squirrel on the given axis with the specified limits
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]-0.9, fpos[1]-0.3), radius=0.5, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]+0.9, fpos[1]-0.3), radius=0.5, color=self.colour2)
        ax.add_patch(patch)
        ax.annotate(self.name, (fpos[0]+0.9, fpos[1]-0.3))

# Class representing a Human
class Human():
    """
    Holds information and behaviour of human creature
    """
    def __init__(self, name, role, colour, pos):
        # Initialize human attributes: name, role, colors, and position
        self.name = name
        self.role = role
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        # Return the current position of the human
        return self.pos
    
    def feed_puppy_if_close(self, puppies):
        # Feed nearby puppies if they are close enough
        for puppy in puppies:
            if abs(puppy.pos[0] - self.pos[0]) <= 2 and abs(puppy.pos[1] - self.pos[1]) <= 2:
                if self.role == "owner":
                    print(f"{self.name} is whistling at {puppy.name}")
                    puppy.feed()
                    return True
                else: 
                    print(f"{puppy.name} growling")
                    self.role = "owner"
                    print(f"{self.name} is trying to pet {puppy.name}")
        return False

    def step_change(self, smells=None, animals=None, toys=None):
        # Perform one step of the human's behavior
        validmoves = [(1,0),(-1,0),(0,-1),(0,1)]
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if animals is not None:
            for c in animals:
                if isinstance(c, Puppy): 
                    if self.feed_puppy_if_close([c]):
                        return

    def plot_me(self, ax, LIMITS):
        # Plot the human on the given axis with the specified limits
        fpos = flip_coords(self.pos, LIMITS)
        # Head
        head = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(head)
        # Body
        body = pat.Rectangle((fpos[0] - 0.25, fpos[1] - 2), 0.5, 2, color=self.colour2)
        ax.add_patch(body)
        # Arms
        left_arm = pat.Rectangle((fpos[0] - 1.5, fpos[1] - 2), 1, 0.2, color=self.colour2)
        ax.add_patch(left_arm)
        right_arm = pat.Rectangle((fpos[0] + 0.5, fpos[1] - 2), 1, 0.2, color=self.colour2)
        ax.add_patch(right_arm)
        # Legs
        left_leg = pat.Rectangle((fpos[0] - 0.25, fpos[1] - 4), 0.5, 2, color=self.colour2)
        ax.add_patch(left_leg)
        right_leg = pat.Rectangle((fpos[0] - 0.25, fpos[1] - 4), 0.5, 2, color=self.colour2)
        ax.add_patch(right_leg)
        ax.annotate(self.name, (fpos[0]+0.9, fpos[1]-0.3))

# Class representing a Toy
class Toy():
    """
    Holds information and behaviour of toy object
    """
    def __init__(self, name, colour, pos):
        # Initialize toy attributes: name, colors, and position
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        # Return the current position of the toy
        return self.pos

    def step_change(self):
        # Perform one step of the toy's behavior
        validmoves = [(5,0),(-5,0),(0,-5),(0,5)]
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self, ax, LIMITS):
        # Plot the toy on the given axis with the specified limits
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=0.5, color=self.colour1)
        ax.add_patch(patch)
        football_shape = pat.Wedge((fpos[0], fpos[1]), r=0.3, theta1=45, theta2=135, color=self.colour1)
        ax.add_patch(football_shape)
        ax.annotate(self.name, (fpos[0]+0.9, fpos[1]-0.3))
