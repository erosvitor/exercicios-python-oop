class Funcionario:

  def __init__(self):
    self.nome = ""
    self.cargo = ""
    self.valorHora = ""

  def calcularSalario(self, horasTrabalhadas):
    return self.valorHora * horasTrabalhadas