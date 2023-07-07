from random import randrange


def print_opening_message():
  print("*********************************")
  print("Bem vindo ao jogo da Forca!")
  print("*********************************")


def get_secret_word():
  with open('words.txt', 'r') as words_file:
    words = [word for word in words_file]

  return words[randrange(0, len(words))].upper()


def get_hit_letters_initialized(secret_word):
  return ['_' for letter in secret_word]


def get_kick():
  return input('Qual letra? ').strip().upper()


def set_hit(hit_letters, secret_word, kick):
  index = 0
  for letter in secret_word:
    if (kick.upper() == letter.upper()):
      hit_letters[index] = letter
    index += 1


def check_hanged(max_erros, errors):
  return max_erros == errors


def check_hit_secret_word(hit_letters):
  return "_" not in hit_letters


def print_missing_letters(hit_letters):
  missing_letters = str(hit_letters.count('_'))
  print(f'Ainda faltam acertar {missing_letters} letra(s)!')


def print_errors_count(errors):
  print(f'Errou: {errors} letra(s)!')


def print_missing_attempts(max_erros, errors):
  print(f'Faltam: {max_erros - errors} tentativa(s)!')


def print_loser_message(secret_word):
  print("Puxa, você foi enforcado!")
  print("A palavra era {}".format(secret_word))
  print("    _______________         ")
  print("   /               \       ")
  print("  /                 \      ")
  print("//                   \/\  ")
  print("\|   XXXX     XXXX   | /   ")
  print(" |   XXXX     XXXX   |/     ")
  print(" |   XXX       XXX   |      ")
  print(" |                   |      ")
  print(" \__      XXX      __/     ")
  print("   |\     XXX     /|       ")
  print("   | |           | |        ")
  print("   | I I I I I I I |        ")
  print("   |  I I I I I I  |        ")
  print("   \_             _/       ")
  print("     \_         _/         ")
  print("       \_______/           ")


def print_winner_message():
  print("Parabéns, você ganhou!")
  print("       ___________      ")
  print("      '._==_==_=_.'     ")
  print("      .-\\:      /-.    ")
  print("     | (|:.     |) |    ")
  print("      '-|:.     |-'     ")
  print("        \\::.    /      ")
  print("         '::. .'        ")
  print("           ) (          ")
  print("         _.' '._        ")
  print("        '-------'       ")


def print_end_game(hit, secret_word):
  if (hit):
    print_winner_message()
  else:
    print_loser_message(secret_word)

  print('Fim do Jogo!')


def draw_gallows(errors):
  print("  _______     ")
  print(" |/      |    ")

  if (errors == 1):
    print(" |      (_)   ")
    print(" |            ")
    print(" |            ")
    print(" |            ")

  if (errors == 2):
    print(" |      (_)   ")
    print(" |      \     ")
    print(" |            ")
    print(" |            ")

  if (errors == 3):
    print(" |      (_)   ")
    print(" |      \|    ")
    print(" |            ")
    print(" |            ")

  if (errors == 4):
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |            ")
    print(" |            ")

  if (errors == 5):
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |            ")

  if (errors == 6):
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |      /     ")

  if (errors == 7):
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |      / \   ")

  print(" |            ")
  print("_|___         ")
  print()


def play():
  print_opening_message()

  secret_word = get_secret_word()
  hit_letters = get_hit_letters_initialized(secret_word)

  hanged = False
  hit = False
  errors = 0
  max_erros = 7

  print(hit_letters)

  while (not hit and not hanged):
    kick = get_kick()

    if (kick in secret_word):
      set_hit(hit_letters, secret_word, kick)
    else:
      errors += 1
      draw_gallows(errors)

    hanged = check_hanged(max_erros, errors)
    hit = check_hit_secret_word(hit_letters)

    if (not hit):
      print_missing_letters(hit_letters)
      print_errors_count(errors)
      print_missing_attempts(max_erros, errors)

    print(hit_letters)

  print_end_game(hit, secret_word)


if (__name__ == "__main__"):
  play()
