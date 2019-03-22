# This function compresses input string to the compressed string.
# Example: 'abbcccc' = 'a1b2c4'
# if compressed string bigger than input string, the result will be input string


def compress_string(string):
    compressed_string = ''
    counter = 1
    for i in range(1, len(string), 1):
        if string[i] == string[i-1]:
            counter += 1
        else:
            compressed_string += string[i-1]+str(counter)
            counter = 1
    compressed_string += string[len(string)-1]+str(counter)
    if len(string) > len(compressed_string):
        return compressed_string
    else:
        return string


input_string = input("Enter a string to compress:")
print("Compressed string is:", compress_string(input_string))
