import random

original_list = [1, 2, 3, 4, 5, 6, 7, 9]
new_list = random.sample(original_list, 3)


original_list = [6, 3, 7]
i, j = random.sample(range(len(original_list)), 2)
original_list[i], original_list[j] = original_list[j], original_list[i]
print("Новий список:", original_list)

pass
