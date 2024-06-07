def linear_search(value_to_find, array_to_search_through):
    for i, val in enumerate(array_to_search_through):
        if val == value_to_find:
            return i


def linear_search_global(value_to_find, array_to_search_through):
    vals = []
    for i, val in enumerate(array_to_search_through):
        if val == value_to_find:
            vals.append(i)
    return vals
    