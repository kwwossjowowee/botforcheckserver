import telebot as tb
bot = tb.TeleBot("")

@bot.message_handler(commands=["echo"])
def echo(message):
  echo_text = ' '.join(message.text.split()[1:])
  return bot.reply_to(message, f"echo: {echo_text}")
  
while True:
  bot.polling(none_stop=True)
