#!python3

from Cliente import Cliente
from Funcionario import Funcionario

cliente = Cliente()
cliente.nome = "Fulano da Silva"
cliente.endereco = "Rua Sem nome, 999"
cliente.telefone = "41-998890110"
cliente.cpf = "102.113.609-37"
cliente.dataNascimento = "10/02/1982"

funcionario = Funcionario()
funcionario.nome = "Beltrano Gomes"
funcionario.endereco = "Av das coisas, 1000"
funcionario.telefone = "41-32002030"
funcionario.cpf = "215.079.299-00"
funcionario.dataNascimento = "05/12/1985"
funcionario.cargo = "Vendedor"

