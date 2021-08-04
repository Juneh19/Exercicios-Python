valor = input("Digite qualquer coisa, qualquer coisa mesmo: ")

if valor.isspace():
    print("Você só digitou um espaço, sacana.")
elif valor.isnumeric():
    print("Você digitou um número.")
elif valor.isalpha():
    print("Você digitou uma letra.")
else:
    print("Você digitou algum símbolo estranho, fio da mãe.")
