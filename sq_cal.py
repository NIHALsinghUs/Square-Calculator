# Define a class to represent a Square object
class Square:

    # Constructor method to initialize the square with a side length
    def __init__(self, side):
        self.side = side

    # Method to calculate and return the area of the square
    def area_of_square(self):
        return self.side * self.side
    
    # Method to calculate and return the perimeter of the square
    def perimeter_of_square(self):
        return 4 * self.side
    

# Main Program Execution
print("--- Square Calculator ---")

print("===========================")

# Take the side length of the square as integer input from the user
side = int(input("Enter the Number : "))

# Create an instance (object) of the Square class with the given side
sq = Square(side)

print("-----------------------------------")

# Display the menu options to the user
print("1. Area of square\n2. Perimeter of square")

print("-----------------------------------")

# Take the menu choice as integer input from the user
user_choice = int(input("Select the option : "))

print("-----------------------------------")

# Check the user's choice and call the appropriate class method
if (user_choice == 1):
    # Call the area method and print the result
    print("Area of square :",sq.area_of_square())

elif (user_choice == 2):
    # Call the perimeter method and print the result
    print("Perimeter of square :",sq.perimeter_of_square())

else:
    # Handle any input that does not match the available options
    print("You select the invalid option :",user_choice)