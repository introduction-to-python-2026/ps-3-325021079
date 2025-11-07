def move(my_list, direction=None):
    result = my_list.copy()
    index_of_one = result.index(1)

    if direction == 'right' and index_of_one < len(result) - 1:
        result[index_of_one] = 0
        result[index_of_one + 1] = 1
    elif direction == 'left' and index_of_one > 0:
        result[index_of_one] = 0
        result[index_of_one - 1] = 1

    return result
