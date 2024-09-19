def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1, 2, 3)
print_params(5, 6)
print_params(b=25)
print_params(c = [1, 2, 3])

values_list = [22, True, 'Hello']
values_dict = {'Bob': 22, 'True': 33, '42': 44}
values_dict_1 = {'a': 22, 'b': 33, 'c': 44}
values_list_2 = [54.32, 'Строка' ]

print_params(values_list) #не распакован values_list
print_params(*values_list) # values_list распакован, значения стали переменными функции print_params
print_params(values_dict) # словарь не распакован
print_params(*values_dict) # на место переменных встали ключи
print_params(**values_dict_1) # работает, когда ключи в словаре соответствуют названиям переменных в фукнции
#print_params(**values_dict) # не работает - ключи должны соответствовать названмиям переменных
print_params(*values_list_2)
print_params(c=23, *values_list_2)
print_params(*values_list_2, 23)
print_params(True, *values_list_2)
#print_params(a=True, *values_list_2) # не работает, почему? С точки зрения логики эта фукция и та, что на строчку выше не отличаются

