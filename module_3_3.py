def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(4, "cookie",False)
print_params(4, 6)
print_params( "Moon" )
print_params(1, 1 , 1)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [321, 'Вулкан', True]
values_dict = {'a' : 2127572 , 'b' : 'Ручка' , 'c' : False }

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5 , 'Stone']
print_params(*values_list_2, 42)