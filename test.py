import requests


TOKEN = """6100275561:AAF4LDysmEXcBATHjJ5vaqxlFppQ8fxQWdc"""
URL = f"""https://api.telegram.org/bot{TOKEN}/"""

example5 = """Дневной:
Si_Money - сигналы форекс
Порядковый номер сигнала за сегодня - 9
Открыть позицию - BUY
Валютная пара - GBPUSD
Объем - 0,01
Цена открытия сделки - 1,2493
Тейк профит - 1,2513
Объем для депозита 10.000 USD"""

example = """Здравствуйте уважаемые подписчики. Сегодня сигналов еще не было. Ждем подходящих условий для открытия сделок."""

example3 = "Привет! Как дела?"

admins = [5754619101, 7166188300]


def send_message(chat_id, text, parse_mode="markdown"):
    url = URL + "sendMessage"
    req = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
    r = requests.post(url, json=req)
    return r.json()


send_message(admins[1], example)
