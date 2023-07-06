def play():
  print("*********************************")
  print("Bem vindo ao jogo da Forca!")
  print("*********************************")

  secret_word = 'banana'.upper()
  hit_letters = ['_' for letter in secret_word]
  hanged = False
  hit = False
  errors = 0
  max_erros = 6

  print(hit_letters)

  while (not hit and not hanged):
    kick = input('Qual letra? ').strip().upper()

    if (kick in secret_word):
      index = 0
      for letter in secret_word:
        if (kick.upper() == letter.upper()):
          hit_letters[index] = letter
        index += 1
    else:
      errors += 1

    hanged = errors == max_erros
    hit = "_" not in hit_letters

    if (not hit):
      missing_letters = str(hit_letters.count('_'))
      print(f'Ainda faltam acertar {missing_letters} letra(s)!')
      print(f'Errou: {errors} letra(s)!')
      print(f'Faltam: {max_erros - errors} tentativa(s)!')

    print(hit_letters)

  if (hit):
    print('Você ganhou!')
  else:
    print('Você perdeu!')

  print('Fim do Jogo!')


if (__name__ == "__main__"):
  play()
