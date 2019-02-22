# This program will find Armstrong numbers in the range of [1, N], where N input munber
# Armstrong example of number is 153 = 1^3+5^3+3^3 (where 3 is number digits)


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


print("The program will find Armstrong numbers in the range of [1,N]")
input_number = input("Enter N: ")

for j in range(int(input_number)):
    if armstrong_number(j) == "YES":
        print(j)
