
# The task is to enter a number and find all pairs of numbers sum of that is equal to entered number

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def find_sum(collection, number):
    output_list = []
    length = len(collection)
    for i in range(length):
        for j in range(i+1, length, 1):
            if collection[i] + collection[j] == number:
                current_item = [collection[i], collection[j]]
                output_list.append(current_item)

    return output_list


def find_sum_eff(collection, number):
    output_list = []
    length = len(collection)
    for i in range(length):
        residue = number - collection[i]
        for j in range(i+1, length, 1):
            if collection[j] > residue:
                continue
            else:
                if collection[j] == residue:
                    current_item = [collection[i], collection[j]]
                    output_list.append(current_item)

    return output_list


print("The collection is:", data)
input_number = input("Enter a number N to find all pairs with sum equal to N in the collection:")
print("Following pairs were found:", find_sum(data, int(input_number)))
print("Following pairs were found:", find_sum_eff(data, int(input_number)))
