import random

class Dragon:
    """ A class to represent all the dragons """

    def __init__(self, thename, num_wings = 0, legs = 0):
        """
        Creates a new dragon with a name, with options of defining number of wings and legs

        :param thename: The dragons name
        :param num_wings: The number of wings on the dragon
        :param legs: The number of legs on the dragon
        """
        self.scale_color = ""
        self.scale_shape = ""
        self.scale_type = ""
        self.wingspan = 0
        self.wing_count = num_wings
        self.weight = 0         # Notice we can't define units; this is where comments matter
        self.height = 0         # In inches
        self.leg_count = legs
        self.can_breath_fire = False
        self.name = thename

    def fly(self):
        """
        Make your dragon fly!

        :return: None
        """
        if self.wing_count > 0:
            print("I'm flying!")

    def breath_fire(self):
        """
        Make your dragon breathe fire!

        :return: None
        """
        if self.can_breath_fire:
            print("Burn!!!")

    def hoard_treasure(self, treasure):
        """
        Make your dragon hoard treasure.

        :param treasure: A treasure string
        :return: The treasure amount
        """
        treasure_amt = random.randint(1, 100)
        print("I get {1} of the {0}".format(treasure, treasure_amt))
        return treasure_amt

    def move(self, movement_type):
        """
        Moves your dragon around, based on the type of movement and the number of legs/wings

        :param movement_type: String representing walk/slither/fly
        :return: None
        """
        if movement_type == "walk":
            if self.leg_count > 0:
                print("Run, peon, run!!!")
        elif movement_type == "slither":
            if self.leg_count == 0:
                print("ssssstth")
            else:
                return "Error"
        else:
            if self.wing_count > 0:
                print("you're screwed")

mays_dragon = Dragon("Doug", 1)
mays_dragon.leg_count = 10
# mays_dragon.wing_count = 1
mays_dragon.can_breath_fire = True
mays_dragon.scale_color = "Cotton Candy Pink"
print("May has {0} wings".format(mays_dragon.wing_count))
print("May's dragon is {0}".format(mays_dragon.name))
wills_dragon = Dragon("Scott", legs = 40)
wills_dragon.height = 120
wills_dragon.weight = 150
# wills_dragon.wing_count = 13
print("Will's dragon has {0} wings".format(wills_dragon.wing_count))
print("Will's dragon has {0} legs".format(wills_dragon.leg_count))

if wills_dragon.wing_count > mays_dragon.wing_count:
    print("Fly {0} Fly!".format(wills_dragon.name))
else:
    print("Fly {0} Fly!".format(mays_dragon.name))

mays_loot = mays_dragon.hoard_treasure("Cotton Candy")
print("May got {0} cotton candies".format(mays_loot))
wills_dragon.move("slither")

mays_dragon.name = "Phyllis"
print("May's dragon had an identity crisis, and changed her name to {0}".format(mays_dragon.name))
