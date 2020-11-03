import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#enable logging
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)

logger = logging.getLogger(__name__)



TOKEN = "1481614465:AAH0-5r47ogHyI1aUFwTJT_tK9CmhAIs7_E"
def start(bot ,update):
    print(update)
    author = update.message.from_user.first_name
    reply = "Hi! {}".format(author)
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def _help(bot,update):
    help_text = "hey! This is a help text."
    bot.send_message(chat_id=update.message.chat_id,text=help_txt)

def echo_text(bot,update):
    reply = update.message.text
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def echo_sticker(bot,update):
    bot.send_sticker(chat_id=update.message.chat.id, 
    sticker = update.message.sticker.File_id)

def error(bot,update):
    logger.error("Update 's' caused error '%s'",Update,Update.error)

def main():
    updater = Updater(TOKEN)


    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)

    
    updater.start_polling()
    logger.info("started polling.....")
    updater.idle()


if __name__ == "__main__":
    main()
