import hangman
import divination


def choose_game():
  print("*********************************")
  print("****** Escolha o seu jogo! ******")
  print("*********************************")

  print("(1) Forca (2) Adivinhação")

  game = int(input('Qual jogo? '))

  if (game == 1):
    hangman.play()
  elif (game == 2):
    divination.play()
  else:
    print('Opção inválida!')


if (__name__ == "__main__"):
  choose_game()
