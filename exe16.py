def total (a, b):
    valorTotal = a * b
    return valorTotal

unit = float(input("Digite o preço do produto: "))
qtd = float(input("Digite a quantidade comprada: "))
print(total(unit, qtd))