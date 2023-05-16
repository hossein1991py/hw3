import math

def divide_numbers(number1, number2):
    """ Divides two numbers.

     :param number1: The first number to divide by
     :type number1: float or int
     :param number2: second number to divide
     :type number2: float or int
     :raises Valueerror: if the input values are not numbers
     :raises ZeroDivisionError: if division by zero is done
     :return: The result of dividing two numbers
     :type: float or inf
    """

    try:
        result = float(number1) / float(number2)
    except ValueError:
        print("Not possible without value")
    except ZeroDivisionError:
        print("Division by zero is impossible")
        return math.inf
    else:
        print("The divide was successful")
        return result

# Sample inputs and function calls
num1 = input("first number: ")
num2 = input("second number: ")
result = divide_numbers(num1, num2)

print(result)