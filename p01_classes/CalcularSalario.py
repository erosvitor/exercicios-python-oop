#!python3

import Funcionario

func = Funcionario.Funcionario()
func.nome = "Fulano"
func.cargo = "Vendedor"
func.valorHora = 14.50

horasTrabalhadas = 30
salario = func.calcularSalario(horasTrabalhadas)

print("O salário é: ", salario)
