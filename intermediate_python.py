def get_unique_list(my_list):

    new_list = []

    for n in my_list:

         if n not in new_list:

             new_list.append(n)

    return new_list # return unique elements of list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)