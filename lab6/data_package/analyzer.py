def calculate_mean(num_list):
    if len(num_list) == 0:
        raise ValueError("List cannot be empty.")

    total = 0
    for num in num_list:
        total += num

    return total / len(num_list)


def find_maximum(num_list):
    if len(num_list) == 0:
        raise ValueError("List cannot be empty.")

    maximum = num_list[0]

    for num in num_list:
        if num > maximum:
            maximum = num

    return maximum


def find_minimum(num_list):
    if len(num_list) == 0:
        raise ValueError("List cannot be empty.")

    minimum = num_list[0]

    for num in num_list:
        if num < minimum:
            minimum = num

    return minimum