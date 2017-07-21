r"""
The Sluggish Adopter
10.0/10.0 points (graded)
The final type of adopter will be the SluggishAdopter, and it will extend the baseAdopter class.
A SluggishAdopter really dislikes travelling. The further away the adoption center is linearly, the less likely they will want to visit it.
Since we are not sure the specific mood the SluggishAdopter will be in on a given day, we will assign their score with a random modifier depending on distance as a guess.

The SluggishAdopter varies from the regular Adopter because a SluggishAdopter really dislikes travelling. The further away the adoption center is linearly,
the less likely they will want to visit it. Since we are not sure the specific mood the SluggishAdopter will be in on a given day, we will assign their score with a random modifier depending
on distance as a guess. The SluggishAdopter is a subclass of the Adopter class, and should inherit from it and only it. The SluggishAdopter's __init__ method should look like the following:

__init__(self, name, desired_species, location)

All of the inputs are the same as the Adopter class, except that location is a tuple of floats of the (x, y) coordinates, similar to the AdoptionCenter's location variable.
The range for the coordinates are -5.0 to 5.0.

For this adopter, you will have to write an additional class method called get_linear_distance(to_location), which will calculate the linear distance between two points, (x1,y1),(x2,y2).
You will want to calculate the distance by using the following formula:

d=(x2−x1)2+(y2−y1)2
This will be used calculate the linear distance between the SluggishAdopter, and the AdoptionCenter.

The SluggishAdopter's scoring method also differs from the Adopter's scoring method. You should override the method so that a score calculated on a SluggishAdopter will return a value that is:

1∗the_number_of_desired_species, if the distance is less than 1
random_value_between_0.7_and_0.9∗the_number_of_desired_species, if the distance is less than 3 but greater than or equal to 1
random_value_between_0.5_and_0.7∗the_number_of_desired_species, if the distance is less than 5 but greater than or equal to 3
random_value_between_0.1_and_0.5∗the_number_of_desired_species, if the distance is greater than or equal to five.
Hints on how to generate random numbers!
The scoring method should take only one argument, the AdoptionCenter instance to calculate the score from.

Hint: remember AdoptionCenter's get_location method!

Below, please write your implementation of the SluggishAdopter class, including its __init__ method, its get_linear_distance(to_location) method, and its get_score(adoption_center) method.
"""

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """

    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self, to_location):
        import math
        return math.sqrt((to_location[0] - self.location[0])**2 + (to_location[1] - self.location[1])**2)

    def get_score(self, adoption_center):
        import random
        distance = self.get_linear_distance(adoption_center.get_location())
        if distance < 1:
            return 1 * Adopter.get_score(self, adoption_center)
        if 1 <= distance < 3:
            return random.uniform(0.7, 0.9) * Adopter.get_score(self, adoption_center)
        if 3 <= distance < 5:
            return random.uniform(0.5, 0.7) * Adopter.get_score(self, adoption_center)
        if distance >= 5:
            return random.uniform(0.1, 0.5) * Adopter.get_score(self, adoption_center)
