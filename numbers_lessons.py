def split_list(lst):
    if not lst:
        return [[], []]

    return [lst[: (len(lst) + 1) // 2], lst[(len(lst) + 1) // 2 :]]


print(split_list([1, 2, 3, 4, 5]))
print(split_list([1, 2, 3, 4]))
print(split_list([]))

pass
