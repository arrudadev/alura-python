print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = 42

guessed_number = int(input('Digite um número: '))

print('Você digitou: ', guessed_number)

if (secret_number == guessed_number):
  print('Você acertou!')
elif (guessed_number > secret_number):
  print('Você errou! o seu chute foi maior que o número secreto.')
else:
  print('Você errou! o seu chute foi menor que o número secreto.')

print('Fim do jogo!')
