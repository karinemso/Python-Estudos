from xmlrpc.server import DocXMLRPCRequestHandler


real = float(input('Quantos reais você tem na carteira? R$'))
dolar = 5.23
convert = real/dolar

print(f'Você tem R${real}, portanto pode comprar US${convert:.2f}')