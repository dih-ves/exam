import tempfile
import random


'''
with open("my_file.txt") as file:
    data = file.read()
'''

#abra um arquivo temporário
arquivoTemporario = tempfile.TemporaryFile()
#print ('AQUIII:', tempfile.gettempdir())

#escreva nesse arquivo 30 linhas com string randomica

def gerar_numero_aleatorio():
    n_aleatorio= random.random()
    n_aleatorio = str(n_aleatorio)
    n_aleatorio_bytes = bytes(n_aleatorio, 'utf-8')
    return n_aleatorio_bytes

#a = gerar_numero_aleatorio()
#print('aqui:', a)


''' Escrevendo 30 vezes no arquivo '''

def gravar_info_lista():
    lista = []
    i = 0
    while i < 30:
        i+=1
        
        b = lista.append(gerar_numero_aleatorio())
        #print ('Lista depois de adc os numeros aleatorios',lista)
        arquivo_com_informacao = arquivoTemporario.writelines(lista)
        print('TESTE:', arquivo_com_informacao)
    return arquivoTemporario

#a = gravar_info_lista()
#print(a)

def ler_arquivo():
    a = gravar_info_lista()
    print('Arquivo:', a)
    for x in a:
        print(x)

a = ler_arquivo()
print(a)


#obj_serialized = pickle.dumps(lista)
#arquivoTemporario.write()

#leia o conteudo deste arquivo e exiba no console
#print(str(arquivoTemporario.read(), encoding='utf8'))



''' Fechando o arquivo temporário '''
arquivoTemporario.close()