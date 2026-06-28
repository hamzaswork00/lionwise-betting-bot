from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu(lang):
    texts = {
        "fr": {"predict": "🔮 Pronostics", "profile": "👤 Profil", "history": "📜 Historique", "admin": "⚙️ Admin", "about": "ℹ️ À propos"},
        "en": {"predict": "🔮 Predictions", "profile": "👤 Profile", "history": "📜 History", "admin": "⚙️ Admin", "about": "ℹ️ About"},
        "ar": {"predict": "🔮 توقعات", "profile": "👤 الملف الشخصي", "history": "📜 السجل", "admin": "⚙️ المدير", "about": "ℹ️ حول"}
    }
    t = texts.get(lang, texts["fr"])
    keyboard = [
        [InlineKeyboardButton(t["predict"], callback_data="predict")],
        [InlineKeyboardButton(t["profile"], callback_data="profile")],
        [InlineKeyboardButton(t["history"], callback_data="history")],
        [InlineKeyboardButton(t["admin"], callback_data="admin")],
        [InlineKeyboardButton(t["about"], callback_data="about")]
    ]
    return InlineKeyboardMarkup(keyboard)

def lang_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🇫🇷 Français", callback_data="lang_fr"),
         InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
         InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar")]
    ])

def admin_deposit_keyboard(dep_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Valider", callback_data=f"validate_{dep_id}"),
         InlineKeyboardButton("❌ Refuser", callback_data=f"reject_{dep_id}")]
    ])

def back_keyboard(lang):
    text = "🔙 Retour" if lang == "fr" else "🔙 Back" if lang == "en" else "🔙 العودة"
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, callback_data="main_menu")]])
