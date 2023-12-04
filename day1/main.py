import numpy as np

def get_all_digits(string) -> list:
    """ Returns all numbers in a string as a list of integers. """

    spelled_out_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    digits = []
    for i, char in enumerate(string):

        if char.isdigit():
            digits.append(str(char))
            continue

        for j, spelled_out_number in enumerate(spelled_out_numbers):
            word = ""
            for k, letter in enumerate(spelled_out_number):

                if i + k >= len(string):
                    break
                if string[i + k] != letter:
                    break

                word += letter

            if word == spelled_out_numbers[j]:
                digits.append(str(j + 1))
                
    return digits

def make_two_digit_number(list_of_digits) -> int:
    """ Returns the first and last digit of a string of digits as a two-digit number. """
    return int(list_of_digits[0] + list_of_digits[-1])

def main():

    # Import list of strings
    with open("day1/day1_input.txt") as f:
        input = f.read().splitlines()

    input = input

    digits = []
    for string in input:
        digits.append(get_all_digits(string))
    
    numbers = []
    for row in digits:
        numbers.append(make_two_digit_number(row))
        
    print(f"sum of all numbers: {sum(numbers)}")
    
if __name__ == "__main__":
    main()



