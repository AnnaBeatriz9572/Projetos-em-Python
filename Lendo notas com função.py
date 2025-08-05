def lernotas():
    n = float(input('Digite a nota: '))
    return n
def resultado(A, B):
    s = (A + B)/2
    print('Nota 1: ', A)
    print('Nota 2: ', B)
    print('Resultado: ', s)
    if s >= 7.0:
        print('Aprovado')
    else:
        print('Reprovado')

a = lernotas()
b = lernotas()
resultado(a,b)
