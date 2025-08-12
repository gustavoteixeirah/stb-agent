import json
from typing import Any
from smolagents import tool
import os # Importamos a biblioteca os para pegar o nome do arquivo

@tool
def qr_code_reader(image_path: str) -> Any:
    """
    Lê um QR Code de um arquivo de imagem e retorna os dados da prova.

    Args:
        image_path (str): O caminho para o arquivo de imagem contendo o QR Code.

    Returns:
        dict: Um dicionário com os dados da prova, incluindo 'assessment_id', 
              'quantity_of_questions' e 'correct_alternatives'.
    """
    print(f"--- MOCK TOOL: Lendo QR Code de '{image_path}' ---")
    mock_data = {
        "assessment_id": "PROVA_SMOL_2025_Biol_T1",
        "quantity_of_questions": 30,
        "correct_alternatives": {
               "1": [
                    "D"
                ],
                "2": [
                    "B"
                ],
                "3": [
                    "B"
                ],
                "4": [
                    "B"
                ],
                "5": [
                    "D"
                ],
                "6": [
                    "D"
                ],
                "7": [
                    "A"
                ],
                "8": [
                    "E"
                ],
                "9": [
                    "A"
                ],
                "10": [
                    "B"
                ],
                "11": [
                    "C"
                ],
                "12": [
                    "E"
                ],
                "13": [
                    "D"
                ],
                "14": [
                    "C"
                ],
                "15": [
                    "D"
                ],
                "16": [
                    "B"
                ],
                "18": [
                    "B"
                ],
                "19": [
                    "D"
                ],
                "20": [
                    "A"
                ],
                "21": [
                    "E"
                ],
                "22": [
                    "B"
                ],
                "23": [
                    "A"
                ],
                "24": [
                    "A"
                ],
                "25": [
                    "E"
                ],
                "26": [
                    "A"
                ],
                "27": [
                    "C"
                ],
                "28": [
                    "B"
                ],
                "29": [
                    "E"
                ],
                "30": [
                    "E"
                ]
                    }
    }
    
    return mock_data
