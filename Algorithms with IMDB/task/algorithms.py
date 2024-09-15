import csv

with open('movies.csv', mode='r', newline='', encoding="UTF-8") as f:
    csv_reader = csv.reader(f)
    movies = list(csv_reader)


def bubble_sort(array):
    n = len(array)

    for index in range(n):
        for second_index in range(0, n - index - 1):
            if array[second_index][1] > array[second_index + 1][1]:
                array[second_index], array[second_index + 1] = array[second_index + 1], array[second_index]
    return array


def merge_sort(array):
    if len(array) <= 1:
        return array

    # Divide the array into two halves
    middle = len(array) // 2
    left_half = merge_sort(array[:middle])
    right_half = merge_sort(array[middle:])

    # Merge the two halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    index = second_index = 0

    # Compare elements from both halves and merge
    while index < len(left) and second_index < len(right):
        if left[index][1] <= right[second_index][1]:  # Compare based on score (second element)
            merged.append(left[index])
            index += 1
        else:
            merged.append(right[second_index])
            second_index += 1

    # Collect the remaining elements
    merged.extend(left[index:])
    merged.extend(right[second_index:])

    return merged



sorted_movies2 = bubble_sort(movies)
sorted_movies = merge_sort(movies)


def binary_search(sorted_array):
    found_movies = []
    n = len(sorted_array)
    low = 0
    high = n - 1

    while low <= high:
        middle = int((low + high) / 2)
        if float(sorted_array[middle][1]) == 6.0:
            return middle
        elif float(sorted_array[middle][1]) > 6.0:
            high = middle - 1
        elif float(sorted_array[middle][1]) < 6.0:
            low = middle + 1

    return found_movies or -1

def print_movies(sorted_array):
    found_array = []
    while binary_search(sorted_array) != -1:
        found_index = binary_search(sorted_array)
        found_array.append(sorted_array[found_index])
        del sorted_array[found_index]
    return found_array

for movie, score in print_movies(sorted_movies):
    print(f'{movie} - {float(score)}')