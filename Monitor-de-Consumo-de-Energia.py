total = 0

dias_acima = 0

for dia in range(1, 8):
    consumo = float(input(f"Digite o consumo do dia {dia} (kWh): "))
    total += consumo
    if consumo > 20:
        dias_acima += 1

print("\n===== RESULTADO =====")
print(f"Consumo total da semana: {total:.2f} kWh")
print(f"Dias com consumo acima de 20 kWh: {dias_acima}")
