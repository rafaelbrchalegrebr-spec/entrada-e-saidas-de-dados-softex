import random

opcoes = ["pedra", "papel", "tesoura"]

# Escolha do usuário
usuario = input("Escolha pedra, papel ou tesoura: ").lower()

# Validação da escolha
if usuario not in opcoes:
    print("Escolha inválida. Tente novamente.")
else:
    computador = random.choice(opcoes)
    print(f"Você escolheu: {usuario}")
    print(f"O computador escolheu: {computador}")

    if usuario == computador:
        print("Empate!")
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "tesoura" and computador == "papel") or \
         (usuario == "papel" and computador == "pedra"):
        print("Você venceu! 🎉")
    else:
        print("O computador venceu! 💻")