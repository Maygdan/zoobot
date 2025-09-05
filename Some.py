from Sets import bot,k,quiz,anis
from ruls import Test,user_data,resultat,who_i,a
from telebot import types
import urllib.parse




@bot.message_handler(commands=['start'])
def st(ms):

    text1=text1='Добро пожаловать посетитель. \n Мы можем предложить вам пройти тест, \
чтобы узнать ваше тотемное  \
животное, а также рассказать о программе опека. \n Если подобная \
информация вас заинтересовала нажмите на одну из кнопак ниже'

    mark=types.InlineKeyboardMarkup(row_width=2)
    k1=types.InlineKeyboardButton('Список животных',callback_data='list')
    k2=types.InlineKeyboardButton('Поддержка',callback_data='help')
    k3=types.InlineKeyboardButton('Программа опека',callback_data='opeka')
    k5=types.InlineKeyboardButton('Тест ваше тотемное животное',callback_data='game')
    k8=types.InlineKeyboardButton('Сайт',url='https://moscowzoo.ru/')

    mark.row(k3,k8,).row(k1,k2).add(k5)
    
    bot.send_message(ms.chat.id,text1,reply_markup=mark)

    

@bot.message_handler(commands=['test'])
def games(ms):

    mark=types.InlineKeyboardMarkup()
    k4=types.InlineKeyboardButton('Назад', callback_data='back')
    k10=types.InlineKeyboardButton('Мои результаты', callback_data='bases')
    k13=types.InlineKeyboardButton('Начать тест', callback_data='Stariy')

    mark.row(k13,k10)
    mark.add(k4)

    bot.send_message(ms.chat.id, 'Давайте начнём тест:  Ваше тотемное животное ',reply_markup=mark)



@bot.message_handler(commands=['help'])
def hp(ms):

    text2='В данном боте присутствует только 1 языка --Русский \n Для корректной работы бота просим вводить \
данные только используя буквы кириллицы,цифры и числа. Важно, если вы решите перепройти тест  \
то ваш результат будет удалён,т.к вы решили его изменить, перепройдя, а не сохранив. Версия 1.0.\n \
Если нашли ошибку в работе бота, есть дополнительные вопросы просим написать на почту alesharet4253@gmail.com \
подробно описав авшу проблему или звоните по номеру +7(964)515-24-53'

    mark=types.InlineKeyboardMarkup()
    k4=types.InlineKeyboardButton('Назад', callback_data='back')
    k8=types.InlineKeyboardButton('Сайт зоопарка',url='https://moscowzoo.ru/')

    mark.row(k4,k8)

    bot.send_message(ms.chat.id,text2,reply_markup=mark)



@bot.message_handler(commands=['animals'])
def ls(ms):
    j='\n'.join(k)


    mark=types.InlineKeyboardMarkup()
    k4=types.InlineKeyboardButton('Назад', callback_data='back')
    k9=types.InlineKeyboardButton('Стать опекуном',callback_data='st_opeka')

    mark.row(k9,k4)

    bot.send_message(ms.chat.id,f'Доступный список обитателей зоопарка:\n {j}',reply_markup=mark)



@bot.message_handler(commands=['opeka'])
def op(ms):

    text3='Опека представляет собой \
одну из программ, помогающих зоопарку заботиться о его обитателях. \
Программа позволяет с помощью пожертвования на любую сумму внести свой \
вклад в развитие зоопарка и сохранение биоразнообразия планеты.\
Взять под опеку можно разных обитателей зоопарка.\
Участником программы может стать любой неравнодушный: и ребёнок, \
и большая корпорация.     Поддержка опекунов помогает зоопарку улучшать\n\
условия для животных и повышать уровень их благополучия.\n Почётный статус опекуна \
позволяет круглый год навещать, быть в курсе событий его жизни и самочувствия.'

    mark=types.InlineKeyboardMarkup()
    k4=types.InlineKeyboardButton('Назад', callback_data='back')
    k9=types.InlineKeyboardButton('Стать опекуном',callback_data='st_opeka')
    k1=types.InlineKeyboardButton('Список животных', callback_data='list')
    k7=types.InlineKeyboardButton('Подробная информация o программe опека', \
                            url='https://moscowzoo.ru/about/guardianship')
    k8=types.InlineKeyboardButton('Сайт зоопарка',url='https://moscowzoo.ru/')

    mark.row(k1,k9)
    mark.add(k7).row(k8,k4)

    bot.send_message(ms.chat.id,text3,reply_markup=mark)



@bot.message_handler(commands=['st_opeka'])
def st_opeka(ms):
        
        text3='Чтобы стать опекуном, укажите животное из списка, а далее внесите ваше пожертвование в фонд зоопарка \
форма заполнения выглядит так: \n <Ваше животное> <сумма пожетвования в рублях>'

        mark=types.InlineKeyboardMarkup()
        k4=types.InlineKeyboardButton('Назад', callback_data='back')

        mark.add(k4)

        bot.send_message(ms.chat.id,text3,reply_markup=mark)



