""" This program called 'accumulation'.
    INPUT "abcd” OUTPUT "A-Bb-Ccc-Dddd"
    INPUT "RqaEzty" OUTPUT "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    INPUT "cwAt" OUTPUT "C-Ww-Aaa-Tttt"
"""


def symbol_multiplier(letter, position):
    output_string = letter.title()
    for i in range(int(position)-1):
        output_string += letter.lower()
    return output_string


def accumulation(string):
    result_string = string[0].title()
    for i in range(len(string)):
        if i == 0:
            continue
        result_string += '-'
        result_string += symbol_multiplier(string[i], i+1)
    return result_string


print("We will accumulate your string.")
print(accumulation(input("Enter string:")))
