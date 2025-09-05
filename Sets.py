import telebot

bot = telebot.TeleBot('8130341917:AAG_6q-29ow1EaW35ht2XPX-rs06nkQPbXk')

k="""лошадь домашняя
обыкновенная собака
обыкновенный кот
обыкновенный бобер
обыкновенный воробей
обыкновенная лисица
обыкновенный павлин
обыкновенная выдра
обыкновенная игуана
сиамская кобра
сивуч
сине-желтый ара
сливолобый попугай
соболь
сойка
соня-полчок
сорока
степной сурок
сурикат
тайпан
фенек
филин
ходулочник
черный гриф
черный кайман
черный лебедь
щилоклювка
щетинистый броненосец
щетинистый кенгуру""".split('\n')
# print(0%2==0)

quiz = [
    {
        'question': 'Вопрос 1: Вы любите спать?',
        'options': [('Не могу жить без 10 часов сна', 1), ('7-8 часов опционально', 2), 
                    ('Спать ? 6 часов на весь день с запасом', 3)]
    },
    {
        'question': 'Вопрос 2: Вы любиту покушать?',
        'options': [('Постоянно ем, не могу остановиться', 1), 
                    ('Работа, дела, не успеваю нормально поесть', 2), 
                    ('Обычный рацион', 3)]
    },
    {
        'question': 'Вопрос 3: Вы любите активный вид деятельности?',
        'options': [('Активный? я лучше посижу на диване', 1), ('Сидеть на месте? - Нет', 2), 
                    ('И спокойный и активный', 3)]
    },
    {
        'question': 'Вопрос 4: Какой климат вам ближе всего?',
        'options': [('Умеренный', 1), ('Экваториальный', 2), ('Полярный', 3)]
    },
]

anis= {'7':'photo/Coala.webp', #Коала
       '9': 'photo/Olen.webp', #Олень
       '8': 'photo/Gepard.webp', #Гепард
      '10':'photo/Dolfin.jpg', #Дельфин
      '5':'photo/Lisa.webp', #Лиса
      '11':'photo/WhiteBear.webp', #Белый медведь
      '4':'photo/Bear.webp',
        '6':'photo/Coala.webp',
         '12':'photo/WhiteBear.webp' #Бурый медведь
        }




# mark=types.InlineKeyboardMarkup()
#     k1=types.InlineKeyboardButton('Список животных',)
#     k2=types.InlineKeyboardButton('Поддержка',)
#     k3=types.InlineKeyboardButton('Программа опека')
#     # k4=types.InlineKeyboardButton('Назад', callback_data='back')
#     k5=types.InlineKeyboardButton('Тест ваше тотемное животное')
#     # k6=types.InlineKeyboardButton('Купить билеты',url='https://moscowzoo.ru/visitors/tickets')
#     # k7=types.InlineKeyboardButton('Подробная информация программы опека', url='https://moscowzoo.ru/about/guardianship')
#     k8=types.InlineKeyboardButton('Сайт',url='https://moscowzoo.ru/')
#     # k9=types.InlineKeyboardButton('Стать опекуном',callvback_data='st_opeka')
#     # k10=types.InlineKeyboardButton('Мои результаты', callback_data='bases')
#     # k11=types.InlineKeyboardButton('Перепройти', callback_data='again')
#     # k12=types.InlineKeyboardButton('Поделиться результом', callback_data='share')
#     # k13=types.InlineKeyboardButton('Начать тест', callback_data='Stariy')
#       k14=types.InlineKeyboardButton("Поделиться в Twitter", url=twitter_url)
#       k15=types.InlineKeyboardButton("Поделиться в VK", url=vk_url)













































# 1


# 11
# 1
