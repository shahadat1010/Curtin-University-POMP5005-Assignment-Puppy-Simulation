import matplotlib.patches as pat
import random

def flip_coords(pos, LIMITS):
    return (pos[1], pos[0])

class Puppy:
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        self.colour2 = csplit[1] if len(csplit) == 2 else csplit[0]
        self.pos = pos
        self.hunger_level = 100

    def get_pos(self):
        return self.pos

    def plot_me(self, ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0] - 0.9, fpos[1] - 0.3), height=2.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0] + 0.9, fpos[1] - 0.3), height=2.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)
        ax.annotate(self.name, (fpos[0] + 0.9, fpos[1] - 0.3))
        ax.annotate(self.hunger_level, (fpos[0] - 2, fpos[1] - 2))

    def chase_squirrel(self, creatures):
        for creature in creatures:
            if isinstance(creature, Squirrel):
                if abs(creature.pos[0] - self.pos[0]) <= 3 and abs(creature.pos[1] - self.pos[1]) <= 3:
                    print(f"{self.name} Smells an {creature.name}")
                    self.pos = creature.pos
                    self.hunger_level = 100
                    print(f"{self.name} caught and ate the squirrel!           |Hunger Level:{self.hunger_level}")
                    creatures.remove(creature)
                    return True
        return False

    def run_to_toy(self, toys):
        for toy in toys:
            if abs(toy.pos[0] - self.pos[0]) <= 3 and abs(toy.pos[1] - self.pos[1]) <= 1:
                self.pos = toy.pos
                toy.step_change()
                self.hunger_level -= 10
                print(f"{self.name} is chasing the {toy.name}!                       |Energy level:{self.hunger_level}")
                return True
        return False

    def step_change(self, smells, creatures, toys):
        if self.chase_squirrel(creatures):
            return
        if self.run_to_toy(toys):
            return

        validmoves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        self.hunger_level -= 5
        print(f"{self.name} is exploring                                     |Energy level:{self.hunger_level}")

    def feed(self):
        if self.hunger_level > 50:
            print(f"{self.name} is being fed!                        |Energy Level:{self.hunger_level}")
            self.hunger_level = 100
        else:
            print(f"Human is playing with {self.name}")

class Squirrel:
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        self.colour2 = csplit[1] if len(csplit) == 2 else csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

    def step_change(self, smells=None, creatures=None, toys=None):
        validmoves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

        if smells is not None and creatures is not None:
            for c in creatures:
                if isinstance(c, Puppy):
                    dist = abs(self.pos[0] - c.pos[0]) + abs(self.pos[1] - c.pos[1])
                    if dist <= 4:
                        if self.pos[0] < c.pos[0]:
                            move = (-1, 0)
                        else:
                            move = (1, 0)
                        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
                        print(f"{self.name} smells Dog Nearby, He is running away!")

    def plot_me(self, ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] - 0.9, fpos[1] - 0.3), radius=0.5, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] + 0.9, fpos[1] - 0.3), radius=0.5, color=self.colour2)
        ax.add_patch(patch)
        ax.annotate(self.name, (fpos[0] + 0.9, fpos[1] - 0.3))

class Human:
    def __init__(self, name, role, colour, pos):
        self.name = name
        self.role = role
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        self.colour2 = csplit[1] if len(csplit) == 2 else csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

    def feed_puppy_if_close(self, puppies):
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

    def step_change(self, smells=None, creatures=None, toys=None):
        validmoves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if creatures is not None:
            for c in creatures:
                if isinstance(c, Puppy):
                    if self.feed_puppy_if_close([c]):
                        return

    def plot_me(self, ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        head = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(head)
        body = pat.Rectangle((fpos[0] - 0.25, fpos[1] - 2), 0.5, 2, color=self.colour2)
        ax.add_patch(body)
        left_arm = pat.Rectangle((fpos[0] - 1.5, fpos[1] - 2), 1, 0.2, color=self.colour2)
        ax.add_patch(left_arm)
        right_arm = pat.Rectangle((fpos[0] + 0.5, fpos[1] - 2), 1, 0.2, color=self.colour2)
        ax.add_patch(right_arm)
        left_leg = pat.Rectangle((fpos[0] - 0.25, fpos[1] - 4), 0.5, 2, color=self.colour2)
        ax.add_patch(left_leg)
        right_leg = pat.Rectangle((fpos[0] - 0.25, fpos[1] - 4), 0.5, 2, color=self.colour2)
        ax.add_patch(right_leg)
        ax.annotate(self.name, (fpos[0] + 0.9, fpos[1] - 0.3))

class Toy:
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        self.colour2 = csplit[1] if len(csplit) == 2 else csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

    def step_change(self):
        validmoves = [(-5, 0), (5, 0), (0, 5), (0, -5)]
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self, ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=0.5, color=self.colour1)
        ax.add_patch(patch)
        football_shape = pat.Wedge((fpos[0], fpos[1]), r=0.3, theta1=45, theta2=135, color=self.colour1)
        ax.add_patch(football_shape)
        ax.annotate(self.name, (fpos[0] + 0.9, fpos[1] - 0.3))
