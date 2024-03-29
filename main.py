import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode
import datetime
import json
from datetime import datetime
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
    first_name = user.first_name
    last_name = user.last_name

    with open('messages.txt', 'a', encoding='utf-8') as file:
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        file.write('[' + current_date + ' - ' + current_time + '] ' + first_name + ' sent: ' + userMessage + '\n')
    if first_name == '✿ Benny ॐ۞':
        await context.bot.send_message(chat_id=update.effective_chat.id, text='אני לא רוצה לדבר איתך')
    elif first_name == 'איליי':
        await context.bot.send_message(chat_id=update.effective_chat.id, text='אוהב אותך אחי')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='ההודעה שלך הועברה למנהל המערכת')
    


async def start(update: Update, context):
    user = update.message.from_user
    first_name = user.first_name
    last_name = user.last_name
    
    # Prepare the data to be logged
    object_data = {
        'user': {
            'first_name': first_name,
            'last_name': last_name,
            'id': user.id,
        },
        'time': str(datetime.now()),
        'status': 'connected'
    }
    
    # Write the data to info.json
    with open('info.json', 'r+', encoding='utf-8') as file:
        # Read the existing JSON data
        json_data = json.load(file)
        # Append the new data to the connections list
        json_data['connections'].append(object_data)
        # Move the file pointer to the beginning of the file
        file.seek(0)
        # Write the updated JSON data back to the file
        json.dump(json_data, file, indent=4, ensure_ascii=False)

    with open('logs.txt', 'a', encoding='utf-8') as file:
        file.write('User ' + first_name + ' connected at ' + str(datetime.now()) + '\n')
        
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