def play():
  print("*********************************")
  print("Bem vindo ao jogo da Forca!")
  print("*********************************")

  secret_word = 'banana'
  hanged = False
  hit = False

  while (not hit and not hanged):
    kick = input('Qual letra? ').strip()

    index = 0
    for letter in secret_word:
      if (kick.upper() == letter.upper()):
        print(f'Encontrei a letra {letter.lower()} na posição {index}')
      index += 1


if (__name__ == "__main__"):
  play()
