data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_ = 0


def calculate_structure_sum(*i):
    global sum_
    for j in i:
        if isinstance(j, (list, tuple, set)):
            calculate_structure_sum(*j)
        elif isinstance(j, dict):
            for k in j.items():
                calculate_structure_sum(*k)
        elif isinstance(j, (int, float)):
            sum_ += j
        else:
            isinstance(j, str)
            sum_ += (len(j))

    return sum_


print(calculate_structure_sum(data_structure))

