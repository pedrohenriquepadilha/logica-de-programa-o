dados_sujos = [
	"  JOAO.SILVA@EXEMPLO.COM ",
	"Maria Souza",
	" Rua das Flores, No 25 ",
]

dados_limpos = []

for item in dados_sujos:
	item = item.strip()

	if "@" in item:
		item = item.lower()

	if "No" in item:
		item = item.replace("No", "Número")

	dados_limpos.append(item)

print(dados_limpos)