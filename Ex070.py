total = totmil = menor = cont = 0
while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("preço do produto: R$"))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            baratp = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {totmil} Produtos Custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
