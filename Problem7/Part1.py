r"""
The Adoption Center
10.0/10.0 points (graded)
The adoption center class will hold information specific to each adoption center, as well as methods for fetching information from or modifying the adoption center.

We want to store this information in an object that we can then pass around in the rest of our program. Your task, in this problem, is to write a class, AdoptionCenter,
starting with a constructor that takes (name, location, species_count) as arguments and stores them appropriately. You will also write some methods, detailed later on in this section.

Adoption Center Initialization

The following information should be stored in an AdoptionCenter instance, and passed in as its initialization variables: __init__(self, name, species_types, location)

name- A string that represents the name of the adoption center
location- A tuple (x, y) That represents the x and y as floating point coordinates of the adoption center location.
species_types- A string:integer dictionary that represents the number of specific pets that each adoption center holds. An example would be: {"Dog": 10, "Cat": 5, "Lizard": 3},
and another example would be {"Cat": 10, "Horse": 8}. Species names will always begin with a capital letter followed by lowercase letters,
so you do not have to check for the case of the species name ('Cat' will never be stored as 'cat' or 'cAT' etc). Note that the specific animals tracked depend on the adoption center.
If an adoption center does not have any of a specific species up for adoption, it will not be represented in the dictionary.
Adoption Center Methods

The following methods should be implemented for the AdoptionCenter class. The solution to this problem should be relatively short and
very straightforward (please review what get methods should do if you find yourself writing multiple lines of code for each).

get_name()- Returns the name of the adoption center
get_location()- Returns the location of the adoption center
get_species_count()- Returns a copy of the full list and count of the available species at the adoption center.
get_number_of_species(species_name)- Returns the number of a given species that the adoption center has.
adopt_pet(species_name)- Decrements the value of a specific species at the adoption center and does not return anything.
"""

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location
    def get_number_of_species(self, animal):
        return self.species_types.get(animal, 0)
    def get_location(self):
        return (float(self.location[0]), float(self.location[1]))
    def get_species_count(self):
        return self.species_types.copy()
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        if species in self.species_types:
            self.species_types[species] -= 1
        if self.species_types[species] == 0:
            del self.species_types[species]
