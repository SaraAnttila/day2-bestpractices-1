"""
Package with types of mammals
"""

class Mammals:
    def __init__(self):
        """
        Construct this class by creating member animals
        """
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t{}'.format(member))
