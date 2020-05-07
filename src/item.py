# needs to have an Item class
# Item should have name and description
# This will be a base class for other items to inherit attributes and methods from later
# Will need to be able to add items to the player's inventory.
# Items can be in a 'list' of items associated with the player object, similar to how items can be 'in' a room.
# Item will need an on_take method to be called when the item is picked up by the player.
# on_take will print out a "You have picked up [ITEM_NAME]".  
# The item can also use this method to run additional code.
# Also add on_drop.
# Add support for the drop command, followed by an item name.

class Item:
  def __init__(self, name, description, current_location=None):
    self.name = name
    self.description = description,
    self.current_location = current_location
