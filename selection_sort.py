list = [3,1,6,7,4]
for i in range(len(list)):
    min_index = i  # Track the index of the minimum element
    for j in range(i+1, len(list)):
        if list[j] < list[min_index]:
            min_index = j  # Update the index of the minimum element
    # Swap the found minimum element with the first element
    list[i], list[min_index] = list[min_index], list[i]

print(list)