print("This is a test. This is only a test.")

def math_fun():
    first_num = input("Pick a number between 1 and 100 ")
    second_num = input("Pick a second number between 1 and 100 ")

    print("{} plus {} is {}.".format(first_num, second_num, int(first_num) + int(second_num)))

answer = input("Do you want to do some math? (y,n) ")

if answer == 'y':
    math_fun()
else:
    print("Ok. Some other time.")


