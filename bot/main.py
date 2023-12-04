import os
from pyrogram import Client, filters

# Токен Бота
bot_token = os.getenv('BOT_TOKEN')

# Клиент
client = Client(
    name='Bot_AdminGroup', 
    bot_token=bot_token
)

@client.on_message(filters.group, group=1)
def forward_messages(client, message):
    text = f"""Сообщение из {message.chat.title} от @{message.from_user.username}
{message.text}"""
    client.send_message(5974014808, text)
 
client.run()