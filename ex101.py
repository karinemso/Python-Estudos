
def voto(ano):
    """
        Informa a obrigatoriedade de voto de acordo com o ano de nascimento
        param ano: ano de nascimento
        return: idade e sit em uma string
    """
    from datetime import datetime
    
    atual = datetime.now().year
    idade = atual - ano
    if idade >= 18 and idade <= 70:
        sit ='Obrigatório'
    elif idade > 70 or 16 <= idade < 18:
        sit ='Facultativo'
    else:
        sit ='Negado'
    return f'Com {idade} anos, o voto é: {sit}'
    


nascimento = int(input('Digite seu ano de nascimento:'))
print(voto(nascimento))
help(voto)
    


