"""
This module performs 4 basic math operation:
add, subtract, multiply, divide on two float numbers
"""


class Calculator:
    """
    A class used to represent a Calculator

    Attributes
    first_num : float
        the first number for performing operations
    second_num : float
        the second number for performing operations

    Methods
    __init__(self, first_num, second_num)
        Initializes Calculator
    add(self)
        Adds two float numbers
    sub(self)
        Subtracts the second number from the first number
    mul(self)
        Multiplies two numbers
    div(self)
        Divides the first number by the second number
    """
    first_num: float
    second_num: float

    def __init__(self, first_num, second_num):
        """
        This method initializes Calculator class with parameters first_num, second_num

        Parameters:
        first_num  (float): the first number for performing operations
        second_num (float): the second number for performing operations
        """
        self.first_num = first_num
        self.second_num = second_num

    def add(self):
        """
        This method adds two float numbers

        Parameters:
        first_num  (float): the first number for performing addition
        second_num (float): the second number for performing addition

        Returns:
        float:Returning a sum of first_num and second_num
        """
        return self.first_num + self.second_num

    def sub(self):
        """
        This method subtracts the second number from the first number

        Parameters:
        first_num  (float): the first number for performing subtraction
        second_num (float): the second number for performing subtraction

        Returns:
        float:Returning a difference of first_num and second_num
        """
        return self.first_num - self.second_num

    def mul(self):
        """
        This method multiplies two numbers

        Parameters:
        first_num  (float): the first number for performing multiplication
        second_num (float): the second number for performing multiplication

        Returns:
        float:Returning a product of first_num and second_num
        """
        return self.first_num * self.second_num

    def div(self):
        """
        This method divides the first number by the second number

        Parameters:
        first_num  (float): the first number for performing division
        second_num (float): the second number for performing division

        Returns:
        float:Returning a quotient of first_num and second_num
        """
        return self.first_num / self.second_num


first_operand = float(input("Please enter the first number : "))
second_operand = float(input("Please enter the second number : "))
my_calc = Calculator(first_operand, second_operand)
while True:
    choice = int(input("Please select the options: \n1 - Addition \n2 - Subtraction "
                       "\n3 - Multiplication \n4 - Division "))
    if choice == 1:
        print("Result: ", my_calc.add())
    elif choice == 2:
        print("Result: ", my_calc.sub())
    elif choice == 3:
        print("Result: ", my_calc.mul())
    elif choice == 4:
        print("Result: ", my_calc.div())
    elif choice == 0:
        print("Exit ")
        break
    else:
        print("Incorrect entering, please, try again ")
        break
