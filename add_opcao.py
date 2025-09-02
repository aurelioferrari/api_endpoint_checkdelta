import requests

url = "http://localhost:8000/opcoes"

nova_opcao = {
    "id": "10",
    "nome": "Opção 10"
}

resposta_post = requests.post(url, json=nova_opcao)
print(resposta_post.json())