def notas(*nums, sit= False):
    """
        Recebe várias notas e mostra um boletim
        param nums: notas (recebe várias)
        param sit: mostra ou não a situação do aluno (opcional)
        return boletim: dicionário com quantidade de notas, maior nota, menor nota, médis e situação(If sit == True)
    """
    boletim = dict()
    boletim['quantidade'] = len(nums)
    boletim['maior']= max(nums)
    boletim['menor'] = min(nums)
    boletim['média'] = sum(nums)/len(nums)
    if sit == True:
        if boletim['média']>7:
            boletim['situação'] = 'Boa'
        elif 6 <= boletim['média'] < 7:
            boletim['situação'] = 'Razoável'
        else:
            boletim['situação']  = 'Ruim'
    return boletim
    



resp = notas(5.5,2.5,1.5,sit=True)
print(resp)