#                                   The task is to implement Quick sum algorithm.
# We are assuming that input string has only capital letters and spaces (we perform just basic check - other symbols
# will be ignored.) Quick sum = sum of position of letter in the input string multiplied by [letter meaning].
# Where [letter meaning] = position in the alphabet (a=1, b=2, etc.).
# example 1: ACM = 1*1 + 2*3 + 3*13 = 46
# example 2: A C M = 1 * 1 + 3 * 3 + 5 * 12 = 75

print("We will perform Quick sum of the string you input:")
input_sting = input("Enter string:")

def letter_meaning(symbol):
    alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    return alphabet.index(symbol)+1  # Real position starts from 1 not 0


def quick_sum(string):
    string_length = len(string)
    calculated_sum = 0
    for i in range(string_length):
        calculated_sum += letter_meaning(string[i])*(i+1)

    return calculated_sum


print(quick_sum(input_sting))
