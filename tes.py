import telebot
from telebot import types

age, height, weight, sex = 0, 0, 0, 0
calories, fats, proteins, carbohydrates = 0.0, 0.0, 0.0, 0.0

bot = telebot.TeleBot('6781506875:AAFMn7bxvL4jbQ4x4iVQsilY9Of2RlWeejo') #токен
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Приступим!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Я бот, который поможет вам skinnуть вес.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if (message.text == 'Приступим!') or (message.text == 'Назад'): #НАЗАД и начало
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Ввести данные')
        btn2 = types.KeyboardButton('Рассчитать КБЖУ')
        btn3 = types.KeyboardButton('Меню')

        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Вот что я умею: '
                                               '\n• Записать ваши данные'
                                               '\n• Рассчитать суточную норму КБЖУ'
                                               '\n• Подобрать индивидуальный рацион питания', reply_markup=markup) #ответ бота


    elif message.text == 'Ввести данные': #мы
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Введите возраст, вес, рост и пол(мужчина|женщина) через пробел') #бот
        bot.register_next_step_handler(message, welcome_user)

    elif message.text == 'Рассчитать КБЖУ': #мы

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Худеем')
        btn2 = types.KeyboardButton('Удерживаем')
        btn3 = types.KeyboardButton('Набираем')
        btn4 = types.KeyboardButton('Назад')

        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.from_user.id, 'Здесь я могу помочь рассчитать вам суточную норму КБЖУ, но для этого мне нужно узнать вашу цель:'
                                               '\n• Похудеть'
                                               '\n• Удерживать вес'
                                               '\n• Набрать мышечную массу', reply_markup=markup) #бот


        bot.register_next_step_handler(message, counter_CPFC)



def welcome_user(message):
    text_mes = message.text.split()
    global age, height, weight, sex
    age = int(text_mes[0])
    weight = int(text_mes[1])
    height = int(text_mes[2])
    if (text_mes[3] == 'мужчина'): sex = 0
    elif (text_mes[3] == 'женщина'): sex = 1

    bot.send_message(message.from_user.id, f'*Ваши данные:*\nВозраст: {age}\nВес: {weight}\nРост: {height}\nПол: {text_mes[3]} ', parse_mode="Markdown")  # бот
    bot.send_message(message.from_user.id, 'Если данные указаны неверно, снова выберите в меню пункт "Ввести данные"')

def counter_CPFC(message):
    global calories, fats, proteins, carbohydrates, age, height, weight, sex
    if (message.text == 'Худеем'):
        #вода
        if (sex == 1):
            calories = (weight*9.99 + height*6.25 - age*4.92 - 161)*1.3*0.9
            proteins = calories * 0.3 / 4
            fats = calories * 0.3 / 9
            carbohydrates = calories * 0.4 / 4

        elif (sex == 0):
            calories = (weight*9.99 + height*6.25 - age*4.92 + 5)*1.3*0.9
            proteins = calories * 0.3 / 4
            fats = calories * 0.3 / 9
            carbohydrates = calories * 0.4 / 4

    if (message.text == 'Удерживаем'):
        if (sex == 1):
            calories = (weight*9.99 + height*6.25 - age*4.92 - 161)*1.3
            proteins = calories * 0.3 / 4
            fats = calories * 0.3 / 9
            carbohydrates = calories * 0.4 / 4

        elif (sex == 0):
            calories = (weight*9.99 + height*6.25 - age*4.92 + 5)*1.3
            proteins = calories * 0.3 / 4
            fats = calories * 0.3 / 9
            carbohydrates = calories * 0.4/ 4

    if (message.text == 'Набираем'):
        if (sex == 1):
            calories = (weight*9.99 + height*6.25 - age*4.92 - 161)*1.3*1.1
            proteins = calories * 0.3 / 4
            fats = calories * 0.3 / 9
            carbohydrates = calories * 0.5 / 4

        elif (sex == 0):
            calories = (weight*9.99 + height*6.25 - age*4.92 + 5)*1.3*1.1
            proteins = calories * 0.3 / 4
            fats = calories * 0.3 / 9
            carbohydrates = calories * 0.5 / 4

    bot.send_message(message.from_user.id, f'Учитывая введенные данные, ваша суточная норма:'
                                           f'\n• Калорий: {calories:.2f} кКал\n• Белков: {proteins:.2f} г'
                                           f'\n• Жиров: {fats:.2f} г\n• Углеводов: {carbohydrates:.2f} г')
    bot.send_message(message.from_user.id, 'Если вы хотите рассчитать КБЖУ для иного варианта работы с весом, нажмите "Назад" и измените свой выбор')  # бот

    if (message.text == 'Назад'):
        get_text_messages(message)


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть