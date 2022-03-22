# Faça um programa em Python que lê do usuário suas notas em múltiplas disciplinas. As notas devem ser
# organizadas em uma lista contendo um dicionário para cada disciplina. Cada dicionário deve possuir os
# campos 'nome' (uma string), 'notas' (uma lista de 3 floats) e 'média' (um float). Seu programa deve
# iniciar perguntando ao usuário o número de disciplinas e ler do usuário o nome e 3 notas de cada disciplina.
# Você deve ainda computar a média obtida em cada disciplina, preenchendo esse valor no campo 'média' dos
# dicionários criados. Ao final, mostre as informações de cada disciplina ao usuário, mostrando as notas
# com 1 casa decimal.


# Funções
def criar_disc():
    disciplina = {}
    disciplina['Nome'] = input('Qual o nome da disciplina? ')
    apoio = input('Digite as 3 notas da disciplina separadas por vírgulas: ').split(',')    
    disciplina['Notas'] = []
    soma = 0
    for x in range(len(apoio)):
        disciplina['Notas'].append(float(apoio[x]))
        soma += disciplina['Notas'][x]        
    disciplina ['Média'] = soma / 3
    return disciplina
        
def printar_disc(disciplina):
    print('%s' % disciplina['Nome'])    
    for k in range(3):
        print('Nota %d: %.1f' % (k+1, disciplina['Notas'][k]))
    print('Média: %.1f' % disciplina['Média'])

        
# Execução
disciplinas = []
num_disc = int(input('Qual o número de disciplinas? '))

for i in range(num_disc):
    disciplina = criar_disc()
    disciplinas.append(disciplina)
    	
for disciplina in disciplinas:
    printar_disc(disciplina)