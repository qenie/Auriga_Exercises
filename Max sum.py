# Search for max sum of continuous sequence in the given array

data = [1, 3, 5, -7, 8, -1, 3, -2, 9]


def max_summary(array):
    max_sum = 0
    for i in range(len(array)):
        max_sum += array[i]
        temp_sum = array[i]
        if max_sum < temp_sum:
            max_sum = temp_sum
    return max_sum


print("Maximum sum is ", max_summary(data))
