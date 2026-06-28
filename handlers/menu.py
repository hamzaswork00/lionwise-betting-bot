from telegram import Update
from telegram.ext import ContextTypes
from database import get_user, get_user_predictions, get_stats
from config import ADMIN_ID
from utils.keyboards import main_menu, back_keyboard
from utils.messages import get_text

async def main_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    uid = query.from_user.id
    user = get_user(uid)
    if not user:
        await query.edit_message_text("❌ Utilisateur non trouvé. Envoie /start.")
        return
    lang = user[3] if user[3] else "fr"
    data = query.data

    if data == "main_menu":
        await query.edit_message_text("🦁 *Menu principal*", parse_mode="Markdown", reply_markup=main_menu(lang))
    elif data == "predict":
        await query.edit_message_text("📸 *Envoie une capture d'écran d'un match* (avec les cotes visibles).\n\nJe l'analyserai et te donnerai un pronostic.", parse_mode="Markdown", reply_markup=back_keyboard(lang))
    elif data == "profile":
        status_map = {"pending": "⏳ En attente", "active": "✅ Actif", "banned": "❌ Banni"}
        text = get_text(lang, "profile").format(uid, status_map.get(user[4], "Inconnu"), lang, user[6][:10] if user[6] else "N/A", user[7][:10] if user[7] else "Non activé")
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_keyboard(lang))
    elif data == "history":
        preds = get_user_predictions(uid)
        if preds:
            lines = [f"📅 {p[7][:10]} : {p[2]} → {p[3]} ({p[4]}%)" for p in preds[:5]]
            text = get_text(lang, "history").format("\n".join(lines))
        else:
            text = get_text(lang, "no_history")
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_keyboard(lang))
    elif data == "about":
        await query.edit_message_text("🦁 *LionWise Betting*\n\nBot IA pour paris sportifs.\nDéveloppé par @Havij_man\nCode promo : LIONSB1", parse_mode="Markdown", reply_markup=back_keyboard(lang))
    elif data == "admin":
        if uid == ADMIN_ID:
            total, pending, active, banned = get_stats()
            text = get_text(lang, "admin_stats").format(total, pending, active, banned)
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_keyboard(lang))
        else:
            await query.answer("⛔ Accès réservé à l'admin.", show_alert=True)
