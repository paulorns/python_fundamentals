#!/usr/bin/python3

valor_hora = float(input('Digite o valor da sua hora de trabalho: '))
qtd_horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = qtd_horas * valor_hora
salario_liquido = salario_bruto

print('\nHoras trabalhadas no mês:', valor_hora)
print('Valor da hora: ', qtd_horas)
print('Salário Bruto: R$', salario_bruto)

if salario_bruto <= 1900:
    desconto_ir = 0
    print('(-) IR (Isento): R$', desconto_ir)
elif salario_bruto >= 1901 and salario_bruto <= 2800:
    desconto_ir = salario_bruto*0.07
    print('(-) IR (7%): R$', desconto_ir)
    salario_liquido -= desconto_ir
elif salario_bruto >= 2801 and salario_bruto <= 3700:
    desconto_ir = salario_bruto*0.15
    print('(-) IR (15%): R$', desconto_ir)
    salario_liquido -= desconto_ir
elif salario_bruto >= 3701 and salario_bruto <= 4600:
    desconto_ir = salario_bruto*0.22
    print('(-) IR (22%): R$', desconto_ir)
    salario_liquido -= desconto_ir
else:
    desconto_ir = salario_bruto*0.27
    print('(-) IR (27%): R$', desconto_ir)
    salario_liquido -= desconto_ir

valor_sindicato = salario_bruto * 0.03
salario_liquido -= valor_sindicato
print('(-) Sindicato (3%): R$', valor_sindicato)
print('FGTS (11%): R$', salario_bruto*0.11)
print('Total dos descontos: R$', desconto_ir+valor_sindicato)
print('Salário Líquido: R$', salario_liquido)
