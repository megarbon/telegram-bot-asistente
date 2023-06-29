import telebot
import csv
from saludos import saludar_nuevos_miembros

TOKEN = '6370610370:AAGxv0O6c1p0Jf3jhmgYALsZESx_66nEWxc'

bot = telebot.TeleBot(TOKEN)



#respuesta al mensaje /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, '¡Hola! Soy Jake el asistente de clase. ¿En qué puedo ayudarte?')


#respuesta al mensaje /horario
@bot.message_handler(commands=['horario'])
def horario(message):
    # Implementa la lógica para obtener el horario de clases
    horario_clases = obtener_horario()
    bot.reply_to(message, horario_clases)


#respuesta al mensaje /entregas
@bot.message_handler(commands=['entregas'])
def entregas(message):
    # Implementa la lógica para obtener las entregas pendientes
    entregas_pendientes = obtener_entregas_pendientes()
    bot.reply_to(message, entregas_pendientes)

#despedida
@bot.message_handler(func=lambda message: True)
def mensaje_texto(message):
    mensaje = message.text
    if mensaje.lower() == "hola":
        bot.reply_to(message, "¡Hola! ¿no deberías estar estudiando en vez de hablar conmigo?")
    elif mensaje.lower() == "adios":
        bot.reply_to(message, "¡Hasta luego mákina!")



@bot.message_handler(func=lambda message: message.new_chat_members is not None)
def handle_new_members(message):
    saludar_nuevos_miembros(bot, message)

bot.polling()
