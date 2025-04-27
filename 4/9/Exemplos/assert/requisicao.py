import requests
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = requisicao.json()
cotacao = requisicao_dic["USDBRL"]["bid"]
print(type(cotacao), cotacao)
preco_produto = 100 # DOLAR
cotacao = float(cotacao)
assert type(cotacao) == float, "Cotacao não é do tipo FLOAT"
faturamento = preco_produto * cotacao
print('o preco do produto de ', preco_produto, 'em dolares, é igual a ', faturamento)

preco_produto_2 = 1265 # DOLAR
faturamento_2 = preco_produto_2 * cotacao
print('o preco do produto de ', preco_produto_2, 'em dolares, é igual a ', faturamento_2)