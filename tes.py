import telebot
from telebot import types

age, height, weight, sex = 0, 0, 0, 0
calories, fats, proteins, carbohydrates, water = 0.0, 0.0, 0.0, 0.0, 0.0
medias = []

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

        bot.register_next_step_handler(message, sendPhoto)

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

@bot.message_handler(content_types=['text'])
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
        #bot.send_message(message.from_user.id, 'Если вы хотите рассчитать КБЖУ для иного варианта работы с весом, нажмите "Назад" и измените свой выбор')  # бот
        bot.register_next_step_handler(message, counter_CPFC)
    else:
        get_text_messages(message)
@bot.message_handler(content_types=['text'])
def sendPhoto(message):
    global calories, medias
    if (message.text != 'Назад'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        if (calories < 1300 or calories > 3500):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.from_user.id,
                             '😢 К сожалению, мне не удалось подобрать вам правильный рацион. Проверьте введенные данные и попробуйте снова!', reply_markup=markup)
            return

        if (message.text == 'Завтрак'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.from_user.id,'😋 Вот ваш завтрак! Можете выбрать любой вариант, который ближе для вас', reply_markup=markup)

            if (calories >= 1300 and calories < 1700): #2 и 3
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1-1KUkNa7Ipv-aAbAroJuwMgB6WMy6M26'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1v75kg5aTBt2O8xt-h6fLZWq6C_cTYKUd')]
            elif (calories >= 1700 and calories < 2000): #5 и 8
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1aiRz-zVDRtF09XrHoXEJxugbJjtqdlao'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=112DTqBjlIfPUrxZoTAc5s9YZqAS6H0Ks')]
            elif (calories >= 2000 and calories < 2300): #9 и 10
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=15hvZ41AKXeW7AESyAxiDOYyHB-nFN_gk'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1lgCsLm75YXp17hLQ0nnERF7itiEAQkG2')]
            elif (calories >= 2300 and calories < 2700): #4 и 6
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1UqRpBMjuwVI_eTYI2yzjjGIABFIpKiLG'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1zDHPkwynftduwuNfKKMwOLShama8CKMf')]
            elif (calories >= 2700 and calories < 3500): #1 и 7
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1AYduq-4KEbFdkIbaAv6Nw5VeFWHSJ7nf'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1A0TKNKGlkYvOoTr4_7Kp0vayf6uex7TO')]


        if (message.text == 'Обед'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.from_user.id,'😋 Вот ваш обед! Можете выбрать любой вариант, который ближе для вас', reply_markup=markup)

            if (calories >= 1300 and calories < 1700): #3 и 5
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1oQ8acZ7exd2SYlYR24nJhyBzPG-eAF-q'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1zXwoekmFZHPzf17kwLTAHWF-YdI2O_yL')]
            elif (calories >= 1700 and calories < 2000): #4 и 1
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1KofnjHQf4QktRBnZOCqAy5bbKOLwbqny'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1IX2N0gr2YrV4e3Dv2Lm9mTYPbJ-Y_Jrx')]
            elif (calories >= 2000 and calories < 2300): #2 и 7
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1fILF_sgpE3l5W0ljz_hlvIu6VaCLy8Xa'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1VpcrUn_aSMzwQ-dv8nbHsip_SB2s2PML')]
            elif (calories >= 2300 and calories < 2700): #8 и 10
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1ZbZNnLLkUSWWXlALNDNOjTd-HYOl2jiX'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1zWlwqPj_wgG2L1lBlKSNsxusal4VvkwP')]
            elif (calories >= 2700 and calories < 3500): #6 и 9
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=141KX7S8rCdLYSNNjztEZumZvuV1kNEJv'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1yp0cLgfm_qsDAKWYIeSKb1Fo6KWzZT1T')]

        if (message.text == 'Ужин'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.from_user.id,'😋 Вот ваш ужин! Можете выбрать любой вариант, который ближе для вас', reply_markup=markup)

            if (calories >= 1300 and calories < 1700): #4 и 6
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1aZTySp1IY5zfnjmPBhSa7mCCFsLuTEsG'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1an1-P-aW1iWjjFY5FR770LNcP8IVt50R')]
            elif (calories >= 1700 and calories < 2000): #9 и 2
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=19fE3jlQddFbuQSmm-ug8X5XOj3kNyDsO'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1qRB8hLNC_xbLkJ4SkVzMAPYyHWcNcAbj')]
            elif (calories >= 2000 and calories < 2300): #1 и 8
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1EjkRyMF0EzCAKBzTqyuKiSm_uq7iYNyr'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1zifIdYjcqHiGIWJtBXL3VoZV_PodW6Y8')]
            elif (calories >= 2300 and calories < 2700): #3 и 5
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1OTMsdH5iZUOyetjFcDiNT6qbGHB7xLqK'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1kpAfSeEz4om6RZuYF61H8xquOXJYyUzr')]
            elif (calories >= 2700 and calories < 3500): #7 и 10
                medias = [types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1G5EI_zsjziEXaRZmV-NmOAfGYsfkkVuA'),
                          types.InputMediaPhoto('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1s5jlLeDdLRIUlakyEroZvk_UObJ08tiP')]

        bot.send_media_group(message.from_user.id, medias)
        bot.register_next_step_handler(message, sendPhoto)

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