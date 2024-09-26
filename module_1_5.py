immutable_var = (0, 1, 0.1, True, 'home', [0, 6])
print(immutable_var)
# immutable_var[0] = 5 # кортеж является неизменяемым объектом, при изменении элемента появится ошибка
# print(immutable_var)
immutable_var[5][1] = 4 # сам по себе кортеж неизменяемый, но мы можем изменить элемент кортежа - список
print(immutable_var)
mutable_list = [-5, 1, 2, 7, 10, 37]
mutable_list[5] = 'Roman'
mutable_list.append(37.1)
mutable_list.extend('qwertyuiop')
mutable_list.extend(['go', 7, 1])
mutable_list.remove(7)
print(mutable_list)
