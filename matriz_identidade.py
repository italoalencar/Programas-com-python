# Faça um programa em Python que defina duas funções. A primeira, chamada
# cria_matriz_identidade(d), deve criar uma matriz quadrada d x d com valores 1
# na diagonal principal e 0 nas demais posições. A segunda, chamada
# mostra_matriz(matriz), deve mostrar uma matriz na tela, linha por linha. Em seguida,
# leia 2 números inteiros do usuário, A e B (separado por vírgula), e use essas funções para criar e mostrar
# matrizes identidades com todas as ordens de A a B.


# Funções
def cria_matriz_identidade(d):
    matriz = []
    for i in range(d):
        linha = d * [0]
        matriz.append(linha)
        
    for i in range(d):
        for j in range(d):
            if i == j:
                matriz[i][j] = 1
    return matriz
    
def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

# Execução 
entrada = input('Digite o intervalo: ')
intervalo = entrada.split(",")

for i in range(2):
    intervalo[i] = int(intervalo[i])

for i in range(intervalo[0],intervalo[1]+1):
    print('Matriz identidade %dx%d:' % (i,i))
    m = cria_matriz_identidade(i)
    mostra_matriz(m)