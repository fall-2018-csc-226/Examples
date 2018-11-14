######################################################################
# Author: Emily Lovell & Scott Heggen      TODO: Change this to your names
# Username: lovelle & heggens             TODO: Change this to your usernames
#
# Assignment: T10: Oh, the Places You'll Go!
#
# Purpose:  To create a map of locations
#           where the user is originally from or has visited,
#           and to use tuples and lists correctly.
######################################################################
# Acknowledgements:
#
# Original Authors: Dr. Scott Heggen and Dr. Jan Pearce

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
from place import *

class WorldMap:
    def __init__(self, input_file):
        self.filename = input_file
        self.file_content = ""
        self.wn = turtle.Screen()
        self.pin = turtle.Turtle()
        self.place = None
        self.all_places = []

        self.wn = turtle.Screen()
        self.wn.setup(width=1100, height=650, startx=0, starty=0)
        self.wn.bgpic("world-map.gif")
        self.wn.title("Oh, the Places You'll Go!")

    def parse_file(self):
        """
        Iterates through the file, and creates the list of places

        :param filename: the name of the file to be opened
        :return: a list representing multiple places
        """

        #####################################################
        # You do not need to modify this function!
        #####################################################

        self.file_content = open(self.filename, 'r')           # Opens file for reading

        str_num = self.file_content.readline()           # The first line of the file, which is the number of entries in the file
        str_num = int(str_num[:-1])                 # The '/n' character needs to be removed

        places_list = []
        for i in range(str_num):
            self.place = Place()
            self.place.extract_place(self.file_content)
            self.all_places.append(self.place)         # Assembles the list of places

        self.file_content.close()

    def place_all_pins(self):
        # Iterates through each item in the place_list list, calling the place_pin() function
        for place in self.all_places:
            self.place_pin(place)  # Adds ONE place to the map for each loop iteration


    def place_pin(self, place):
        """
        This function places a pin on the world map.

        :param window: the window object where the pin will be placed
        :param place: a tuple object describing a place to be put on the map
        :return: None
        """

        #####################################################
        # You do not need to modify this function!
        #####################################################

        self.pin.penup()

        self.pin.color(place.color)                     # Set the pin to user's chosen color
        self.pin.shape("circle")                     # Sets the pin to a circle shape

        # Logically, the denominator for longitude should be 360; lat should be 180.
        # These values (195 and 120) were determined through testing to account for
        # the extra white space on the edges of the map. You shouldn't change them!

        self.pin.goto((place.longitude / 195) * self.wn.window_width() / 2, (place.latitude / 120) * self.wn.window_height() / 2)
        self.pin.stamp()                             # Stamps on the location

        text = "{0}'s place:\n    {1}".format(place.name, place.location)   # Setting up pin label
        self.pin.write(text, font=("Arial", 10, "bold"))                 # Stamps the text describing the location






def main():
    """
    This program is designed to place pins on a world map.
    Each place is represented as a tuple.
    Each tuple is then added to a list.
    The list of tuples is used to populate the map.

    :return: None
    """

    # The next three lines set up the world map

    # A sample file was created for you to use here: places.txt
    in_file = input("Enter the name of the file: ")

    wm = WorldMap(in_file)
    wm.parse_file()        # generates place_list from the file
    wm.place_all_pins()

    print("Map created!")
    wm.wn.exitonclick()


if __name__ == "__main__":
    main()
