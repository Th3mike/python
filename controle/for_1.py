"""for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 100, 7):
    print(i)

nums = [2, 4, 6, 8]

for n in nums:
    print(n, end=' ')

texto = 'Python é muito massa!'

for letra in texto:
    print(letra, end=' ')

for n in {1, 2, 3, 4, 5, 6, 7, 8, 9, 'meu deus'}:
    print(n, end=' ')

for atrib in produto:
    print(atrib, '===>', produto[atrib])"""

produto = {
    'nome': 'Poco Phone',
    'preco': 1.650,
    'desc': 0.5
}

for atrib, valor in produto.items():
    print(atrib, '==>', valor)

for valor in produto.values():
    print(valor, end=' ')

for atrib in produto.keys():
    print(atrib, end=' ')