# def num_in_seq(n):
#     first_num = 8
#     difference = 7
#
#     n_position = first_num + (n - 1) * difference
#
#     return n_position


# Recursive version
def num_in_seq(n):
    if n == 1:
        return 8

    return num_in_seq(n - 1) + 7


print(num_in_seq(1))  # Should be 8
print(num_in_seq(5))  # Should be 36
print(num_in_seq(10))  # Should be 71
