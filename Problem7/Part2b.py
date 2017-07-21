r"""
The Flexible and Fearful Adopters
20.0/20.0 points (graded)
Now that you have written the base class for the adopter types, we want to represent different personalities and traits.
The next two types of adopters will be the FlexibleAdopter and the FearfulAdopter, and both will be subclasses of the base Adopter class.

The Flexible Adopter

The FlexibleAdopter varies from the regular Adopter because a FlexibleAdopter is able to specify more than one species that they are interested in, but will still have one preferred species.
The FlexibleAdopter is a subclass of the Adopter class, and should inherit from it and only it. The FlexibleAdopter's __init__ method should look like the following:

__init__(self, name, desired_species, considered_species)

All of the inputs are the same as the Adopter class, except that considered_species is a list of strings of alternative species that the person is interested in adopting.

The FlexibleAdopter's scoring method also differs from the Adopter's scoring method. You should override the method so that a score calculated on a FlexibleAdopter will return a value that is
the result of adopter_score+0.3∗num_other where:

adopter_score is the value that the Adopter class's score method returns
num_other is the number of animals the adoption center has of all the other considered species
Note that since considered_species is a list, you will have to iterate over the values to get the total number of considered pets that a specific adoption center has.
The scoring method should take only one argument, the AdoptionCenter instance to calculate the score from.

Below, please write your implementation of the FlexibleAdopter class, including its __init__ method and its get_score(adoption_center) method.

The Fearful Adopter

The FearfulAdopter varies from the regular Adopter because a FearfulAdopter is afraid of one certain species of animal. While they may visit an AdoptionCenter that houses one or more of the
feared species, their enthusiasm to visit the AdoptionCenter is reduced. The FearfulAdopter is a subclass of the Adopter class, and should inherit from it and only it.
The FearfulAdopter's __init__ method should look like the following:

__init__(self, name, desired_species, feared_species)

All of the inputs are the same as the Adopter class, except that feared_species is a string that is the name of the feared species.

The FearfulAdopter's scoring method also differs from the Adopter's scoring method. You should override the method so that a score calculated on a FearfulAdopter will return a value that
is the result of adopter_score−0.3∗num_feared where:

adopter_score is the value that the Adopter class's score method returns
num_feared is the number of animals the adoption center has of the feared species
The scoring method should take only one argument, the AdoptionCenter instance to calculate the score from.

Below, please write your implementation of the FearfulAdopter class, including its __init__ method and its get_score(adoption_center) method.
"""

class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        num_other = sum(adoption_center.get_species_count().get(c, 0) for c in self.considered_species)
        return Adopter.get_score(self, adoption_center) + 0.3*num_other

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
    def get_score(self, adoption_center):
        num_feared = adoption_center.get_species_count().get(self.feared_species, 0)
        result = Adopter.get_score(self, adoption_center) - 0.3 * num_feared
        if result > 0:
            return result
        return 0.0
