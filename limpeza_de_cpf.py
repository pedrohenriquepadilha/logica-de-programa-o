cpf = " 123.456.789-00 "
Telefone = "(11) 99999-8888"

cpf_higienizado = cpf.strip().replace(".", "").replace("-", "").replace(" ", "")
Telefone_higienizado = Telefone.strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

print("cpf higienizado:", cpf_higienizado)
print("telefone higienizado:", Telefone_higienizado)
