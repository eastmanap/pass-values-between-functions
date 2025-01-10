# Apollos Eastman
# 1/10/2025
# Passing Return Values

# Square number
def square_number(num):
    return num * num

# Add squares
def add_squares(num1, num2):
    return square_number(num1) + square_number(num2)

# Main
def main():
    answer1 = float(input('Enter the first number:'))
    answer2 = float(input('Enter the second number:'))   
    result = add_squares(answer1, answer2)
    
    print(f'The sum of the squares of {answer1} and {answer2} is: {result}')

# Call
main()
