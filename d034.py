#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a 1.250,00, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Informe o salário do funcionario : '))
ajuste1 = (salario*10/100) + salario
ajuste2 = (salario*15/100) + salario
if salario > 1250 : 
    print(f'O salário do trabalhador é {salario} e teve um ajuste para {ajuste1}')
else : 
    print(f'O salário do trabalhador é {salario} e teve um ajuste para {ajuste2}')              
    