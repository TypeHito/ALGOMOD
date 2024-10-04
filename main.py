from pyrogram import Client
import lang
from methods import translate, remove_urls
import const


# app = Client("MMSignal")
app = Client(const.APP_NAME, const.API_ID, const.API_HASH)  #me


@app.on_message()
async def message_handler(client, messsage):
    """
        Проверяет, является ли поступаюшай сообщения из указанных в  valid_chats.
        Args:
          client:  json обект бота.
          messsage: json обект сообщения.
        если valid_chats то отправляет тект сообшения в указанный  channel
    """
    try:
        if messsage.chat.id in const.VALID_CHATS:
            text = [await translate(messsage.text, i) for i in lang.langs]
            if remove_urls(text):
                return
            await app.send_message(const.UZ_ALTER_CHANNEL, text[0] + lang.end_uz_alter)
            await app.send_message(const.UZ_CHANNEL, text[0] + lang.end_uz)
            await app.send_message(const.RU_CHANNEL, text[1] + lang.end_ru)
            await app.send_message(const.EN_CHANNEL, text[2] + lang.end_en)
    except Exception as err:
        print(err)
        await app.send_message(const.ADMINS[0], "MMSignal: " + str(err))
    # print(messsage.chat.id)


print("ALGO SIGNAL MM BOT HAS BEEN STARTED!")
app.run()

