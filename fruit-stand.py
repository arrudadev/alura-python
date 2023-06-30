fruits = ['Banana', 'Maçã', 'Pera', 'Uva', 'Melancia', 'Melão']

fruit = input('Qual é a fruta que deseja consultar? ')


def convert_list_in_upper_case(list):
  return [item.upper() for item in list]


if (fruit.upper() in convert_list_in_upper_case(fruits)):
  print(f'Sim, temos {fruit.capitalize()} no estoque!')
else:
  print(f'Não temos {fruit.capitalize()} no estoque!')
