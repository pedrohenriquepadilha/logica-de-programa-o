valor = 1200.00

print("====================================")
print("TABELA DE PARCELAMENTO - COMPRA R$ 1200.00")
print("====================================")

for parcela in range(1, 11):
    valor_parcela = valor / parcela
    print(f"{parcela}x de R$ {valor_parcela:.2f}")

print("====================================")


