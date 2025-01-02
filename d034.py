# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais a R$ 1.250,00, o aumento será de 15%.

salario = float(input('Informe o salário do funcionario : '))
ajuste1 = (salario*10/100) + salario
ajuste2 = (salario*15/100) + salario
if salario > 1250 : 
    print(f'O salário do trabalhador é {salario} e teve um ajuste para {ajuste1}')
else : 
    print(f'O salário do trabalhador é {salario} e teve um ajuste para {ajuste2}')              
    