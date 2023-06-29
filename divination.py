from random import randrange

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

# generate random number in range 1:100
secret_number = randrange(1, 101)
attempts_total = 3

for current_attempt in range(1, attempts_total + 1):
  print('Tentativa {} de {}'.format(current_attempt, attempts_total))

  guessed_number = int(input('Digite um número entre 1 e 100: '))

  print('Você digitou: ', guessed_number)

  if (guessed_number < 1 or guessed_number > 100):
    print('Você deve digitar um número entre 1 e 100!')
    continue

  if (secret_number == guessed_number):
    print('Você acertou!')
    break
  elif (guessed_number > secret_number):
    print('Você errou! o seu chute foi maior que o número secreto.')
  else:
    print('Você errou! o seu chute foi menor que o número secreto.')

print('Fim do jogo!')
