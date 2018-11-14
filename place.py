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

class Place:
    def __init__(self, place_name="", loc="", lat=0, long=0, col="black"):
        self.name = place_name
        self.location = loc
        self.latitude = lat
        self.longitude = long
        self.color = col

    def extract_place(self, file_content):
        self.name = file_content.readline().strip("\n")
        self.location = file_content.readline().strip("\n")
        self.latitude = float(file_content.readline().strip("\n"))
        self.longitude = float(file_content.readline().strip("\n"))
        self.color = file_content.readline().strip("\n")
