import time
import requests
import json

# Caminho para o arquivo
file_path = r"C:\"

# URL do endpoint para enviar os dados
url = "http://"

def send_request(json_data):
    try:
        response = requests.post(url, json=json_data)
        if response.status_code == 200 or 201:
            print(f"Requisição para o representante {json_data['rep']} foi bem-sucedida.")
        else:
            print(f"Erro ao enviar para o representante {json_data['rep']}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Falha ao enviar para o representante {json_data['rep']}: {e}")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        json_list = json.loads(data)
except FileNotFoundError:
    print(f"O arquivo {file_path} não foi encontrado.")
except json.JSONDecodeError:
    print("Erro ao decodificar o JSON. Verifique o formato do arquivo.")

for data in json_list:
    send_request(data)
    time.sleep(1)

print("Processo concluído.")
