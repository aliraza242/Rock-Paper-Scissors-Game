''' R(Winner) = S(Runner)
    p(Winner) = R(Runner)
    S(Winner) = P(Runner) '''
    
import random    # Import a module
    
point_user = 0
point_computer = 0

while True:   # Infinite Loop
    user_input = input("Enter Your Choices [rock , paper , scissors] : ")  
    print()
    possible_choices = ["rock" , "paper" , "scissors"]
    computer_input = random.choice(possible_choices)         
  
    print(f"You choose : {user_input}\nComputer choose : {computer_input}")    

    if user_input == computer_input:                # conditions
        print(f"You both choose : {user_input}") 
    
    elif user_input == "rock":
        if computer_input == "scissors":       # When computer choose scissor then user win
            print("User wins , Rock will break the scissors")
            point_user += 1
        else:                              
            print("User loose , Paper will cover the rock")    
            point_computer += 1
    elif user_input == "paper":
        if computer_input == "rock":
            print("User wins , Paper will cover the rock")
            point_user += 1
        else:
            print("User loose , Scissor will cut the paper")
            point_computer += 1 
        
    elif user_input == "scissors":
        if computer_input == "paper":
            print("User wins , Scissor will cut the paper")
            point_user += 1
        else:
            print("User loose , Rock will break the scissors")   
            point_computer += 1

    play_again = input("Do you want to play again? (y/n) : ") 
    if play_again.lower() != "y":
        break

print(f"Total Points of user is : {point_user} and the computer is : {point_computer}") 