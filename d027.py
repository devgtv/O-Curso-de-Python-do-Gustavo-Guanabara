# Pergunte ao usuário o seu nome completo e informe seu primeiro e último nome.

n = str(input('Qual e o seu nome completo ? ')).strip()
p = n.split()
ultimo = p[-1]
print(f'Seu primeiro nome é {p[0]}')
print(f'Seu ultimo nome é {ultimo}')