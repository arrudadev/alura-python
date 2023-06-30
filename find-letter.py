word = "banana"

user_input_letter = input("Digite uma letra: ")

findInIndex = word.find(user_input_letter)

print("Usando a função find:")
print(f"Encontrei a letra {user_input_letter} no index {findInIndex}")

print("=============================")

print("Usando interação na palavra:")

index = 0
for letter in word:
  if letter == user_input_letter:
    print(f"Encontrei a letra {user_input_letter} no index {index}")
  index += 1
