import asyncio

import logging

from aiogram import Bot, Dispatcher

import terms_of_use

# bot = telebot.TeleBot('7783272138:AAFH58ANX4HcKzjNR7OeY3hSEOwCt4SM3A8')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def main():
    bot = Bot(token='7783272138:AAFH58ANX4HcKzjNR7OeY3hSEOwCt4SM3A8')
    dp = Dispatcher()

    dp.include_router(terms_of_use.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

#
# #Проверка фотографии
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     bot.reply_to(message, 'GOOD!')
#
# #Отправка на сайт
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open_new_tab('https://www.nomerogram.ru/')


#НАЧАЛО ПОЛЬЗОВАНИЯ БОТОМ
# @bot.message_handler(commands=['start', 'main', 'hello'])
# def main(message):
#     markup = types.InlineKeyboardMarkup()
#     button_readnda = types.InlineKeyboardButton('Прочитать политику конфиденциальности', callback_data='start_read_nda')
#     markup.add(button_readnda)
#     bot.send_message(message.chat.id, f'Добро пожаловать, {message.from_user.last_name} {message.from_user.first_name} в <b>Номероавто РБ🇧🇾</b>!''\n \nЭто — <b>единственный</b> в Беларуси Telegram-бот для <em>регистрации</em> и получения <em>информации</em> об авто и его владельца в Республике Беларусь! \n \n Пожалуйста, сначала ознакотесь с политикой конфиденциальности ⬇', parse_mode='html', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.message:
#         if call.data == 'start_read_nda':
#             bot.send_message(call.message.chat.id, 'Политика конфиденциальности "Номероавто РБ🇧🇾" \n1. Введение: Добро пожаловать в "Номероавто РБ🇧🇾". Мы ценим вашу конфиденциальность и стремимся защищать ваши персональные данные. Эта Политика конфиденциальности объясняет, как мы собираем, используем и защищаем вашу информацию, когда вы используете нашего бота в Telegram.\n 2. Какие данные мы собираем: При использовании "Номероавто" мы можем собирать следующие типы данных:\n-Фотографии автомобилей: Вы можете загружать фотографии автомобилей, которые мы используем для предоставления нашей услуги.\n-Метаданные: Мы также можем собирать метаданные, включая дату, время и местоположение, когда была сделана фотографии (если доступно).\n-Никнейм пользователя: Ваш никнейм в Telegram будет использоваться для взаимодействия с ботом.\n 3. Как мы используем ваши данные: Мы используем собранные данные для следующих целей: Предоставление услуги: Чтобы показать вам марку и модель автомобиля по загруженным фотографиям.\n-Улучшение сервиса: Для анализа и улучшения работы нашего бота.\n-Поддержка пользователей: Для оказания поддержки и ответов на ваши вопросы.\n 4. Безопасность данных: Мы принимаем разумные меры для защиты ваших данных от несанкционированного доступа, использования или раскрытия. Однако, пожалуйста, помните, что никакой способ передачи данных по интернету или способ хранения данных не является 100% безопасным.\n 5. Хранение данных: Мы храним ваши данные только столько времени, сколько это необходимо для выполнения целей, указанных в этой Политике конфиденциальности. После этого ваши личные данные будут удалены или анонимизированы.\n 6. Передача данных третьим лицам: Мы не передаем ваши данные третьим лицам без вашего согласия, за исключением случаев, когда это необходимо для выполнения наших обязательств перед вами, или если это требуется по закону. Мы не несём ответсвенности за полную сохранность ваших личных данный, которые видны в аккаунте!\n 7. Изменения в политике конфиденциальности: Мы можем периодически обновлять эту Политику конфиденциальности. Мы обязательно уведомим вас о любых изменениях, размещая обновленную версию здесь. Рекомендуем периодически проверять эту страницу на предмет любых обновлений.\n 8. Контактные данные: Если у вас есть вопросы или пожелания по поводу нашей Политики конфиденциальности, пожалуйста, свяжитесь с нами через Telegram-бота или по следующему адресу электронной почты: celp064@gmai.com\n 9. Согласие на обработку данных Используя "Номероавто РБ", вы подтверждаете, что ознакомлены с данной Политикой конфиденциальности и соглашаетесь с условиями обработки ваших данных.\n \n <b>Напишите</b> <u>ПРИНЯТЬ</u>, если вы согласны с условиями на обработку данных или <u>ОТКЛОНИТЬ</u>, если не согласны.', parse_mode='html')
#
# #Инфа для разраба
# @bot.message_handler(commands=['kirilldevinfo'])
# def main(message):
#     bot.send_message(message.chat.id, message)
#     bot.reply_to(message, 'ЭТОТ БОТ СОЗДАН КИРИЛЛОМ КОВАЛЬЧУКОМ! А ВАНЯ ! \n')
#
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'отклонить':
#         bot.send_message(message.chat.id, '❌Вы не приняли наш запрос на обработку данных!❌\n \nВы должны дать согласие на обработку данных. Иначе Вы не сможете пользоваться ботом!\n \n<u><b>Напишите</b> "ПРИНЯТЬ", если вы согласны с условиями на обработку данных или мы не сможем с вами сотрудничать!</u>', parse_mode='html')
#     elif message.text.lower() == 'принять':
#         markup = types.ReplyKeyboardMarkup()
#         markup.add(types.KeyboardButton('Открыть Web-приложение', web_app=WebAppInfo(url='https://kirill1029.github.io/')))
#         bot.send_message(message.chat.id, '✅Вы приняли наш запрос на обработку данных!✅\n \n⬇ Теперь вы можете открыть наше Web-приложение ⬇\n ', parse_mode='html', reply_markup=markup)
#
# @dp.message_handler(content_types=['web_app_data'])
# async def web_app(message: types.Message):
#     await message.answer(message.web_app_data.data)
#
# bot.polling(none_stop=True)
#
# executor.start_polling(dp)
#
#
#
#
# markup = types.InlineKeyboardMarkup()
# button_accept = markup.add(types.InlineKeyboardButton('✅Я принимаю все условия✅', callback_data='readed'))
# button_decline = markup.add(types.InlineKeyboardButton('❌Я не принимаю эти условия❌', callback_data='not-readed'))
# markup.add(button_accept, button_decline)