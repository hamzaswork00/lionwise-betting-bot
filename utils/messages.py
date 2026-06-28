LOCALES = {
    "fr": {
        "welcome": "🦁 *Bienvenue sur LionWise Betting !*\n\nCode promo : `{}`\n\n1️⃣ Crée un compte 1xBet\n2️⃣ Envoie ton ID (ex: 123456)\n3️⃣ Envoie une capture de ton solde",
        "ask_id": "📝 Envoie ton *ID 1xBet* (les chiffres) :",
        "ask_photo": "📸 Envoie une capture de ton solde.",
        "deposit_ok": "✅ Reçu ! En attente de validation.",
        "activate": "🎉 Compte activé ! Utilise le menu pour les pronostics.",
        "error": "❌ Erreur, réessaie.",
        "banned": "❌ Banni.",
        "active": "✅ Déjà actif ! Utilise le menu.",
        "choose_lang": "🌍 Choisis ta langue :",
        "profile": "👤 *Profil*\n\nID : `{}`\nStatut : {}\nLangue : {}\nInscrit le : {}\nActivé le : {}",
        "history": "📜 *Historique des pronostics*\n\n{}",
        "no_history": "Aucun pronostic pour le moment.",
        "prediction_result": "🎯 *Pronostic {}*\n\n🏟️ {}\n📊 Confiance : {}%\n💰 Cote : {}\n\n📝 *Analyse :*\n{}",
        "admin_stats": "📊 *Statistiques du bot*\n\n👥 Total : {}\n⏳ En attente : {}\n✅ Actifs : {}\n❌ Bannis : {}"
    },
    "en": {
        "welcome": "🦁 *Welcome to LionWise Betting !*\n\nPromo code : `{}`\n\n1️⃣ Create 1xBet account\n2️⃣ Send your ID (e.g. 123456)\n3️⃣ Send a screenshot of your balance",
        "ask_id": "📝 Send your *1xBet ID* (numbers) :",
        "ask_photo": "📸 Send a screenshot of your balance.",
        "deposit_ok": "✅ Received! Waiting for validation.",
        "activate": "🎉 Activated! Use the menu for predictions.",
        "error": "❌ Error, try again.",
        "banned": "❌ Banned.",
        "active": "✅ Already active! Use the menu.",
        "choose_lang": "🌍 Choose your language :",
        "profile": "👤 *Profile*\n\nID : `{}`\nStatus : {}\nLanguage : {}\nRegistered : {}\nActivated : {}",
        "history": "📜 *Prediction history*\n\n{}",
        "no_history": "No predictions yet.",
        "prediction_result": "🎯 *Prediction {}*\n\n🏟️ {}\n📊 Confidence : {}%\n💰 Odds : {}\n\n📝 *Analysis :*\n{}",
        "admin_stats": "📊 *Bot statistics*\n\n👥 Total : {}\n⏳ Pending : {}\n✅ Active : {}\n❌ Banned : {}"
    },
    "ar": {
        "welcome": "🦁 *مرحبًا بك في LionWise Betting !*\n\nرمز العرض : `{}`\n\n1️⃣ أنشئ حساب 1xBet\n2️⃣ أرسل معرفك (مثال: 123456)\n3️⃣ أرسل لقطة شاشة من رصيدك",
        "ask_id": "📝 أرسل *معرف 1xBet* (الأرقام) :",
        "ask_photo": "📸 أرسل لقطة شاشة من رصيدك.",
        "deposit_ok": "✅ تم الاستلام! في انتظار التحقق.",
        "activate": "🎉 تم التفعيل! استخدم القائمة للتوقعات.",
        "error": "❌ خطأ، حاول مجددًا.",
        "banned": "❌ محظور.",
        "active": "✅ نشط بالفعل! استخدم القائمة.",
        "choose_lang": "🌍 اختر لغتك :",
        "profile": "👤 *الملف الشخصي*\n\nالمعرف : `{}`\nالحالة : {}\nاللغة : {}\nتاريخ التسجيل : {}\nتاريخ التفعيل : {}",
        "history": "📜 *سجل التوقعات*\n\n{}",
        "no_history": "لا توجد توقعات حتى الآن.",
        "prediction_result": "🎯 *توقع {}*\n\n🏟️ {}\n📊 الثقة : {}%\n💰 الاحتمالات : {}\n\n📝 *التحليل :*\n{}",
        "admin_stats": "📊 *إحصائيات البوت*\n\n👥 المجموع : {}\n⏳ في الانتظار : {}\n✅ نشط : {}\n❌ محظور : {}"
    }
}

def get_text(lang, key, *args):
    text = LOCALES.get(lang, LOCALES["fr"]).get(key, "")
    if not text:
        return ""
    try:
        return text.format(*args)
    except (IndexError, KeyError):
        return text
