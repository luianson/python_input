import random
import turtle as t

# Input the length
def get_line_length():

    choice = input('Enter line length "long, medium, short": ')

    print (choice)

    if choice == 'long':
        line_length = 250
    elif choice == 'medium':
        line_length = 200
    else:
        line_length = 100

    return line_length

# Input the width
def get_line_width():
    choice = input('Enter line width "superthick, thick, thin": ')

    print (choice)
    if choice == 'superthick':
        width = 40
    elif choice == 'thick':
        width = 25
    else:
        width = 10
    return width

#Get Length from user
line_length = get_line_length()
print('The return value is', line_length)

#Get Width from user
line_width = get_line_width()
print('The return value is', line_width)

t.shape('turtle')
t.fillcolor('green')
t.pensize(line_width)
t.forward(line_length)
