def reverse_string_iteration(string: str) -> str:
    if len(string) < 2:
        return string
    reversed_string: str = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
        # reversed_array.append(string[i])
    return reversed_string


def reverse_string_recursion(string: str) -> str:
    if string == '':
        return string
    else:
        return reverse_string_recursion(string[1:len(string)]) + string[0]



# result = reverse_string_iteration('engin')
# result2 = reverse_string_recursion('engin')
#
# print(result)
# print(result2)