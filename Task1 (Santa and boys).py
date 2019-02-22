# The task is to find amount of "Bad boys" (represented  by '=o' symbols) and "Good boys" (represented by 'o='
# symbols) in the given string. There is also Santa (represented by 'd' symbol) but actually 'd' symbol treated just
# like other symbols (not sufficient).

symbols_counter = 0  # just a counter that changes from 0 to len(input_string)
good_boy_counter = 0
bad_boy_counter = 0
santa_counter = 0

string = input("Input a string:")
string_length = len(string)  # to check array boundaries

while symbols_counter < string_length:
    if string[symbols_counter] == "d":
        symbols_counter += 1
        santa_counter += 1
    elif symbols_counter + 1 > string_length-1:  # check that symbols_counter+1 will not out of array of input_string
        break
    elif string[symbols_counter] == '=' and string[symbols_counter+1] == 'o':
        bad_boy_counter += 1
        symbols_counter += 2
    elif string[symbols_counter] == 'o' and string[symbols_counter+1] == '=':
        good_boy_counter += 1
        symbols_counter += 2
    else:
        symbols_counter += 1

print("Good boys:", good_boy_counter)
print("Bad boys:", bad_boy_counter)
if santa_counter == 0:
    print("But there is no Santa around")
