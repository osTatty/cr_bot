import telebot
from telebot import types

age, height, weight, sex = 0, 0, 0, 0
calories, fats, proteins, carbohydrates, water = 0.0, 0.0, 0.0, 0.0, 0.0

bot = telebot.TeleBot('6781506875:AAFMn7bxvL4jbQ4x4iVQsilY9Of2RlWeejo') #токен
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Приступим!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋🏼 Привет! Я бот, который поможет вам skinnуть вес.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if (message.text == 'Приступим!') or (message.text == 'Назад'): #НАЗАД и начало
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Ввести данные')
        btn2 = types.KeyboardButton('Рассчитать КБЖУ')
        btn3 = types.KeyboardButton('Меню')
        btn4 = types.KeyboardButton('Мои данные')

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Вот что я умею: '
                                               '\n✍🏼 Записать ваши данные'
                                               '\n🥗 Подобрать индивидуальный рацион питания'
                                               '\n🏋🏼️ Рассчитать суточную норму КБЖУ'
                                               '\n📖 Показать ваши данные', reply_markup=markup) #ответ бота

    elif message.text == 'Ввести данные': #мы
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, '📝 Введите возраст, вес, рост и пол(мужчина|женщина) через пробел') #бот

        bot.register_next_step_handler(message, func_check1)


    elif message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Завтрак')
        btn2 = types.KeyboardButton('Обед')
        btn3 = types.KeyboardButton('Ужин')
        btn4 = types.KeyboardButton('Назад')

        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.from_user.id,
                         '☝🏼 Я подобрал индивидуальный рацион питания, основываясь на потребностях вашего организма в питательных веществах.'
                         '\n\n📋 Можете ознакомиться с несколькими вариантами блюд на каждый прием пищи.', reply_markup=markup)

    elif message.text == 'Мои данные': #мы
        global sex
        if (sex == 1):
            sexy = "женщина"
        else:
            sexy = "мужчина"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id,
                         f'*🗒 Ваши данные*\n▸ Возраст: {age}\n▸ Вес: {weight}\n▸ Рост: {height}\n▸ Пол: {sexy} ',
                         parse_mode="Markdown")

    elif message.text == 'Рассчитать КБЖУ': #мы

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Худеем')
        btn2 = types.KeyboardButton('Удерживаем')
        btn3 = types.KeyboardButton('Набираем')
        btn4 = types.KeyboardButton('Назад')

        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.from_user.id,
                         '☝🏼 Здесь я могу помочь рассчитать вам суточную норму КБЖУ, но для этого мне нужно узнать вашу цель:'
                         '\n▸ Похудеть'
                         '\n▸ Удерживать вес'
                         '\n▸ Набрать мышечную массу', reply_markup=markup)  # бот

        bot.register_next_step_handler(message, counter_CPFC)



def welcome_user(message):
    text_mes = message.text.split()
    global age, height, weight, sex
    age = int(text_mes[0])
    weight = int(text_mes[1])
    height = int(text_mes[2])
    if (text_mes[3] in "женщина"):
        sex = 1
        text_mes[3] = "женщина"
    elif (text_mes[3] in "мужчина"):
        sex = 0
        text_mes[3] = "мужчина"

    bot.send_message(message.from_user.id,
                     f'*🗒 Ваши данные*\n▸ Возраст: {age}\n▸ Вес: {weight}\n▸ Рост: {height}\n▸ Пол: {text_mes[3]} ',
                     parse_mode="Markdown")
    bot.send_message(message.from_user.id, 'Если данные указаны неверно, снова выберите в меню пункт "Ввести данные"')

def counter_CPFC(message):
    global calories, fats, proteins, carbohydrates, age, height, weight, sex, water
    if (message.text != 'Назад'):
        if (message.text == 'Худеем'):
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
        water = 1500 + (weight - 20) * 20

        bot.send_message(message.from_user.id, f'Учитывая введенные данные, ваша суточная норма:'
                                               f'\n🔥 Калорий: {calories:.2f} кКал\n🍳 Белков: {proteins:.2f} г'
                                               f'\n🥩 Жиров: {fats:.2f} г\n🥞 Углеводов: {carbohydrates:.2f} г'
                                               f'\n💧 Норма воды: {water:.0f} мл')
        bot.send_message(message.from_user.id, 'Если вы хотите рассчитать КБЖУ для иного варианта работы с весом, нажмите "Назад" и измените свой выбор')  # бот
    else:
        get_text_messages(message)


def func_check1(message):
    check1 = message.text.split()

    if ((check1[0].isdigit() and check1[1].isdigit() and check1[2].isdigit()) and
                (int(check1[0]) > 0 and int(check1[0]) <= 110) and (int(check1[1]) >= 20 and int(check1[1]) <= 250) and
                (int(check1[2]) >= 90 and int(check1[2]) <= 260) and (check1[3] in "женщина" or check1[3] in "мужчина")):
        welcome_user(message)

    else:
        bot.send_message(message.from_user.id, '🤬 Данные введены некорректно! Повторите попытку. ')  # бот
        bot.register_next_step_handler(message, func_check1)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть