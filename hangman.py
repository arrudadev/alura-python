def play():
  print("*********************************")
  print("Bem vindo ao jogo da Forca!")
  print("*********************************")

  secret_word = 'banana'
  hit_letters = ['_', '_', '_', '_', '_', '_']
  hanged = False
  hit = False

  print(hit_letters)

  while (not hit and not hanged):
    kick = input('Qual letra? ').strip()

    index = 0
    for letter in secret_word:
      if (kick.upper() == letter.upper()):
        hit_letters[index] = letter
      index += 1

    missing_letters = str(hit_letters.count('_'))

    print(f'Ainda faltam acertar {missing_letters}')
    print(hit_letters)


if (__name__ == "__main__"):
  play()
