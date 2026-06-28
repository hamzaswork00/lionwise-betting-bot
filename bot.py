import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, filters
from config import BOT_TOKEN
from handlers.start import start, lang_callback, ask_id, ASK_ID, ASK_PHOTO
from handlers.deposit import handle_deposit_photo
from handlers.prediction import handle_match_photo
from handlers.menu import main_menu_callback
from handlers.admin import admin_callback, admin_commands

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_id)],
            ASK_PHOTO: [MessageHandler(filters.PHOTO, handle_deposit_photo)],
        },
        fallbacks=[CommandHandler("start", start)]
    )
    app.add_handler(conv_handler)

    app.add_handler(CallbackQueryHandler(lang_callback, pattern="^lang_"))
    app.add_handler(CallbackQueryHandler(main_menu_callback, pattern="^(main_menu|predict|profile|history|about|admin)$"))
    app.add_handler(CallbackQueryHandler(admin_callback, pattern="^(validate|reject)_"))
    app.add_handler(CommandHandler("stats", admin_commands))
    app.add_handler(MessageHandler(filters.PHOTO, handle_match_photo))

    logger.info("🤖 LionWise Betting Bot démarré avec Groq AI !")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
