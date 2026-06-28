import requests
import json
import re
from config import GROQ_API_KEY

def generate_prediction(team1, team2, bet_type, odds):
    if not GROQ_API_KEY:
        return {"prediction": "Erreur", "confidence": 50, "analysis": "Clé API manquante."}
    
    API_URL = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    prompt = (
        f"Match : {team1} vs {team2}\n"
        f"Type de pari : {bet_type}\n"
        f"Cotes : {odds}\n"
        "Donne une prédiction avec un pourcentage de confiance (0-100) et une analyse en 2-3 phrases. "
        "Réponds UNIQUEMENT en JSON avec les clés : prediction, confidence, analysis."
    )
    payload = {
        "model": "gemma2-9b-it",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 250
    }
    try:
        r = requests.post(API_URL, headers=headers, json=payload, timeout=25)
        r.raise_for_status()
        content = r.json()["choices"][0]["message"]["content"]
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return {"prediction": "Erreur", "confidence": 50, "analysis": "L'IA n'a pas pu générer une analyse."}
    except Exception as e:
        print(f"Erreur Groq prediction: {e}")
        return {"prediction": "Erreur", "confidence": 50, "analysis": "Erreur lors de l'appel à l'API."}
