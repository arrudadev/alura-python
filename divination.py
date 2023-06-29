from random import randrange


def play():
  print("*********************************")
  print("Bem vindo ao jogo de Adivinhação!")
  print("*********************************")

  # generate random number in range 1:100
  secret_number = randrange(1, 101)
  attempts_total = 0
  points = 1000

  print('Qual o nível de dificuldade?')
  print('(1) Fácil (2) Médio (3) Difícil')

  difficultyLevel = int(input('Defina o nível: '))

  if (difficultyLevel == 1):
    attempts_total = 20
  elif (difficultyLevel == 2):
    attempts_total = 10
  else:
    attempts_total = 5

  for current_attempt in range(1, attempts_total + 1):
    print('Tentativa {} de {}'.format(current_attempt, attempts_total))

    guessed_number = int(input('Digite um número entre 1 e 100: '))

    print('Você digitou: ', guessed_number)

    if (guessed_number < 1 or guessed_number > 100):
      print('Você deve digitar um número entre 1 e 100!')
      continue

    if (secret_number == guessed_number):
      print(f'Você acertou e fez {points} pontos!')
      break
    elif (current_attempt == attempts_total):
      print(
          f'o número secreto era {secret_number}. Você fez {points} pontos!')
    elif (guessed_number > secret_number):
      print('Você errou! o seu chute foi maior que o número secreto.')
    else:
      print('Você errou! o seu chute foi menor que o número secreto.')

      points -= abs(secret_number - guessed_number)
  print('Fim do jogo!')


if (__name__ == "__main__"):
  play()
