import requests
import base64
import json
import re
from config import GROQ_API_KEY

def analyze_image(image_bytes):
    if not GROQ_API_KEY:
        return {"account_id": None, "balance": None, "bet_type": None, "odds": None}
    
    API_URL = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    b64 = base64.b64encode(image_bytes).decode('utf-8')
    prompt = (
        "Analyse cette capture d'écran de l'application 1xBet. "
        "Extrais le numéro de compte (account_id), le solde (balance), "
        "le type de pari (bet_type) et les cotes (odds) si c'est un match. "
        "Réponds UNIQUEMENT en JSON avec les clés : account_id, balance, bet_type, odds."
    )
    payload = {
        "model": "llava-v1.5-7b-4096-preview",
        "messages": [
            {"role": "user", "content": [{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}]}
        ],
        "temperature": 0.1,
        "max_tokens": 300
    }
    try:
        r = requests.post(API_URL, headers=headers, json=payload, timeout=25)
        r.raise_for_status()
        content = r.json()["choices"][0]["message"]["content"]
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return {"account_id": None, "balance": None, "bet_type": None, "odds": None}
    except Exception as e:
        print(f"Erreur Groq vision: {e}")
        return {"account_id": None, "balance": None, "bet_type": None, "odds": None}
