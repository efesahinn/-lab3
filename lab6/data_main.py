from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)

try:
    user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

    parts = user_input.split(",")

    stripped_parts = strip_whitespaces(parts)

    number_list = []
    for item in stripped_parts:
        number_list.append(float(item))

    cleaned_unique_data = remove_duplicates(number_list)

    mean_value = calculate_mean(cleaned_unique_data)
    max_value = find_maximum(cleaned_unique_data)
    min_value = find_minimum(cleaned_unique_data)

    print(f"Cleaned and unique data: {cleaned_unique_data}")
    print("--------------------")
    print(f"Mean: {mean_value:.2f}")
    print(f"Maximum: {max_value}")
    print(f"Minimum: {min_value}")

except ValueError:
    print("Data Error: Please make sure you only enter numbers separated by commas.")