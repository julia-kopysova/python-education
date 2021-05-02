"""
This module demonstrates resolved tasks from https://www.learnpython.org/en/
"""
from typing import List


def print_hello() -> type(None):
    """
    This function outputs "Hello, World!" in console

    Returns:
        type(None): Returning None
    """
    print("Hello, World!")


def print_values() -> type(None):
    """
    This function outputs the initialized value of the variables when the condition is met

    Returns:
        type(None): Returning None
    """
    # Change this code
    my_string = "hello"
    my_float = 10.0
    my_int = 20

    # Testing code
    if my_string == "hello":
        print("String: %s" % my_string)
    if isinstance(my_float, float) and my_float == 10.0:
        print("Float: %f" % my_float)
    if isinstance(my_int, int) and my_int == 20:
        print("Integer: %d" % my_int)


def print_list() -> type(None):
    """
    This function outputs lists and second name in the names list

    Returns:
        type(None): Returning None
    """
    numbers = [1, 2, 3]
    strings = ["hello", "word"]
    names = ["John", "Eric", "Jessica"]

    # Write your code here
    second_name = names[1]

    # This code should write out the filled arrays and the second name in the names list (Eric).
    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % second_name)


def using_operators() -> type(None):
    """
    This function creates two lists called x_list and y_list,
    which contain 10 instances of the variables x and y,
    respectively. You are also required to create a list called big_list,
    which contains the variables x and y,
    10 times each, by concatenating the two created lists.

    Returns:
        type(None): Returning None
    """
    x_object = object()
    y_object = object()

    # Change this code
    x_list = [x_object] * 10
    y_list = [y_object] * 10
    big_list = x_list + y_list

    print("x_list contains %d objects" % len(x_list))
    print("y_list contains %d objects" % len(y_list))
    print("big_list contains %d objects" % len(big_list))

    # testing code
    if x_list.count(x_object) == 10 and y_list.count(y_object) == 10:
        print("Almost there...")
    if big_list.count(x_object) == 10 and big_list.count(y_object) == 10:
        print("Great!")


def print_format_string() -> type(None):
    """
    This function outputs a format string which prints out the
    data using the following syntax:
    Hello John Doe. Your current balance is $53.44.

    Returns:
        type(None): Returning None
    """
    data = ("John", "Doe", 53.44)
    format_string = "Hello %s %s. Your current balance is $%s."

    print(format_string % data)


def string_operating() -> type(None):
    """
    This function outputs result of basic string operation

    Returns:
        type(None): Returning None
    """
    my_string = "Strings are awesome!"
    # Length should be 20
    print("Length of s = %d" % len(my_string))

    # First occurrence of "a" should be at index 8
    print("The first occurrence of the letter a = %d" % my_string.index("a"))

    # Number of a's should be 2
    print("a occurs %d times" % my_string.count("a"))

    # Slicing the string into bits
    print("The first five characters are '%s'" % my_string[:5])  # Start to 5
    print("The next five characters are '%s'" % my_string[5:10])  # 5 to 10
    print("The thirteenth character is '%s'" % my_string[12])  # Just number 12
    print("The characters with odd index are '%s'" % my_string[1::2])  # (0-based indexing)
    print("The last five characters are '%s'" % my_string[-5:])  # 5th-from-last to end

    # Convert everything to uppercase
    print("String in uppercase: %s" % my_string.upper())

    # Convert everything to lowercase
    print("String in lowercase: %s" % my_string.lower())

    # Check how a string starts
    if my_string.startswith("Str"):
        print("String starts with 'Str'. Good!")

    # Check how a string ends
    if my_string.endswith("ome!"):
        print("String ends with 'ome!'. Good!")

    # Split the string into three separate strings,
    # each containing only a word
    print("Split the words of the string: %s" % my_string.split(" "))


def condition_operation() -> type(None):
    """
    This function outputs result of condition operation

    Returns:
        type(None): Returning None
    """
    # Change this code
    number = 16
    second_number = None
    first_array = [1, 2, 3]
    second_array = [1, 2]

    if number > 15:
        print("1")

    if first_array:
        print("2")

    if len(second_array) == 2:
        print("3")

    if len(first_array) + len(second_array) == 5:
        print("4")

    if first_array and first_array[0] == 1:
        print("5")

    if not second_number:
        print("6")


def print_even_num() -> type(None):
    """
    This function outputs print out all even numbers
    from the numbers list in the same order they are received.
    Don't print any numbers that come after 237 in the sequence.

    Returns:
        type(None): Returning None
    """
    numbers = [
        951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
        615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
        743, 527
    ]

    # Your code goes here
    for number in numbers:
        if number == 237:
            break
        if number % 2 == 1:
            continue
        print(number)


# Modify this function to return a list of strings as defined above
def list_benefits() -> List[str]:
    """
    This function return a list of strings

    Returns:
        List[str]: Returning list of benefits
    """
    return ["More organized code", "More readable code",
            "Easier code reuse",
            "Allowing programmers to share and connect code together"]


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit: str) -> str:
    """
    This function concatenates to each benefit -
    " is a benefit of functions!"

    Receives:
        benefit: str: Name of benefit
    Returns:
        str: Returning string with benefits
    """
    return benefit + " is a benefit of functions!"


def name_the_benefits_of_functions() -> type(None):
    """
    This function outputs all benefits in sentences

    Returns:
        type(None): Returning None
    """
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


def len_args(first_num, second_num, third_num, *args) -> int:
    """
    This function outputs a length of args

    Returns:
        int: Returning length of args
    """
    print(first_num, second_num, third_num)
    return len(args)


def multiple_function(first_num, second_num, third_num, **kwargs) -> bool:
    """
    This function returns True if kwargs["magic_number"] = 7

    Returns:
        bool: Returning result of checking
    """
    print(first_num, second_num, third_num)
    return kwargs["magic_number"] == 7


if __name__ == "__main__":
    # Task 1: "Hello, World"
    # print_hello()

    # Task 2: Variables and Types
    # print_values()

    # Task 3: Lists
    # print_list()

    # Task 4: Basic Operators
    # using_operators()

    # Task 5: String Formatting
    # print_format_string()

    # Task 6: Basic String Operations
    # string_operating()

    # Task 7: Conditions
    # condition_operation()

    # Task 8: Loops
    # print_even_num()

    # Task 9: Functions
    # name_the_benefits_of_functions()

    # Task 10: Multiple Function Arguments
    if len_args(1, 2, 3, 4) == 1:
        print("Good.")
    if len_args(1, 2, 3, 4, 5) == 2:
        print("Better.")
    if not multiple_function(1, 2, 3, magic_number=6):
        print("Great.")
    if multiple_function(1, 2, 3, magic_number=7):
        print("Awesome!")


