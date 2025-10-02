#Import libs
import libs.cave_picker as cave

cave_number = 0
# Start of the game
print(r"""
  _____                                 _____                      
 |  __ \                               / ____|                     
 | |  | |_ __ __ _  __ _  ___  _ __   | |  __  __ _ _ __ ___   ___ 
 | |  | | '__/ _` |/ _` |/ _ \| '_ \  | | |_ |/ _` | '_ ` _ \ / _ \
 | |__| | | | (_| | (_| | (_) | | | | | |__| | (_| | | | | | |  __/
 |_____/|_|  \__,_|\__, |\___/|_| |_|  \_____|\__,_|_| |_| |_|\___|
                    __/ |                                          
                   |___/                                           

      """)

print("""You are in the Kingdom of Dragons. 
In front of you, you see two caves. 
In one cave, the dragon is friendly and will 
share his treasure with you. 
The other dragon is hungry and will eat you on sight""")
print("")


while True:
    cave_number = int(input("Cave 1 or 2: "))
    if cave_number in [1, 2]:
        break
    
cave.pick_cave(cave_number)