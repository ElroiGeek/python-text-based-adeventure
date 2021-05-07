
answer = input("would you like to play? [yes/no]")

if answer.lower().strip == "yes":
    
    answer = input("You reached a crossroad, would you like to go left or right?").lower().strip
    if answer == "left":
        answer = input("You encounterd a monster, would ou like to run or attack it.")
        
        if answer == "attack":
            print("That was not the greatest idea, you lost!")
        else:    
            print("Good choice, you made it away safely.")
            
            
    elif answer == "right":
        print("You walk aimlessly to the right and fall on a patch of ice. You injured your leg and cannot continue. Game Over!")
    else:
        print("Invalid choice, you lost!")
  
