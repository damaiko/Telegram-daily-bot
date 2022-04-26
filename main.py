import telebot
import requests



API_KEY = "5313312563:AAG3Umcq2r1hkiccPdZeBmbm1Ftysz-cTDc"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['news'])
def news(message):
  response = requests.get("https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=ABvvPrqHVstgaFv2EglNvxzQm9WXXPzX").json()
  #results_len = response['num_results']
  #for result in range(results_len):
  bot.send_message(message.chat.id, response['results'][1]['url'])
  



bot.polling()