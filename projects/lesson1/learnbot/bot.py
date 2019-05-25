from telegram.ext import Updater, CommandHandler
PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
def greet_user(bot,update):
    text = 'Buenos dias, patron'
    print(text)
    update.message.reply_text(text)
def main():
    mybot = Updater('894555361:AAEibA26NX97OPoCTd6cBuZOkSwUdpYFwLY',request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    mybot.idle()
main()