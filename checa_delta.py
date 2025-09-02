import requests
from endpoint_origem import Geral, dados_origem
from time import sleep


url = "http://localhost:8000/opcoes"

resposta_get = requests.get(url)
print(resposta_get.json())

lista_inicial = []
lista_nova = []


# gerar lista inicial
resp_inicial = resposta_get.json()
for item in resp_inicial:
        lista_inicial.append(item["nome"])


while True:
    novos_itens = []
    # gerar lista mais recente
    resp_checagem = requests.get(url).json()
    for item in resp_checagem:
          lista_nova.append(item["nome"])
    #checa se algum item da lista atualizada tem na lista velha
    for item in lista_nova:  
        if item not in lista_inicial:
            novos_itens.append(item)
          
    if len(novos_itens) > 0:
        for item in novos_itens:
            lista_inicial.append(item)
            print(f"Item adicionado: {item}")
            
    else:
        print("Não há novos itens.")

    sleep(30)


