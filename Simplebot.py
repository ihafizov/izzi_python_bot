import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
	level=logging.INFO,
	filename='bot.log'
	)

def start_bot(update: Updater, CallbackContext):
	mytext = """Привет, {}!
Я пока не очень умный бот и знаю только команду /start. Можешь нажать еще раз :)""".format(update.message.chat.first_name)
	logging.info("{} started a bot".format(update.message.chat.first_name))
	update.message.reply_text(mytext)
	print("{} взаимодействует с ботом".format(update.message.chat.first_name))

def chat(update: Updater, CallbackContext):
	text = "Создатель еще не научил меня понимать слова. Я понимаю только команды, и то пока что одну: /start"
	logging.info("{} wrote to bot".format(update.message.chat.first_name))

	update.message.reply_text(text)

def main():
	updtr = Updater(settings.TOKEN_TELEGRAM)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	logging.info('Bot started')
	main()