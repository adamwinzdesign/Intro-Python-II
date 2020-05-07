# Implement a class to hold room information. This should have name and
# description attributes.
# Room needs attributes that point to other rooms where appropriate, ex n_to, s_to, e_to, w_to
# Room needs to extend the class with list that holds the items that are currently in the room
# Add functionality to the main loop that prints out all the items that are visible to the player when they enter the room.

class Room:
  def __init__(self, name, description, items=None):
    self.name = name
    self.description = description
    self.items = items

  def __str__(self):
    return f'{self.name}'

  def print_description(self):
    return f"{self.description}"