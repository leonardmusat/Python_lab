def set_operations(sets):
    result = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a = sets[i]
            b = sets[j]

            union_result = a | b
            intersection_result = a & b
            a_minus_b_result = a - b
            b_minus_a_result = b - a
            key_union = str(a) + " | " + str(b)
            key_intersection = str(a) + " & " + str(b)
            key_a_minus_b = str(a) + " - " + str(b)
            key_b_minus_a = str(b) + " - " + str(a)

            result[key_union] = union_result
            result[key_intersection] = intersection_result
            result[key_a_minus_b] = a_minus_b_result
            result[key_b_minus_a] = b_minus_a_result

    return result


set_list = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]

result_dict = set_operations(set_list)
print(result_dict)