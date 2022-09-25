# Getting the modules.
import random
import time

# Python making a random choice from a list.
def game_starting():
    list_game_options = ["Rock", "Paper", "Chizzle"]
    bot_output = random.choice(list_game_options)
    return bot_output

# Getting user input.
print("Rock, paper or chizzle?")
user_input = input("> ")
user_input = user_input.lower()

# Run the function to let python make a random choice.
print("Now its the computers turn!")
time.sleep(0.2)
get_computer_response = game_starting()

# Logic behind Rock, paper, scissors.
if get_computer_response == user_input:
    print(f"The computer picked {get_computer_response} so it's a tie!")
    
elif user_input == "rock":
    if get_computer_response == "Paper":
        print(f"Shit, you lose! computer did go for {get_computer_response}")
    else:
        print(f"You won! Jihaaaa, computer did chose for: {get_computer_response}")    
    
elif user_input == "paper":
    if get_computer_response == "Chizzle":
        print(f"Shit, you lose! computer did go for {get_computer_response}")
    else:
        print(f"You won! Jihaaaa, computer did chose for: {get_computer_response}")    
        
elif user_input == "chizzle":
    if get_computer_response == "Rock":
        print(f"Shit, you lose! computer did go for {get_computer_response}")
    else:
        print(f"You won! Jihaaaa, computer did chose for: {get_computer_response}")         
        
# With love made by Kelvin (ITKDR).
