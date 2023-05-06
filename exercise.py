
def user_calcs():
    while True:
        question = input("Would you like 'square footage' or 'circumference'.\n Type 'quit' to quit. ")
        if question == 'square footage':
            length = int(input('What is the length of the home? '))
            width = int(input('What is the width of the home? '))
            square_feet = length * width
            print(f'The square footage of your home is ' + str(square_feet))
        if question == 'circumference':
            radius = int(input('Enter radius. '))
            import math
            circumference = math.pi * 2 * radius
            print(f'The circumference of this circle is ' + str(circumference))
        if question == 'quit':
            break
user_calcs()

