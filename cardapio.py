# Mini Sistema 1: Cardápio Simples

cardapio = {
    1: ("Skirt", 79.00),
    2: ("Picanha", 130.00),
    3: ("Refrigerante", 9.00)
}

print("------ CARDÁPIO ------")
for codigo, (item, preco) in cardapio.items():
    print(f"{codigo} - {item} - R${preco:.2f}")

escolha = int(input("\nDigite o código do item desejado: "))

if escolha in cardapio:
    item, preco = cardapio[escolha]
    print(f"\nVocê escolheu: {item} - R${preco:.2f}")
else:
    print("\nOpção inválida.")