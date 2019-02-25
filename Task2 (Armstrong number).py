"""" This program defines function to check if the input number is Armstrong number.
 Armstrong example of number is 153 = 1^3+5^3+3^3 (where 3 is number digits) """

input_number = input("Enter a number: ")


def armstrong_number(number):
    calculated_value = 0
    input_string = str(number)
    digits = len(str(number))
    for i in range(digits):
        calculated_value += int(input_string[i]) ** digits
    if calculated_value == int(number):
        return "YES"
    else:
        return "NO"


print(armstrong_number(input_number))
