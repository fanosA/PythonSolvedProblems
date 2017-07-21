r"""
Part 3 - Connecting Adopters and Adoption Centers
20.0/20.0 points (graded)
Now that you have implemented both the AdoptionCenter and the different types of Adopters, it is time to try to adopt out some pets!

We will deal with two scenarios, one from the perspective of the Adopter type, and one from the perspective of an AdoptionCenter.

Help an Adopter visit AdoptionCenters in the Best Order

An Adopter or Adopter Subclass has a list of AdoptionCenters in the area, as well as information on what animals each AdoptionCenter has that day.
Write a method that will return an organized the list of the AdoptionCenters in such a way that the scores unique to the Adopter or Adopter Subclass for the AdoptionCenter will be ordered from
highest score to lowest score.

Write the method get_ordered_adoption_center_list(adopter, list_of_adoption_centers) with the following parameters:

adopter - A single Adopter or Adopter Subclass instance
list_of_adoption_centers - A list of AdoptionCenter instances.
The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
In case of ties, order the adoption center names alphabetically.

Help an AdoptionCenter Select Adopters

Using the methods that you have been given, you want to help organize a list of Adopter types for an AdoptionCenter to send advertisements which will invite them to visit the AdoptionCenter.
The AdoptionCenters may have limited funds and can only send out mail to a select few Adopters in their database, so want to select the best candidates to advertise to in order to increase the odds of adoption.

Your task is to write a method get_adopters_for_advertisement(adoption_center, list_of_adopters, n). The method should return a list of length n that represents the highest scoring Adopters/Adopter Subclasses for the specific AdoptionCenter (You want to find the top n best Adopter matches). Write the method get_adopters_for_advertisement(adoption_center, list_of_adopters, n) with the following parameters:

adoption_center - A single AdoptionCenter instance
list_of_adopters - A list of Adopter (or a subclass of Adopter) instances.
n - The number of adopters to return to send advertisements to (n <= 0, note that n can be larger than the length of list_of_adopters)
The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score). In case of ties, order the Adopter names alphabetically.
"""

def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
   The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
   """
    def get_score_key(var):
        return adopter.get_score(var)
    def get_name_key(var):
        return var.get_name()
    s = sorted(list_of_adoption_centers, key=get_name_key)
    return sorted(s, key=get_score_key, reverse=True)

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
   The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
   """
    def get_score_key(var):
        return var.get_score(adoption_center)
    def get_name_key(var):
        return var.get_name()
    s1 = sorted(list_of_adopters, key=get_name_key)
    s2 = sorted(s1, key=get_score_key, reverse=True)
    if n > len(s2): return s2
    return s2[:n + 1]
