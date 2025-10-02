import random
import time

def pick_cave(cave_number):
    """The fuction that picks the cave which cave is safe"""
    safe_cave = random.randint(1,5)
    
    if cave_number == safe_cave:
        print("You approach the cave...")
        time.sleep(2)
        print("A large dragon jumps out in front of you! He opens his jaws and...")
        time.sleep(2)
        print("Gives you his treasure!")
    else:
        print("You approach the cave...")
        time.sleep(2)
        print("A large dragon jumps out in front of you! He opens his jaws and...")
        time.sleep(2)
        print("Gobbles you down in one bite!")