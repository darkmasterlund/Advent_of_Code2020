# Class for bags Advent of Code

class bag:

    def __init__(self, color, contains):
        # String
        self.color = color
        # List of strings
        self.contains = contains

    def clean_contains(self):
        # This method takes the variable self.contains, a list of strings provided my instruction
        # and turns it into a dictionary of {bag name : num bags}
        # Create empty dictionary
        new_contains = {}

        # For each bag in the contains list update the dictionary
        for bg in self.contains:

            try: new_contains.update({bg[3:].replace('.', '').replace('bags','bag'):int(bg[1])})
            except: new_contains.update({'none':0})

        # Set self.contains to the new dictionary
        self.contains = new_contains
