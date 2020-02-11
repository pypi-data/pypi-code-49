try:
    import telebot as __telebot
    from telebot import types
    import time as __time
    import hackingtools as ht
    import ast as __ast
    
    __bot_name__ = ht.core.Config.getConfig(parentKey='core', key='TelegramBot', subkey='bot-name')
    __bot_token__ = ht.core.Config.getConfig(parentKey='core', key='TelegramBot', subkey='bot-token')
    bot = None

    __crossIcon__ = u"\u274C"

    try:
        bot = __telebot.TeleBot(__bot_token__)
    except:
        pass

    @bot.message_handler(commands=['start'])
    def handle_command_adminwindow(message):
        stringList = {}
        for module in ht.getModulesNames():
            stringList[module] = ht.getModuleCategory(module)

        markup = types.InlineKeyboardMarkup()

        for key, value in stringList.items():
            markup.add(types.InlineKeyboardButton(text=key, callback_data="['value', '" + key + "', '" + value + "']"))

        bot.send_message(chat_id=message.chat.id, text="Here you have the modules:", reply_markup=markup)
        
    @bot.callback_query_handler(lambda q: q.message.chat.type == "private")
    def private_query(query):
        if (query.data.startswith("['value'")):
            valueFromCallBack = __ast.literal_eval(query.data)[1]
            keyFromCallBack = __ast.literal_eval(query.data)[2]
            bot.answer_callback_query(callback_query_id=query.id, show_alert=True, text="You Clicked " + valueFromCallBack + " module and it's category is " + keyFromCallBack)
            
        bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id)

    bot.polling()
except:
    try:
        bot.stop_polling()
    except:
        pass