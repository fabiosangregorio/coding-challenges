import math


def reverseArray(array):
    n = len(array)
    last = n - 1
    middle = math.floor(n / 2)

    # + 1 because range excludes the upper bound
    for left in range(middle):
        right = last - left
        temp = array[left]
        array[left] = array[right]
        array[right] = temp

    return array


if __name__ == "__main__":
    input_data = [1, 4, 3, 2]
    print(reverseArray(input_data))