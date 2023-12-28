#
#     ls = ls[::-1]
#     array = []
#     second_array = []
#     for i in range(len(ls)):
#         array.append(ls[i])
#         second_array.append(sum(array))
#     return second_array[::-1] + [0]
# print(parts_sums([0, 1, 3, 6, 10]))

def parts_sums(ls):
    sums = [sum(ls)]
    for i in ls:
        sums.append(sums[-1]-i)
    return sums