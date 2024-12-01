from pyrogram import Client
import lang
from methods import translate, remove_urls, get_gold
import const
from pyrogram import Client, filters

bot_status = True
# app = Client("MMSignal")
app = Client(const.APP_NAME, const.API_ID, const.API_HASH)  #me


@app.on_message(filters.private & filters.text)
# @app.on_message()
async def message_handler(client, messsage):
    global bot_status
    # print(messsage.chat.id)
    """
        Проверяет, является ли поступаюшай сообщения из указанных в  valid_chats.
        Args:
          client:  json обект бота.
          messsage: json обект сообщения.
        если valid_chats то отправляет тект сообшения в указанный  channel
    """

    if messsage.chat.id in const.ADMINS:

        if messsage.text == "start":
            bot_status = True
            await messsage.reply_text(f"Bot status ID: {bot_status}")
            return
        elif messsage.text == "stop":
            bot_status = False
            await messsage.reply_text(f"Bot status ID: {bot_status}")
            return

    if bot_status:
        try:
            if messsage.chat.id in const.VALID_CHATS:
                if remove_urls(messsage.text):
                    return await app.send_message(const.ADMINS[0], messsage.text)
                text = [await translate(messsage.text, i) for i in lang.langs]

                await app.send_message(const.UZ_ALTER_CHANNEL, text[0] + lang.end_uz_alter)
                await app.send_message(const.UZ_CHANNEL, text[0] + lang.end_uz)
                await app.send_message(const.RU_CHANNEL, text[1] + lang.end_ru)
                await app.send_message(const.EN_CHANNEL, text[2] + lang.end_en)


                if get_gold(messsage.text):
                    try:
                        await app.send_message(const.GOLD_CHANNEL, text[0][29:])
                        await app.send_message(const.FAKE_GOLD_CHANNEL, lang.fake_new)
                    except Exception as err:
                        await app.send_message(const.GOLD_CHANNEL, text[0])
                        await app.send_message(const.FAKE_GOLD_CHANNEL, text[0])

                # await app.send_message(messsage.chat.id, text[1] + lang.end_en)
        except Exception as err:
            print(err)
            await app.send_message(const.ADMINS[0], "MMSignal: " + str(err))


print("ALGO SIGNAL MM BOT HAS BEEN STARTED!")
app.run()
