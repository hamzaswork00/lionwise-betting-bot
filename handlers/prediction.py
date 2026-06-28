from telegram import Update
from telegram.ext import ContextTypes
from database import get_user, add_prediction
from services.groq_vision import analyze_image
from services.groq_prediction import generate_prediction
from utils.keyboards import main_menu
from utils.messages import get_text

async def handle_match_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    user = get_user(uid)
    if not user or user[4] != "active":
        await update.message.reply_text("❌ Vous devez être actif pour utiliser cette fonction.")
        return
    lang = user[3] if user[3] else "fr"
    file = await update.message.photo[-1].get_file()
    image_bytes = await file.download_as_bytearray()
    data = analyze_image(image_bytes)
    if not data.get("account_id") or not data.get("bet_type"):
        await update.message.reply_text("❌ Je n'ai pas réussi à lire la capture. Essaie avec une image plus claire (cotes visibles).")
        return
    team1 = data.get("account_id", "Équipe A")
    team2 = data.get("balance", "Équipe B")
    bet_type = data.get("bet_type", "Inconnu")
    odds = data.get("odds", "N/A")
    pred = generate_prediction(team1, team2, bet_type, odds)
    add_prediction(uid, f"{team1} vs {team2}", pred.get("prediction", "N/A"), pred.get("confidence", 0), odds, pred.get("analysis", ""))
    result_text = get_text(lang, "prediction_result").format(bet_type, f"{team1} 🆚 {team2}", pred.get("confidence", 0), odds, pred.get("analysis", "Analyse non disponible"))
    await update.message.reply_text(result_text, parse_mode="Markdown", reply_markup=main_menu(lang))
