total = 0
quantidade = int(input("Digite a quantidade de itens: "))

for i in range(1, quantidade + 1):
    preco = float(input(f"Digite o preço do item {i}: R$ "))
    total += preco

media = total / quantidade

print("\n===== RESULTADO =====")
print(f"Total da compra: R$ {total:.2f}")
print(f"Média por item: R$ {media:.2f}")