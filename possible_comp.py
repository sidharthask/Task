def find_comp(input_list):
    if len(input_list) == 0:
        return [[]]
    list_values = []

    for i in find_comp(input_list[1:]):
        list_values += i, i + [input_list[0]]

    return list_values


def get_sum_dict(compined_list):
    if [] in compined_list:
        compined_list.remove([])

    map_dict = {}
    for i in compined_list:
        map_dict[sum(i)] = i

    return map_dict


def get_common_sum(c, d):
    e = list(c.keys())
    f = list(d.keys())

    for i in e:
        if i in f:
            common_sum = i
            return common_sum


class CheckComp:
    def main(a, b):
        possib_comp_a = find_comp(a)
        possib_comp_b = find_comp(b)
        a_get_sum = get_sum_dict(possib_comp_a)
        b_get_sum = get_sum_dict(possib_comp_b)
        common_sum = get_common_sum(a_get_sum,b_get_sum)
        a_list = a_get_sum[common_sum]
        b_list = b_get_sum[common_sum]

        print(a_list, b_list)
        return a_list, b_list



if __name__ == "__main__":
    # A = [1,2,3,4,5,6] # test case
    # B = [9,10,11,12,13,14] # test case
    A = [int(item) for item in input("Enter the first list items separated by space : ").split()]
    B = [int(item) for item in input("Enter the second list items separated by space : ").split()]
    CheckComp.main(A, B)



