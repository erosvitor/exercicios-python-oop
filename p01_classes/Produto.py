class Produto:

  def __init__(self):
    self.descricao = ""
    self.preco = 0

  def precoDistribuidor(self):
    return self.preco + (self.preco * (3/100))

  def precoRepresentante(self):
    return self.preco + (self.preco * (4.5/100))

  def precoConsumitor(self):
    return self.preco + (self.preco * (5.5/100))