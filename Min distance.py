# Search for a minimal distance between 2 words entered from user in the text file 'test.txt'

file_name = 'test.txt'


def distance(list1, list2):
    if list1 and list2:
        list_sorted = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                list_sorted.append(abs(list1[i]-list2[j]))
        return min(list_sorted)


def min_between_words(word1, word2):
    with open(file_name, 'r') as file:
        counter = 0
        word1_counter = []
        word2_counter = []
        for line in file:
            words = line.split()
            for word in words:
                counter += 1
                if word == word1:
                    word1_counter.append(counter)
                elif word == word2:
                    word2_counter.append(counter)
    if not word1_counter:       # if word1 was not found in the text minimal distance cannot be calculated
        return -1
    elif not word2_counter:     # if word2 was not found in the text minimal distance cannot be calculated
        return -2
    return distance(word1_counter, word2_counter)


input_word1 = input("Enter word 1:")
input_word2 = input("Enter word 2:")

if min_between_words(input_word1, input_word2) == -1:
    print("There is no word '{0}' in the file".format(input_word1))
elif min_between_words(input_word1, input_word2) == -2:
    print("There is no word '{0}' word in the file".format(input_word2))
else:
    print("Minimum distance between '{0}' and '{1}' words is:".format(input_word1, input_word2),
          min_between_words(input_word1, input_word2))
