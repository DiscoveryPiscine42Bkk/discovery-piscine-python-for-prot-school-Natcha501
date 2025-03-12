original_array = [2, 8, 9, 48, 8, 22, -12, 2]

filtered_array = [value for value in original_array if value > 5]

processed_array = [value + 2 for value in filtered_array]

processed_set = set(processed_array)

print(original_array)

print(processed_set)