matriz = [
    [3, 8, 1],
    [4, 9, 6],
    [2, 7, 5],
]
print("=== EXIBIÇÃO DE MATRIZ EM FORMATO DE GRADE")
for i in range(3):
    for c in range(3):
        print(f"{matriz[1][c]}", end=" ")
    print()

print(f"Elemento na linha 0, Coluna 1: {matriz[0][1]}")
print(f"Elemento na linha 2, Coluna 2: {matriz[2][2]}")

soma_diagonal = 0
for i in range(3):
    for c in range(3):
        if l == c:
            soma_diagonal += matriz[1][c]
            print(f"SOMA DOS ELEMENTOS NA DIAGONAL: {soma_diagonal}")