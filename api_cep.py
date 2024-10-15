import requests

# Solicita ao usuário que informe o CEP
cep = input('Informe o CEP: ')

# Constrói o link de acesso à API ViaCEP
link = f'https://viacep.com.br/ws/{cep}/json/'

# Realiza a requisição GET para obter os dados do CEP
requisicao = requests.get(link)

# Verifica se a requisição foi bem-sucedida (código de resposta 200)
if requisicao.status_code == 200:
    # Converte os dados da resposta para um dicionário
    dados_cep = requisicao.json()

    # Extrai e exibe as informações do CEP
    uf = dados_cep.get('uf')
    cidade = dados_cep.get('localidade')
    bairro = dados_cep.get('bairro')

    # Exibe as informações
    print(f'Estado (UF): {uf}')
    print(f'Cidade: {cidade}')
    print(f'Bairro: {bairro}')
else:
    print(f'Erro ao consultar o CEP: código {requisicao.status_code}')

