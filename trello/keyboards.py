from units import column_informations, sql_get_info
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton)



def get_inline_boards_btn(action):
    global last_board_id
    boards_name = column_informations("boards", "name")
    boards_id = column_informations("boards", "id")
    boards_len = len(boards_name)
    inline_boards_btn = InlineKeyboardMarkup()
    if boards_len % 2 == 0:
        last_board = None
    else:
        last_board = boards_name.pop()
        last_board_id = boards_id.pop()
    for i in range(0, len(boards_name) - 1, 2):
        inline_boards_btn.add(
            InlineKeyboardButton(
                boards_name[i], callback_data=f"{action}_{boards_id[i]}"
            ),
            InlineKeyboardButton(
                boards_name[i + 1], callback_data=f"{action}_{boards_id[i + 1]}"
            ),
        )
    if last_board and last_board_id:
        inline_boards_btn.add(
            InlineKeyboardButton(last_board, callback_data=f"{action}_{last_board_id}")
        )
    return inline_boards_btn

def get_lists_btn(board_id):
    lists_btn = ReplyKeyboardMarkup()
    lists = sql_get_info("lists", "name", "board_id", board_id)
    if len(lists) % 2 == 0:
        last_list = None
    else:
        last_list = lists.pop()
    for list_index in range(0, len(lists) - 1, 2):
        lists_btn.add(
            KeyboardButton(lists[list_index]),
            KeyboardButton(lists[list_index + 1])
        )
    if last_list:
        lists_btn.add(KeyboardButton(last_list))
    return lists_btn

def get_inline_lists_btn(board_id, action):
    global last_list_id
    lists_inline_btn = InlineKeyboardMarkup()
    lists = sql_get_info("lists", "name", "board_id", board_id)
    lists_id = sql_get_info("lists", "id", "board_id", board_id)
    if len(lists) % 2 == 0:
        last_list = None
    else:
        last_list = lists.pop()
        last_list_id = lists_id.pop()
    for i in range(len(lists) - 1):
        lists_inline_btn.add(
            InlineKeyboardButton(
                lists[i],
                callback_data=f'{action}_{lists_id[i]}'
            ),
            InlineKeyboardButton(
                lists[i + 1],
                callback_data=f'{action}_{lists_id[i + 1]}'
            )
        )
    if last_list and last_list_id:
        lists_inline_btn.add(
            InlineKeyboardButton(
                last_list,
                callback_data=f'{action}_{last_list_id}'
            )
        )
    return lists_inline_btn