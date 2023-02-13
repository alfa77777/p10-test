import telebot
from environs import Env
import os
import csv

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

student_list = []


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 "Hello! I am a bot that can register students' information. "
                 "Please use the /register command to start.")


@bot.message_handler(commands=['register'])
def register(message):
    bot.reply_to(message,
                 "Please send me the following information in this format: Name, Age, Course"
                 "\nFor example: John Doe, 25, Computer Science")


@bot.message_handler(commands=['get_students'])
def get_students(message):
    try:
        with open("students.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            if os.path.getsize("students.csv") == 0:
                bot.reply_to(message, "No students have been registered yet.")
                return
    except FileNotFoundError:
        bot.reply_to(message, "No students have been registered yet.")
        return
    else:
        student_info = "\n".join([f"Name: {row['Name']}, Age: {row['Age']}, Course: {row['Course']}" for row in reader])
        bot.reply_to(message, f"Here is the list of registered students:\n{student_info}")

        csvfile.seek(0)  # Go back to the beginning of the file

        keyboard = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton(text="Send me the CSV file", callback_data="send_csv")
        keyboard.add(button)
        bot.send_message(chat_id=message.chat.id, text="Do you want to receive the students.csv file?",
                         reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "send_csv")
def callback_send_csv(call):
    with open("students.csv", "rb") as csvfile:
        bot.send_document(chat_id=call.message.chat.id, document=csvfile)


@bot.message_handler(commands=['clear'])
def clear(message):
    with open("students.csv", "w"):
        pass  # Do nothing, this will overwrite the file and clear its content
    bot.reply_to(message, "Cleared the student information successfully.")


@bot.message_handler(content_types=['text'])
def register_student(message):
    info = message.text.split(", ")
    if len(info) == 3:
        name, age, course = info
        student = {"Name": name, "Age": age, "Course": course}
        student_list.append(student)

        with open("students.csv", "a", newline="") as csvfile:
            fieldnames = ["Name", "Age", "Course"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header only once
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(student)

        bot.reply_to(message, f"Successfully registered {name} with age {age} taking {course}")
    else:
        bot.reply_to(message, "Invalid input format. Please send the information in this format: Name, Age, Course")


def bot_commads():
    return [
        telebot.types.BotCommand("/start", "start bot"),
        telebot.types.BotCommand("/register", "registrate students"),
        telebot.types.BotCommand("/get_students", "get info students"),
        telebot.types.BotCommand("/clear", "clear students info")
    ]


if __name__ == "__main__":
    bot.set_my_commands(commands=bot_commads())
    bot.polling()

