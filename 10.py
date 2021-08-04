numero = int(input("Digite o número: "))
multiplicante = 1

while multiplicante > 0:
    if multiplicante <= 10:
        produto = numero * multiplicante
        print("{} vezes {} = {}".format(numero, multiplicante, produto))
        multiplicante += 1
        continue
    elif multiplicante > 10:
        break