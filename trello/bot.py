from environs import Env
import psycopg2.extras
import telebot
from main import update_database
from units import get_column_info, put_trello_username, new_user, get_member_id, \
    put_trello_member_id, set_fullname, sql_get_info
from keyboards import get_inline_boards_btn, get_inline_lists_btn
env = Env()
env.read_env()

API_KEY = env("TRELLO_KEY")
API_TOKEN = env("TRELLO_TOKEN")
host = env("HOST")
database = env("DATABASE")
user = env("USER")
password = env("PASSWORD")

BOT_TOKEN = env("TELEGRAM_API")
bot = telebot.TeleBot(BOT_TOKEN)

# Connect to the database
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)




@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum, ro'yxatdan o'tish uchun /register")

# /Register
@bot.message_handler(commands=["register"])
def register_handler(message):
    check = get_column_info("users", "chat_id")
    if message.chat.id not in check:
        new_user("users", "chat_id", message.chat.id)
        bot.send_message(message.chat.id, "Trello username yuboring:")
        bot.register_next_step_handler(message, get_trello_username)
    else:
        bot.send_message(message.chat.id, "Siz avval ro'yxatdan o'tgansiz")


def get_trello_username(message):
    username = get_column_info("users", "username")
    if message.text in username:
        bot.send_message(message.chat.id, "Bu user name mavjud! qayta urinib ko'ring /register")
    else:
        put_trello_username(message.chat.id, message.text)
        set_fullname(message, message.chat.id)
        try:
            member_id = get_member_id(message.text)
            put_trello_member_id(message.text, member_id)
        except Exception:
            pass
        bot.send_message(message.chat.id, "Muvaffaqqiyatli qo'shildi")


@bot.message_handler(commands=["update_trello_username"])
def update_tr_username(message):
    bot.send_message(message.chat.id, "Yangi username kiriting:")
    bot.register_next_step_handler(message, con_up_username)


def con_up_username(message):
    username = get_column_info("users", "username")
    if message.text in username:
        bot.send_message(message.chat.id, "Bu user name mavjud! qayta urinib ko'ring /update_trello_username")
    else:
        put_trello_username(message.chat.id, message.text)
        set_fullname(message, message.chat.id)
        try:
            member_id = get_member_id(message.text)
            put_trello_member_id(message.text, member_id)
        except Exception:
            pass
        bot.send_message(message.chat.id, "Muvaffaqqiyatli yangilandi")


@bot.message_handler(commands=["boards"])
def get_boards(message):

    check = get_column_info("users", "chat_id")
    if message.chat.id not in check:
        bot.send_message(message.chat.id, "Trello username topilmadi.")
    else:
        bot.send_message(message.chat.id, "Doskani tanlang:",
                         reply_markup=get_inline_boards_btn("show_tasks"))


@bot.callback_query_handler(lambda call: call.data.startswith("show_tasks"))
def get_board_lists(call):
    message = call.message
    board_id = call.data.split("_")[2]
    bot.send_message(
        message.chat.id, "Listni tanlang:", reply_markup=get_inline_lists_btn(board_id, "show_list_tasks")
    )


@bot.callback_query_handler(lambda c: c.data.startswith("show_list_tasks"))
def get_member_cards(call):
    message = call.message
    list_id = call.data.split("_")[3]
    cards = sql_get_info("cards", "name", "list_id", list_id)
    msg = "on card:\n"
    for i in range(len(cards)):
        msg += f"{i}. {cards[i]}\n"
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=["update"])
def update(message):
    send_message = bot.send_message(message.chat.id, "Biroz kuting yangilanmoqda!")
    try:
        update_database()
        bot.edit_message_text(chat_id=message.chat.id, message_id=send_message.message_id, text="Database yangilandi!")
    except Exception:
        bot.edit_message_text(chat_id=message.chat.id, message_id=send_message.message_id,
                              text="Database yangilanmadi.")


my_commands = [
    telebot.types.BotCommand("/start", "Boshlash"),
    telebot.types.BotCommand("/register", "Ro'yxatdan o'tish"),
    telebot.types.BotCommand("/boards", "Doskalarni ko'rish"),
    telebot.types.BotCommand("/update", "Database ma'lumotlarini yangilash"),
    telebot.types.BotCommand("/update_trello_username", "Trello username yangilash")
]

if __name__ == "__main__":
    print("Started.....")
    bot.set_my_commands(my_commands)
    bot.infinity_polling()

