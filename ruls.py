from Sets import bot,k,quiz
from telebot import types



class ZooExp(Exception):
    pass

class Test:
    @ staticmethod
    def check(ms,a):
        val = ms.split(' ')

        if len(val)==2 and val[0] in k :

            try:

                if float(val[1])>0:
                    bot.send_message(a.chat.id,f'Вы стали опекуном животного: {val[0]}, спасибо за ваш вклад')

                else:

                    try:
                        raise ZooExp
                    
                    except ZooExp:
                        bot.send_message(a.chat.id,'Неправильный ввод данных')
                
            except ZooExp:
                bot.send_message(a.chat.id,'Сумма пожертвования должна быть натуральным числом')

        elif len(val)==3 and val[0]+' '+val[1] in k:

            try:

                if float(val[2])>0:
                    bot.send_message(a.chat.id,f'Вы стали опекуном животного: {val[0]} {val[1]}, спасибо за ваш вклад')

                else:

                    try:
                        raise ZooExp
                    
                    except ZooExp:
                        bot.send_message(a.chat.id,'Неправильный ввод данных')

            except ZooExp:
                bot.send_message(a.chat.id,'Сумма пожертвования должна быть натуральным числом')

        else:
            bot.send_message(a.chat.id,'Неправильный ввод параметров, попробуйте ещё раз:')

user_data = {}

resultat=[]
a=[]

def who_i(score):

    if score ==4:
        return 'Вы — бурый медведь. Вы спокойны и уверены, любите размеренный образ жизни и \
комфорт.'
    if score==5:
        return 'Вы — лиса. Вы сообразительны, любите находить нестандартные решения и быстро \
адаптируетесь к изменениям. '
    if score in [6,7]:
        return 'Вы — коала. Любите спать и отдыхать в уюте, цените спокойствие и безопасность.'
    if score==8:
        return 'Вы — гепард. Вы быстры и решительны, любите стремительные действия и вызовы.'
    if score==9:
        return 'Вы — олень. Вы спокойны и уравновешенны, можете быть как активным и бодрым, \
так и тихим и пассивным. '
    if score==10:
        return 'Вы — дельфин. Вы очень умны и любознательны, почти не спите и всегда бодры, \
готовы к новым открытиям и общению.'
    if score in [11,12]:
        return 'Вы — белый медведь. Вы сильны и выносливы, привыкли к суровым условиям и \
умеете сохранять спокойствие в любых испытаниях.'
        
    
    
