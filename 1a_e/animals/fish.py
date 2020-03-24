"""
Package with types of fish
"""

class Fish:
    def __init__(self):
        """
        Construct this class by creating member animals
        """
        self.members = ['Salmon', 'Tuna', 'Clown fish']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t{}'.format(member))
