# Write a class to hold player information, e.g. what room they are in
# currently.
# Program should throw an error if player attempts to move where there is no room.
# Needs name and room

class Player:
  def __init__(self, name, room, inventory=None):
    self.name = name
    self.room = room
    self.inventory = inventory

  def move_to(self, direction, room):
      attribute = direction + '_to'

      if hasattr(room, attribute):
        return getattr(room, attribute)

      print('You look and see that there is not a way forward in that direction.\n')

      return room
