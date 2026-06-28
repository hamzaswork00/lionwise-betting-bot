from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from database import get_user, create_user, set_language
from utils.keyboards import lang_keyboard, main_menu
from utils.messages import get_text

ASK_ID, ASK_PHOTO = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    user = get_user(uid)
    if not user:
        create_user(uid, update.effective_user.username, update.effective_user.first_name)
        await update.message.reply_text("🌍 Choisis ta langue / Choose your language / اختر لغتك :", reply_markup=lang_keyboard())
        return ConversationHandler.END
    else:
        lang = user[3] if user[3] else "fr"
        status = user[4]
        if status == "banned":
            await update.message.reply_text("❌ Vous êtes banni.")
            return ConversationHandler.END
        elif status == "pending":
            await update.message.reply_text(get_text(lang, "ask_id"))
            return ASK_ID
        else:
            await update.message.reply_text("✅ Déjà actif ! Utilise le menu.", reply_markup=main_menu(lang))
            return ConversationHandler.END

async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data.split("_")[1]
    uid = query.from_user.id
    set_language(uid, lang)
    await query.edit_message_text(get_text(lang, "welcome", "LIONSB1"))
    await query.message.reply_text(get_text(lang, "ask_id"))
    return ASK_ID

async def ask_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    text = update.message.text
    user = get_user(uid)
    lang = user[3] if user[3] else "fr"
    if text.isdigit() and 4 <= len(text) <= 10:
        context.user_data["account_id"] = text
        await update.message.reply_text(get_text(lang, "ask_photo"))
        return ASK_PHOTO
    else:
        await update.message.reply_text("❌ L'ID doit être composé de 4 à 10 chiffres.")
        return ASK_ID
