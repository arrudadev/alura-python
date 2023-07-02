week_days_tuple = ('Segunda', 'Terça', 'Quarta',
                   'Quinta', 'Sexta', 'Sábado', 'Domingo')

week_days_list = ['Segunda', 'Terça', 'Quarta',
                  'Quinta', 'Sexta', 'Sábado', 'Domingo']

print('Type:', type(week_days_tuple))
print('Data:', week_days_tuple)
print('Type:', type(week_days_list))
print('Data:', week_days_tuple)

# tuples are immutable, the following code does`t work:
#  week_days_tuple.append('Domingo2')

# List are mutable, the following code work:
# week_days_list.append('Domingo2')

# it`s possible to convert list in tuple and tuple in list

converted_tuple_in_list = list(week_days_tuple)
converted_list_in_tuple = tuple(week_days_list)

print('Type:', type(converted_tuple_in_list))
print('Data:', converted_tuple_in_list)
print('Type:', type(converted_list_in_tuple))
print('Data:', converted_list_in_tuple)
