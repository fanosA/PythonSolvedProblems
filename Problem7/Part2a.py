r"""
Meet the Adopter
10.0/10.0 points (graded)
There are a few types of potential adopters. The base class of the adopters is simply called "Adopter", which you will write below.
The Adopter class will contain information that will be shared among all types of adopters.

Adopter Initialization

The following information should be stored in an Adopter instance, and passed in as its initialization variables:

__init__(self, name, desired_species):

name- A string that represents the name of the adopter
desired_species- A string that represents the desired species to adopt
Adopter Methods

The following methods should be implemented for the Adopter class

get_name() - Returns the name of the adopter
get_desired_species() - Returns the desired species of the adopter
get_score(adoption_center) - Returns the score (details below)
About Scoring

Each Adopter class, and each Adopter subclass will have its own scoring methods. The minimum value that a score can be is 0, and there is no upper bound.
The score method will take in an adoption_center as its argument, and will do some calculations to determine how good of a fit the specific adopter is to the specific adoption center.
"""

class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        return 1.0*adoption_center.get_species_count().get(self.desired_species)
