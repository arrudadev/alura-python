print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = 42
attempts_total = 3
attempts_count = 1

while (attempts_count <= attempts_total):
  print('Tentativa', attempts_count, 'de', attempts_total)
  guessed_number = int(input('Digite um número: '))

  print('Você digitou: ', guessed_number)

  if (secret_number == guessed_number):
    print('Você acertou!')
  elif (guessed_number > secret_number):
    print('Você errou! o seu chute foi maior que o número secreto.')
  else:
    print('Você errou! o seu chute foi menor que o número secreto.')

  attempts_count += 1

print('Fim do jogo!')
