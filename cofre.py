# Faça um programa em Python que simule a colocação de notas em um cofre. Seu programa deve iniciar
# lendo do usuário os valores de notas que serão suportados, por exemplo 2, 5 e 10. Em seguida, um
# dicionário representando o cofre deve ser criado com o valor das notas representando as chaves e
# os valores associados sendo as quantidades disponíveis. Inicialmente as quantidades devem ser
# iguais a zero. Por exemplo, {2: 0, 5: 0, 10:0}. Seu programa deve então perguntar para o usuário
# a quantidade de cada tipo de nota no cofre. Por fim, as notas no cofre são mostradas na tela e o
# total de dinheiro (com duas casas decimais) deve ser indicado.


# Entrada
ced = input('Quais os valores de notas do seu cofre? ').split(',')

# Conversão da entrada
for i in range(len(ced)):
    ced[i] = int(ced[i])

# Criação do dicionário
nota = {}
for x in ced:
    nota['%d' % x] = float(input('Quantidade de notas de R$%d: ' % x))

# Saída    
print('Estado do cofre')
soma = 0
for x in ced:
    print('Notas de R$%d: %d' % (x,nota['%d' % x]))
    soma += (x * nota['%d' % x])    
print('Total no cofre: R$%.2f' % soma)