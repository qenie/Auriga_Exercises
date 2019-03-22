""" The task is to write nickname generator. The input is date of birth in format DD.MM.YY.
    The nickname consists of 2 words: word1 and word2.
    word1 = biggest number of DD and converted to word (example: DD = 08, word1 = 8ight)
    word2 = smallest number of YY and converted to word (example: YY = 97, word2 = 7even)
    Note: we do not check input (assuming corrected input)
"""

words_dictionary = {0: 'ero',
                    1: 'ne',
                    2: 'wo',
                    3: 'hree',
                    4: 'our',
                    5: 'ive',
                    6: 'ix',
                    7: 'even',
                    8: 'ight',
                    9: 'ine'}


def biggest_number(number):
    input_number = int(number)
    digit_1 = input_number // 10
    digit_2 = input_number - digit_1*10
    if digit_1 > digit_2:
        return digit_1
    else:
        return digit_2


def smallest_number(number):
    input_number = int(number)
    digit_1 = input_number // 10
    digit_2 = input_number - digit_1*10
    if digit_1 < digit_2:
        return digit_1
    else:
        return digit_2


print("We will generate a nickname for you. Enter your date of birth in following format DD.MM.YY")
input_date_of_birth = input("Input your date of birth:")
word1_number = int(input_date_of_birth[0]+input_date_of_birth[1])
word2_number = int(input_date_of_birth[6]+input_date_of_birth[7])
word1 = str(biggest_number(word1_number)) + words_dictionary[biggest_number(word1_number)]
word2 = str(smallest_number(word2_number)) + words_dictionary[smallest_number(word2_number)]

print("Nickname is: {0} {1}".format(word1, word2))