@bot.message_handler(commands=['share'])
def share(ms):

    # set(resultat)
    if resultat:
        BOT_LINK='https://t.me/TEER_GANGIRSEbot'
        result_text='Угадайте, кто я?'
        share_text = f"{result_text}\n\nПопробуйте и вы: {BOT_LINK}"
        twitter_url = f"https://twitter.com/intent/tweet?text=" + urllib.parse.quote(share_text) 
        vk_url = f"https://vk.com/share.php?url={BOT_LINK}&title="+ urllib.parse.quote(share_text) # type: ignore
        wa_link = "https://wa.me/?text=" + urllib.parse.quote(share_text)
    
        mark = types.InlineKeyboardMarkup()
        k16=types.InlineKeyboardButton("Ватсапп", url=wa_link)
        k14=types.InlineKeyboardButton("Twitter", url=twitter_url)
        k15=types.InlineKeyboardButton("VK", url=vk_url)
        k4=types.InlineKeyboardButton('Назад', callback_data='back')

        mark.row(k16,k15)
        mark.row(k14,k4)
    
        bot.send_message(ms.chat.id, share_text, reply_markup=mark)
    else:
        bot.send_message(ms.chat.id,'Вы ещё не прошли тест 😇')



@bot.message_handler(commands=['Stariy'])
def start_quiz(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'current_q': 0, 'score': 0}
    send_question(chat_id)



@bot.message_handler(func=lambda message: message.chat.id in user_data)
def handle_answer(message):
    chat_id = message.chat.id
    current = user_data[chat_id]['current_q']
    q = quiz[current]

    selected_text = message.text
    for option_text, points in q['options']:
        if option_text == selected_text:
            user_data[chat_id]['score'] += points
            break
    else:

        bot.send_message(chat_id, 'Пожалуйста, выберите вариант из клавиатуры.')
        return

    user_data[chat_id]['current_q'] += 1
    send_question(chat_id)

    

def send_question(chat_id):
    current = user_data[chat_id]['current_q']
    if current < len(quiz):
        q = quiz[current]
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for option_text, _ in q['options']:
            markup.add(option_text)
        bot.send_message(chat_id, q['question'], reply_markup=markup)
    else:
        mark=types.InlineKeyboardMarkup()
        k4=types.InlineKeyboardButton('Вернуться в меню', callback_data='back')
        k10=types.InlineKeyboardButton('Мои результаты', callback_data='bases')
        k11=types.InlineKeyboardButton('Перепройти', callback_data='again')
        k12=types.InlineKeyboardButton('Поделиться результом', callback_data='share')

        mark.add(k4)
        mark.row(k10,k11)
        mark.add(k12)

        score = user_data[chat_id]['score']
        resultat.append(user_data[chat_id])
        with open(f'{anis.get(str(score))}','rb') as phot: 
            # print(anis.get(str(score)))
            result=who_i(score)
            bot.send_photo(chat_id,phot, result, reply_markup=mark)
            resultat.append(phot)
            # print(resultat)

@bot.message_handler(commands=['resultats'])
def bs(ms):
    # set(resultat)
    mark=types.InlineKeyboardMarkup()
    k4=types.InlineKeyboardButton('Вернуться в меню', callback_data='back')
    mark.add(k4)
    if resultat:
        b=len(resultat)//2
        if b<3: 
            r=[who_i(resultat[j].get('score')).split('.')[0][4:] for j in range(b+1) if j%2==0] # type: ignore
            ra='\n'.join([i for i in list(map(str,r))])
            
        else:
            r=[who_i(resultat[j].get('score')).split('.')[0][4:] for j in range(b+3) if j%2==0] # type: ignore
            ra='\n'.join([i for i in list(map(str,r))])
        bot.send_message(ms.chat.id,f'Ваши результаты :\n {ra}',reply_markup=mark) 
    else:
        bot.send_message(ms.chat.id,'Вы ещё не прошли ни одного теста',reply_markup=mark)
    
        
        

       

@bot.callback_query_handler(func=lambda call:call.data=='help')

def hp_callback(call):
            bot.delete_message(call.message.chat.id,call.message.message_id -0)
            hp(call.message)



@bot.callback_query_handler(func=lambda call:call.data=='list')
def ls_callback(call):
            bot.delete_message(call.message.chat.id,call.message.message_id -0)
            ls(call.message)



@bot.callback_query_handler(func=lambda call:call.data=='opeka')
def op_callback(call):
            bot.delete_message(call.message.chat.id,call.message.message_id -0)
            op(call.message)



@bot.callback_query_handler(func=lambda call:call.data=='game')
def game_callback(call):
            bot.delete_message(call.message.chat.id,call.message.message_id -0)
            games(call.message)



@bot.callback_query_handler(func=lambda call:call.data=='back')
def back_callback(call):
            bot.delete_message(call.message.chat.id, call.message.message_id-0)
            st(call.message)
            
            
@bot.callback_query_handler(func=lambda call:call.data=='st_opeka')
def st_opeka_callback(call):
            bot.delete_message(call.message.chat.id,call.message.message_id -0)
            st_opeka(call.message)


@bot.callback_query_handler(func=lambda call:call.data=='share')
def share_callback(call):
            
            bot.delete_message(call.message.chat.id,call.message.message_id)
            share(call.message)


@bot.callback_query_handler(func=lambda call:call.data in ['Stariy','again'])
def test_callback(call):
            bot.delete_message(call.message.chat.id,call.message.message_id -0)
            start_quiz(call.message)


@bot.callback_query_handler(func=lambda call:call.data=='bases')

def bases_callback(call):
            bot.delete_message(call.message.chat.id,call.message.message_id -0)
            bs(call.message)

@bot.message_handler(content_types=['text'])
def rn_op(ms):
        a=ms
        val=ms.text.lower()
        Test.check(val,a)


 
bot.polling()
