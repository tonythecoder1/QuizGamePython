import requests
import html

parameters = {
    "amount": 10,            # Número de perguntas
    "category": 15,          # (Opcional) Categoria: 15 = Video Games
    "difficulty": "medium",  # (Opcional) Nível de dificuldade: easy, medium, hard
    "type": "boolean"        # Tipo: "boolean" = True/False, "multiple" = múltipla escolha
}

response = requests.get("https://opentdb.com/api.php?amount=10&category=15&difficulty=medium&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
