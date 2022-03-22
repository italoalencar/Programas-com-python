# Faça um programa em Python que leia do usuário uma frase e uma palavra. Em seguida,
# indique quantas vezes a palavra em questão aparece na frase e em que posições.
# Ignore a diferença entre minúsculas e maiúsculas.

frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra: ')

print('Frase digitada: %s' % frase)
print('Palavra digitada: %s' % palavra)

i = 0
while i >= 0:
    i = frase.find(palavra,i)
    if i >= 0:
        print('%s aparece na posição %d' % (palavra,i))
        i += 1