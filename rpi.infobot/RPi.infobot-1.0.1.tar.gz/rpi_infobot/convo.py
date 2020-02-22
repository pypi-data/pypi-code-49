import logging
import netifaces as ni
from telegram import (
    Bot,
    Update,
    ParseMode
)
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext
)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def hello(cfg):
    bot = Bot(cfg.token)
    me = bot.get_me()
    for c in cfg.chats:
        logger.info("Sending hello to {c}".format(c=c))
        bot.send_message(c, f"{me.full_name} is online 🎉")

def goodbye(cfg, sig, frame):
    bot = Bot(cfg.token)
    me = bot.get_me()
    for c in cfg.chats:
        logger.info("Sending goodbye to {c}".format(c=c))
        bot.send_message(c, f"{me.full_name} is offline 😴 (SIG={sig})")

def chatinfo(update: Update, context: CallbackContext):
    msg = f"User: {update.effective_user.full_name} is in chat: {update.message.chat_id}"
    logger.info(msg)
    update.message.reply_text(msg)

def showip(update: Update, context: CallbackContext):
    ifaces = ni.interfaces()
    lines = []
    for i in ifaces:
        iface = ni.ifaddresses(i)
        mac = iface[ni.AF_LINK][0]['addr']
        ipv4 = 'NONE'
        inet = iface.get(ni.AF_INET) # ni.AF_INET6 is IPv6
        if inet is not None and len(inet) > 0:
            ipv4 = inet[0]['addr']

        lines.append(f"`{i}` has MAC: *{mac}* and IPv4: *{ipv4}*")

    output = "\n".join(lines)
    logger.info(output)
    update.message.reply_text(output, parse_mode=ParseMode.MARKDOWN)

def start(cfg):
    hello(cfg)

    updater = Updater(cfg.token, use_context=True, user_sig_handler=lambda sig,frame: goodbye(cfg, sig, frame))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('chatinfo', chatinfo)
    )

    dispatcher.add_handler(
        CommandHandler('showip', showip)
    )

    updater.start_polling()
    updater.idle()

