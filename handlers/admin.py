from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID, ADMIN_GROUP_ID
from database import get_deposit, update_deposit_status, update_user_status, get_user, add_history, get_stats
from utils.keyboards import admin_deposit_keyboard
from utils.messages import get_text

async def notify_admin(update, context, file_id, dep_id):
    uid = update.effective_user.id
    user = get_user(uid)
    username = user[1] if user and user[1] else "inconnu"
    caption = f"📥 Nouvelle demande de dépôt #{dep_id}\n👤 @{username}\n🆔 {uid}"
    await context.bot.send_photo(
        chat_id=ADMIN_GROUP_ID,
        photo=file_id,
        caption=caption,
        parse_mode=None,
        reply_markup=admin_deposit_keyboard(dep_id)
    )

async def admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.from_user.id != ADMIN_ID:
        await query.answer("⛔ Vous n'êtes pas autorisé.", show_alert=True)
        return
    dep_id = int(query.data.split("_")[1])
    dep = get_deposit(dep_id)
    if not dep:
        await query.edit_message_caption("❌ Demande introuvable.")
        return
    uid = dep[1]
    if query.data.startswith("validate"):
        update_deposit_status(dep_id, "approved")
        update_user_status(uid, "active")
        add_history(uid, "activation", "Compte activé via dépôt")
        lang = get_user(uid)[3] or "fr"
        await context.bot.send_message(uid, get_text(lang, "activate"), parse_mode="Markdown")
        await query.edit_message_caption(f"✅ Demande #{dep_id} validée.")
    else:
        update_deposit_status(dep_id, "rejected")
        await query.edit_message_caption(f"❌ Demande #{dep_id} refusée.")

async def admin_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Commande réservée à l'admin.")
        return
    if update.message.text == "/stats":
        total, pending, active, banned = get_stats()
        await update.message.reply_text(
            f"📊 *Statistiques du bot*\n\n👥 Total : {total}\n⏳ En attente : {pending}\n✅ Actifs : {active}\n❌ Bannis : {banned}",
            parse_mode="Markdown"
        )
