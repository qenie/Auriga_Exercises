# This program converts arabic numerals to roman numerals

def conversion(number):
    output_string = ''
    # create a tuple to define roman numerals
    roman_numeral = {1: "I",       11: "XI",       21: "XXX",      31: "CD",
                     2: "II",      12: "XII",      22: "XL",       32: "D",
                     3: "III",     13: "XIII",     23: "L",        33: "DC",
                     4: "IV",      14: "XIV",      24: "LX",       34: "DCC",
                     5: "V",       15: "XV",       25: "LXX",      35: "DCCC",
                     6: "VI",      16: "XVI",      26: "LXXX",     36: "CM",
                     7: "VII",     17: "XVII",     27: "XC",       37: "M",
                     8: "VIII",    18: "XVIII",    28: "C",        38: "MM",
                     9: "IX",      19: "XIX",      29: "CC",       39: "MMM",
                     10: "X",      20: "XX",       30: "CCC"}

    # create a tuple with indexes to relate to roman_numeral tuple
    roman_index = {1: 1,  11: 11,  21: 30,  31: 400,
                   2: 2,  12: 12,  22: 40,  32: 500,
                   3: 3,  13: 13,  23: 50,  33: 600,
                   4: 4,  14: 14,  24: 60,  34: 700,
                   5: 5,  15: 15,  25: 70,  35: 800,
                   6: 6,  16: 16,  26: 80,  36: 900,
                   7: 7,  17: 17,  27: 90,  37: 1000,
                   8: 8,  18: 18,  28: 100, 38: 2000,
                   9: 9,  19:19,   29: 200, 39: 3000,
                   10:10, 20: 20,  30: 300,}

    temp_number = number
    for i in range(39, 0, -1):
        while temp_number - roman_index[i] >= 0:
            temp_number -= roman_index[i]
            output_string += roman_numeral[i]

    return output_string


print("We will convert arabic numeral to roman numeral.")
input_number = int(input("Enter a number to convert to roman:"))
print(conversion(input_number))
