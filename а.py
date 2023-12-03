import telebot
import sqlite3

db = sqlite3.connect('user.db')
sql = db.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS user (id INTEGER, username TEXT, user_contact TEXT);')
db.close()
bot = telebot.TeleBot('6488211867:AAF6O03JFXlXQjTBJTM4KAXkqJLTwiyizm0')


@bot.message_handler(commands=['start'])
def start(message):
    global uid
    uid = message.from_user.id
    bot.send_message(uid, 'Привет, Напиши свое имя')
    bot.register_next_step_handler(message, get_name)
def get_name(message):
   username = message.text
   bot.send_message(uid, 'Нажмите на кнопку', reply_markup=classmethod.kontakt())
   bot.register_next_step_handler(message, get_number, username)

def get_number(message, username):
    if message.contact and message.contact.phone_number:
        user_contact = message.contact.phone_number
        bot.send_message(uid, 'Отлично вы прошли регистрацию', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, save, user_contact, username)
    else:
        bot.send_message(uid, 'Вы не прошли повторите!')
        bot.register_next_step_handler(message, get_name, username)

def save(message, user_contact, username):
    db = sqlite3.connect('user.db')
    sql = db.cursor()
    sql.execute('INSERT INTO user (id, username, user_contact) VALUES (?,?,?);', (uid, username, user_contact))
    db.commit()
    db.close()

bot.infinity_polling()
