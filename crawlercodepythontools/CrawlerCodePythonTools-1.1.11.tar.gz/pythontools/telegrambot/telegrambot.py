from pythontools.core import logger
import telegram
from telegram.ext import CommandHandler, Updater, Filters, MessageHandler


class TelegramBot:

    def __init__(self, token):
        self.bot = telegram.Bot(token=token)
        self.updater = Updater(token=token, use_context=True)
        self.trustedUserIDs = []
        self.trustedUserUsernames = []
        self.trustedGroupTitles = []
        self.trustedGroupIDs = []

    def start(self):
        self.updater.start_polling()
        logger.log("§8[§eBOT§8] §aBot started")

    def trustUserByUsername(self, username):
        self.trustedUserUsernames.append(username)

    def trustUserByID(self, id):
        self.trustedUserIDs.append(str(id))

    def trustGroupByTitle(self, title):
        self.trustedGroupTitles.append(title)

    def trustGroupByID(self, id):
        self.trustedGroupIDs.append(str(id))

    def sendMessage(self, chat_id, text):
        self.bot.send_message(chat_id, text, parse_mode=telegram.ParseMode.MARKDOWN)

    def sendPhoto(self, chat_id, photo):
        self.bot.send_photo(chat_id, photo=photo)

    def registerCommand(self, trigger, method):
        def meth(update, context):
            if (update.message.chat["type"] == "private" and (
                    str(update.message.chat["id"]) in self.trustedUserIDs or str(
                    update.message.chat["username"]) in self.trustedUserUsernames)) or (
                    update.message.chat["type"] == "supergroup" and (
                    str(update.message.chat["id"]) in self.trustedGroupIDs or str(
                    update.message.chat["title"]) in self.trustedGroupTitles)):
                method(Command(update, context))
            else:
                context.bot.send_message(chat_id=update.message.chat["id"], text="Sorry, no permission!")

        self.updater.dispatcher.add_handler(CommandHandler(trigger, meth))
        logger.log("§8[§eBOT§8] §rCommand '" + trigger + "' registered")

    def registerMessageHandler(self, method):
        def meth(update, context):
            if (update.message.chat["type"] == "private" and (
                    str(update.message.chat["id"]) in self.trustedUserIDs or str(
                    update.message.chat["username"]) in self.trustedUserUsernames)) or (
                    update.message.chat["type"] == "supergroup" and (
                    str(update.message.chat["id"]) in self.trustedGroupIDs or str(
                    update.message.chat["title"]) in self.trustedGroupTitles)):
                method(Message(update, context))
            else:
                context.bot.send_message(chat_id=update.message.chat["id"], text="Sorry, no permission!")

        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, meth))
        logger.log("§8[§eBOT§8] §rMessage handler registered")

    def getInfo(self):
        return self.bot.get_me()


class Message:

    def __init__(self, update, context):
        self.update = update
        self.context = context
        self.chat_id = update.message.chat["id"]
        self.text = update.message["text"]

    def reply(self, text):
        self.context.bot.send_message(chat_id=self.chat_id, text=text)


class Command:

    def __init__(self, update, context):
        self.update = update
        self.context = context
        self.chat_id = update.message.chat["id"]

    def reply(self, text):
        self.context.bot.send_message(chat_id=self.chat_id, text=text)