# This is a sample Python script.
# function

def num_check(question):

    valid = False
    while not valid:

        error = "please enter a number that is more than zero"

        try:
            # asks user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print("please enter a number that is more than zero")
                print()

        except ValueError:
            print(error)

# main routine goes here

# introduction / Heading print statements

print()
print("**** Area Perimeter Calculator ****")
print()

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")
    print()
    print("Width", width)
    print("Height", height)
    print()

    # calculate area (width x height)
    area = width * height

    # calculate perimeter

    perimeter = 2 * (width + height)

    # output and perimeter (to 2 dp)

    print("Perimeter: {.2f} units".format(perimeter))
    print("Area: {.2f} square units".format(area))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator")


