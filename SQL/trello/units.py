import psycopg2
from environs import Env
import telebot

env = Env()
env.read_env()

BOT_TOKEN = env("TELEGRAM_API")
bot = telebot.TeleBot(BOT_TOKEN)

env = Env()
env.read_env()

API_KEY = env("TRELLO_KEY")
API_TOKEN = env("TRELLO_TOKEN")
host = env("HOST")
database = env("DATABASE")
user = env("USER")
password = env("PASSWORD")

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)


def get_data(table_n):
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM {table_n}")
    rows = cur.fetchall()

    colnames = [desc[0] for desc in cur.description]

    result = []
    for row in rows:
        row_dict = {}
        for i in range(len(colnames)):
            row_dict[colnames[i]] = row[i]
        result.append(row_dict)
    return result

def column_informations(table_n, column_n):
    cur = conn.cursor()

    cur.execute(f"SELECT {column_n} FROM {table_n}",)
    rows = cur.fetchall()
    result = []
    for i in rows:
        result.append(i[0])
    return result


# print(column_informations("boards", "name"))

def new_user(table_name, column, data):
    cur = conn.cursor()

    cur.execute(f"INSERT INTO {table_name} ({column}) VALUES ({data})")

    conn.commit()


def get_member_id(username):
    cur = conn.cursor()

    cur.execute(f"SELECT id FROM members where trello_username = %s", (username,))
    rows = cur.fetchall()
    return rows[0][0]

def put_trello_username(chat_id, username):
    cur = conn.cursor()

    cur.execute(f"UPDATE users SET username = %s WHERE chat_id = %s", (username, chat_id))

    conn.commit()

def put_trello_member_id(username, member_id):
    cur = conn.cursor()

    cur.execute(f"UPDATE users SET member_id = %s WHERE username = %s", (member_id, username))

    conn.commit()

# print(put_trello_member_id("boburtohirov01", get_member_id("boburtohirov01")))

def get_column_info(table_n, column_name):
    data = get_data(table_n)
    check = []
    for i in data:
        check.append(i[column_name])
    return check

def set_fullname(message, chat_id):
    fullname = message.from_user.first_name
    if message.from_user.last_name:
        fullname += f" {message.from_user.last_name}"
    cur = conn.cursor()

    cur.execute(f"UPDATE users SET full_name = %s WHERE chat_id = %s", (fullname, chat_id))

    conn.commit()

def sql_get_info(table_n, column_n, where = None, check = None):
    cur = conn.cursor()
    if where:
        cur.execute(f"SELECT {column_n} FROM {table_n} where {where} = {check}")
    else:
        cur.execute(f"SELECT {column_n} FROM {table_n}")

    rows = cur.fetchall()
    result = []

    for i in rows:
        result.append(i[0])
    return result
# print(sql_get_info("boards", "name"))