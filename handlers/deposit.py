from telegram import Update
from telegram.ext import ContextTypes
from database import add_deposit, get_user
from handlers.admin import notify_admin
from utils.messages import get_text

async def handle_deposit_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    user = get_user(uid)
    if not user:
        await update.message.reply_text("❌ Utilisateur non trouvé. Envoie /start.")
        return
    lang = user[3] if user[3] else "fr"
    file_id = update.message.photo[-1].file_id
    dep_id = add_deposit(uid, file_id)
    await notify_admin(update, context, file_id, dep_id)
    await update.message.reply_text(get_text(lang, "deposit_ok"))
    return -1
