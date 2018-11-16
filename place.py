######################################################################
# Author: Emily Lovell & Scott Heggen
# Username: lovelle & heggens
#
# Assignment: T10: Oh, the Places You'll Go! (Refactored!)
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

class Place:
    """
    A class to represent a place.
    """

    def __init__(self, place_name="", loc="", lat=0, long=0, col="black"):
        """
        Create a new place, given a name, location, latitude, longitude, and pin color.

        :param place_name: Name of person associated with a place
        :param loc: Name/description of the place
        :param lat: Latitude of the place
        :param long: Longitude of the place
        :param col: Color of the pin that mark the place on the map
        """
        self.name = place_name
        self.location = loc
        self.latitude = lat
        self.longitude = long
        self.color = col

    def extract_place(self, file_content):
        """
        Extract the next place from the open file.

        :param file_content: A specified file that has been opened for reading
        :return:
        """
        self.name = file_content.readline().strip("\n")
        self.location = file_content.readline().strip("\n")
        self.latitude = float(file_content.readline().strip("\n"))
        self.longitude = float(file_content.readline().strip("\n"))
        self.color = file_content.readline().strip("\n")
