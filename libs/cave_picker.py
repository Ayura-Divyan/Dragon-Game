import random

def pick_cave(cave_number):
    """The fuction that picks the cave which cave is safe"""
    safe_cave = random.randint(1,2)
    
    if cave_number == safe_cave:
        print("You approach the cave...")
        print("A large dragon jumps out in front of you! He opens his jaws and...")
        print("Gives you his treasure!")
    else:
        print("You approach the cave...")
        print("A large dragon jumps out in front of you! He opens his jaws and...")
        print("Gobbles you down in one bite!")