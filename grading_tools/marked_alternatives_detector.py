import requests
from typing import Any
from smolagents import tool
import os # Importamos a biblioteca os para pegar o nome do arquivo

@tool
def marked_alternatives_detector(image_path: str) -> Any:
    """
    Detects marked alternatives from the answer sheet image by calling a remote API.

    Args:
        image_path: The local path to the image file.

    Returns:
        The JSON response from the API.
    """
    # URL do endpoint da sua API
    api_url = 'http://localhost:8000/detect_marks'

    # Verifica se o arquivo de imagem existe no caminho fornecido
    if not os.path.exists(image_path):
        return {"error": f"File not found at path: {image_path}"}

    try:
        # Abre o arquivo de imagem em modo de leitura binária ('rb')
        with open(image_path, 'rb') as f:
            # Prepara os dados do formulário para o upload.
            # A chave 'file' deve corresponder ao que a API espera.
            # O curl --form 'file=@/caminho/...' se traduz para este dicionário.
            files = {'file': (os.path.basename(image_path), f)}

            # Faz a requisição POST para a API com o arquivo
            response = requests.post(api_url, files=files)

            # Lança uma exceção se a requisição falhou (ex: status 4xx ou 5xx)
            response.raise_for_status()

            # Retorna a resposta da API, geralmente em formato JSON
            return response.json()

    except requests.exceptions.RequestException as e:
        # Captura erros de conexão, timeout, etc.
        print(f"An error occurred while calling the API: {e}")
        return {"error": "Failed to connect to the detection API.", "details": str(e)}
    except Exception as e:
        # Captura outros erros inesperados (ex: erro ao ler o arquivo)
        print(f"An unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred.", "details": str(e)}
