print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = 42

guessed_number = int(input('Digite um número: '))

print('Você digitou: ', guessed_number)

if (secret_number == guessed_number):
  print('Você acertou!')
else:
  print('Você errou!')

print('Fim do jogo!')
