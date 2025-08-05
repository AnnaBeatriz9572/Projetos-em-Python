#escrevendo no arquivo
arquivo = open('arq.text.txt', 'w')
arquivo.write('Curso de python\n')
arquivo.write('Aula prática')
arquivo.close()
#lendo o arquivo
arquivo = open('arq.text.txt', 'r')
print(arquivo.read())
arquivo.close()
