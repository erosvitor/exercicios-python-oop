#!python3

import Produto

prod = Produto.Produto()
prod.descricao = "Caneta"
prod.preco = 1.50

print("Preço distribuidor:", prod.precoDistribuidor())
print("Preço representante:", prod.precoRepresentante())
print("Preço consumidor:", prod.precoConsumitor())
