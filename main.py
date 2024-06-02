from pyrogram import Client
from methods import translate
from lang import start, end
import const


# app = Client("MMSignal")
app = Client(const.APP_NAME, const.API_ID, const.API_HASH)  #me


@app.on_message()
def message_handler(client, messsage):
    """
        Проверяет, является ли поступаюшай сообщения из указанных в  valid_chats.
        Args:
          client:  json обект бота.
          messsage: json обект сообщения.
        если valid_chats то отправляет тект сообшения в указанный  channel
    """
    try:
        if messsage.chat.id in const.VALID_CHATS:
            text = translate(messsage.text)
            msg = start + text + end
            for channel in const.VALID_CHANNELS:
                app.send_message(channel, msg)
            # app.send_message(admins[1], msg)
    except Exception as err:
        print(err)
        app.send_message(const.ADMINS[0], "MMSignal: " + str(err))


print("ALGO SIGNAL MM BOT HAS BEEN STARTED!")
app.run()

