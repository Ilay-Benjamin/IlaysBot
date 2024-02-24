class Menu:
    def main_menu_keyboard():
        keyboard = [[InlineKeyboardButton('Menu 1', callback_data='m1')],
            [InlineKeyboardButton('Menu 2', callback_data='m2')],
            [InlineKeyboardButton('Menu 3', callback_data='m3')]]
        return InlineKeyboardMarkup(keyboard)
    
