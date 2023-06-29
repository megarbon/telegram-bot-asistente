import telebot

def saludar_nuevos_miembros(bot, message):
    for member in message.new_chat_members:
        bot.send_message(message.chat.id, f"¡Bienvenido/a {member.first_name} al grupo de clase!")
