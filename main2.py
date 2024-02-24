import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    ConversationHandler,
)


async def creator (update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = 'מפתח הבוט הוא איליי בנימין, ניתן ליצור קשר בכתובת המייל - ilaybenjamin1@gmail.com'
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=text
    )


async def help1 (update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    help_details = {
        'help': 'מראה את רשימת הפקודות הקיימות',
        'start': 'מאתחל את הבוט',
        'echo': 'מחזיר את ההודעה שהתקבלה',
        'creator': 'מראה את פרטי המפתח של הבוט'
    }
    text = 'הנה רשימת הפקודות הקיימות:\n'
    for command, description in help_details.items():
        text += f'/{command} - {description}\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def echo (update: Update, context: ContextTypes.DEFAULT_TYPE):
    userMessage = update.message.text
    user = update.message.from_user
    first_name = update.message.chat.first_name
    await context.bot.send_message(chat_id=update.effective_chat.id, text='היי ' + first_name)


async def start (update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    first_name = update.message.chat.first_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text='נעים מאוד ' + first_name + ' אני רובוט שמסייע בקבלת תורים למרפאה, איך אני יכול לעזור לך? \n ניתן להקליד /help על מנת לקבל את רשימת הפקודות'
    )
    
    
def main ():
    application = (
        ApplicationBuilder()
        .token("7021552355:AAG_3dfOmXMdpYvMoHPhk4cVB1NARMF0T2k")
        .build()
    )

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    start_handler = CommandHandler("start", start)
    help_hendler = CommandHandler("help", help1)
    creator_handler = CommandHandler("creator", creator)    

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(help_hendler)
    application.add_handler(creator_handler)

    application.run_polling()


if __name__ == "__main__":
    main()