# ############# Header to describe what the program does ##############################################################################################

    # Task [NUMBER e.g.04] - [DESCRIPTION - e.g. Data Types and Conditional Statements]
    # Practical Task [NUMBER e.g 2 - (depending on the Task)]
    # --------------------------------------------------------------------------------------------------------------------------------------------------------

    # Pseudocode:
    # START


    # END


# ############# Initial clear screen ##############################################################################################

import os

# Clear the terminal window for clarity. This is an improved version that works with both windows and unix/mac
os.system('cls' if os.name == 'nt' else 'clear')

# Add this \/[down] to the end of a function, especially when checking for the correctness of input with a 'while loop' #########

# # Clear the screen for the next iteration
# input("Press Enter to continue...")
# os.system('cls' if os.name == 'nt' else 'clear')
##################################################################################################################################

# ############# Validate numerical input ############################################################################################
#  Works very well with menus
def get_num_input(prompt):
    """
    Get numeric input from user. If non-numeric input is given user will be
    prompt to enter another value.

    prompt : str - Prompt to provide user for input.
    """
    while True:
        user_input = input(prompt)
        if user_input.lstrip("-").isnumeric():
            return int(user_input)
        print("Invalid input, please use numbers only!")

get_num_input("Hello: ")
