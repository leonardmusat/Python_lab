def lab3_8(mapping):
    key = 'start'
    result = []
    visited_keys = set()

    while key not in visited_keys:
        visited_keys.add(key)
        result.append(mapping[key])
        key = mapping[key]
        if key in visited_keys:
            result.pop()
            break
    return result


print(lab3_8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))