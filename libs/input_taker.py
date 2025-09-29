def validate_user_choice(cave_number):
    """This function will validate the user input"""  
    # Validation of input
    if cave_number != 1 and cave_number != 2:
        print("Invalid input. Please choose 1 or 2.")
        return validate_user_choice(cave_number=int(input("Cave 1 or 2: ")))
    else:
        return cave_number
