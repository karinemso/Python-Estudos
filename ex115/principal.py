from utilidades import interface
from utilidades import arquivo


arq = 'ex115\cursoemvideo.txt'
if not arquivo.existeArquivo(arq):
    arquivo.criaArquivo(arq)
interface.show(arq)
print('Muito obrigada! Volte sempre!')
