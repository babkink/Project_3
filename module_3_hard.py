data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum = 0
def calculate_structure_sum(*str_):
    global sum
    for i in str_:
        if isinstance(i, (tuple, list)):
            for j in range(len(i)):
                if isinstance(i[j], (int, float)):
                    sum = sum + i[j]
                elif isinstance(i[j], str):
                    sum = sum + len(i[j])
                else:
                    a = i[j]
                    calculate_structure_sum(a)
        elif isinstance(i, set):
            calculate_structure_sum(list(i))
        elif isinstance(i, dict):
            for k, v in i.items():
                if type(k) == int or type(k) == float:
                    sum = sum + k
                elif type(k) == str:
                    sum = sum + len(k)
                if type(v) == int or type(v) == float:
                    sum = sum + v
                elif type(v) == str:
                    sum = sum + len(v)
    return sum



print(calculate_structure_sum(data_structure))

