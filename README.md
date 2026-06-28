# 🦁 LionWise Betting Bot

Bot Telegram intelligent pour affilié 1xBet avec analyse d'images par IA (Groq), menu interactif complet, validation admin via groupe, et support multilingue (FR/EN/AR).

---

## 🚀 Fonctionnalités

- 🤖 **IA Groq intégrée** : Analyse d'images de matchs + génération de pronostics
- 📸 **Analyse visuelle** : Capture d'écran 1xBet → extraction auto des cotes & infos
- 🎯 **Pronostics IA** : Confiance en % + analyse détaillée en 2-3 phrases
- 💰 **Validation des dépôts** : Workflow photo → groupe admin → activation
- 🌍 **Multilingue** : Français, Anglais, Arabe
- 📊 **Statistiques** : Commandes /stats pour l'admin
- 🗃️ **SQLite** : Base de données locale légère

---

## 📁 Structure du projet

```
lionwise-betting-bot/
├── bot.py                      # Point d'entrée principal
├── config.py                   # Variables d'environnement
├── database.py                 # Base de données SQLite
├── requirements.txt            # Dépendances Python
├── Dockerfile                  # Image Docker (Back4App)
├── .dockerignore               # Fichiers ignorés par Docker
├── README.md                   # Ce fichier
├── handlers/                   # Gestionnaires de commandes
│   ├── __init__.py
│   ├── start.py               # /start + inscription
│   ├── deposit.py             # Gestion des dépôts
│   ├── prediction.py          # Analyse de matchs
│   ├── menu.py                # Menu interactif
│   └── admin.py               # Commandes admin
├── services/                   # Services externes
│   ├── __init__.py
│   ├── groq_vision.py         # Analyse d'images Groq
│   └── groq_prediction.py     # Génération de pronostics
└── utils/                      # Utilitaires
    ├── __init__.py
    ├── keyboards.py           # Claviers Telegram
    └── messages.py            # Textes multilingues
```

---

## 🔧 Variables d'environnement

| Variable | Description |
|----------|-------------|
| `BOT_TOKEN` | Token du bot Telegram (depuis @BotFather) |
| `ADMIN_ID` | Telegram ID de l'administrateur |
| `ADMIN_GROUP_ID` | ID du groupe pour les notifications dépôts |
| `GROQ_API_KEY` | Clé API Groq (gratuite sur [groq.com](https://groq.com)) |

---

## 🐳 Déploiement sur Back4App (Docker)

### Étape 1 : Créer un compte
1. Va sur [Back4App](https://www.back4app.com) (gratuit, sans CB)
2. Crée un compte

### Étape 2 : Pousser sur GitHub
1. Crée un nouveau repository sur GitHub
2. Upload tous les fichiers de ce projet

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/TON_USER/lionwise-betting-bot.git
git push -u origin main
```

### Étape 3 : Déployer sur Back4App
1. Dans Back4App, clique **"Create New App"**
2. Choisis **"Deploy via GitHub"**
3. Connecte ton compte GitHub et sélectionne le repo
4. Back4App détecte automatiquement le `Dockerfile`

### Étape 4 : Variables d'environnement
Dans l'interface Back4App, va dans **Settings > Environment Variables** et ajoute :

```env
BOT_TOKEN=<TON_BOT_TOKEN>
ADMIN_ID=<TON_ADMIN_ID>
ADMIN_GROUP_ID=<TON_ADMIN_GROUP_ID>
GROQ_API_KEY=<TA_CLE_API_GROQ>
```

> ⚠️ **Ne mets jamais tes vraies clés dans le README ou dans le code !** Utilise toujours les variables d'environnement.

### Étape 5 : Lancer
- Clique **Deploy** dans Back4App
- Le bot démarre automatiquement en **polling** (pas besoin de webhook)
- Vérifie les logs dans l'onglet **Logs**

---

## 🏃 Exécution locale (développement)

```bash
# 1. Cloner le projet
git clone https://github.com/TON_USER/lionwise-betting-bot.git
cd lionwise-betting-bot

# 2. Créer un environnement virtuel
python -m venv venv

# 3. Activer (Linux/Mac)
source venv/bin/activate
# ou (Windows)
venv\Scripts\activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Créer un fichier .env avec TES propres valeurs
cat > .env << 'EOF'
BOT_TOKEN=<TON_BOT_TOKEN>
ADMIN_ID=<TON_ADMIN_ID>
ADMIN_GROUP_ID=<TON_ADMIN_GROUP_ID>
GROQ_API_KEY=<TA_CLE_API_GROQ>
EOF

# 6. Lancer le bot
python bot.py
```

---

## 🔄 Modèles Groq utilisés

| Usage | Modèle | Description |
|-------|--------|-------------|
| Vision | `llava-v1.5-7b-4096-preview` | Analyse des captures d'écran 1xBet |
| Pronostics | `gemma2-9b-it` | Génération des pronostics et analyses |

---

## 📱 Flux utilisateur

1. **/start** → Choix de la langue
2. **Envoie ID 1xBet** → Validation format
3. **Envoie capture solde** → Notif groupe admin
4. **Admin valide** → Compte activé
5. **Menu principal** → Pronostics / Profil / Historique
6. **Envoie capture match** → IA analyse + pronostic

---

## 👤 Commandes Admin

| Commande | Description |
|----------|-------------|
| `/stats` | Statistiques globales (total, en attente, actifs, bannis) |
| Boutons ✅/❌ | Valider/Refuser les demandes de dépôt dans le groupe |

---

## 🔒 Sécurité

- Le bot vérifie l'`ADMIN_ID` pour toutes les commandes sensibles
- Les callback queries admin sont protégées
- Clés API en variables d'environnement (jamais en dur dans le code)
- SQLite avec `check_same_thread=False` pour le multi-threading

---

## 📝 License

Projet privé - LionWise Betting.

Développé avec ❤️ par @Havij_man.
