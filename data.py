telefone = input("digite o telefone na formato (XX)XXXXX-XXXX")

ddd = telefone[1:3]
numero = telefone[4:]

print(f"DDD: {ddd}")
print(f"Número: {numero}")

data = input("digite a sua data de nascimento (DD/MM/AAAA):")

dia = data[0:2]
mes = data[3:5]
ano = data[6:]

print(f"Dia: {dia}")
print(f"Mês: {mes}")
pritn(f"Ano: {Ano}")

email = input("digite seu e-mail (nome.sobrenome@escola.com)")

primeiro_nome  = email[0:5]
dominío = email[13:]

print(f"Primeiro nome extraído: {primeiro_nome}")
print(f"dominío extraído: {dominío}")