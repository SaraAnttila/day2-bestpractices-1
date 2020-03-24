"""
Package with types of birds
"""

class Birds:
    def __init__(self):
        """
        Construct this class by creating member animals
        """
        self.members = ['Sparrow', 'Robin', 'Duck']

    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t{}'.format(member))
