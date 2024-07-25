import telebot as tb
bot = tb.TeleBot("7017864172:AAEjHeeAkyqq4Hbf_IIKayULDqhI6aIly20")

@bot.message_handler(commands=["echo"])
def echo(message):
  echo_text = ' '.join(message.text.split()[1:])
  return bot.reply_to(message, f"echo: {echo_text}")
  
while True:
  bot.polling(none_stop=True)
