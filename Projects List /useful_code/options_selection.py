# This is a great way to implement selections in a menu.
# Normally it would be an if-statement but this uses 
# a dictionary and the .get method

MAIN_MENU = """Choose an option:
1. Add Movie
2. Update Movie Review or Rating
3. Search for a Movie
4. Display All Movies (Sorted by Ratings)
5. Remove a Movie
6. Recommend Movie
\n0. Exit
:"""


def a():
    print('a')

def b():
    print('b')

def c():
    print('c')

def d():
    print('d')

def default():
    print('Exiting... ')

option = input("Select an option (otherwise Default will be selected): ")

funcs= {'1': a, '2': b, '3': c, '4': d,'0': exit}
funcs.get(option, default)()
# Alternative to the last line: 
# f = funcs.get(option, default)  #without the ()
# f()