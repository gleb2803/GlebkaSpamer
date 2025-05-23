import keyboard
import time
import random

texts = [
         "@everyone Правил нет",
         "@everyone Мирон Лох",
         "@everyone ЛОЛ",
         "@everyone Юпитер",
         "@everyone Сатурн",
         "@everyone Chin hen honci",
         "@everyone Школа пока",
         "@everyone Биба и Боба",
         "@everyone ЫЫЫЫЫЫЫЫЫЫЫЫ",
         "@everyone Я РУСКИЙЙЙЙЙЙЙЙЙЙЙ",
         "@everyone Хлеб",

]
start_texts = [
    "Загрузка...",
    "Загрузка завершена",
    "Запуск...",
    "Запуск завершён",
    "Запуск Активации...",
    "Активация запущена :)"
]
end_texts = [
    "Получена команда 'Стоп'",
    "Остановка всех процесов",
    "Остановка завершена",
    "Всем удачного дня",
    "-Glebka spamer stoper"
]

wait_time = random.randint(60,180)

times = 0

while True:
    keyboard.wait("page up")
    for text in start_texts:
        keyboard.write(text)
        keyboard.press("ctrl")
        keyboard.press("enter")
        keyboard.release("ctrl")
        keyboard.release("enter")
        time.sleep(5)
        
    while not keyboard.is_pressed("page down"):
        if wait_time == times:
            wait_time = random.randint(60, 180)
            times = 0
            keyboard.write(random.choice(texts) + " :)")
            keyboard.press("ctrl")
            keyboard.press("enter")
            keyboard.release("ctrl")
            keyboard.release("enter")
        time.sleep(1)
        times += 1
    for text in end_texts:
        keyboard.write(text)
        keyboard.press("ctrl")
        keyboard.press("enter")
        keyboard.release("ctrl")
        keyboard.release("enter")
        time.sleep(1)