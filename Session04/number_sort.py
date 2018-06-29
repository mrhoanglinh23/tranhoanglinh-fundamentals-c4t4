# numbers = [2, 0, -3, -32]

# sorted_list = []
# sorting = True
# while sorting:
    min_numb = min(numbers)
    sorted_list.append(min_numb)
    numbers.remove(min_numb)

    if len(numbers) == 0:
        sorting = False

# print(*sorted_list)

