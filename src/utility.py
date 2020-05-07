from os import name, system

# Clear terminal, regardless of platform

def clear_terminal():
  if name == 'nt':
    # Win
    system('cls')
  else:
    # Mac/Linux
    system('clear')
    