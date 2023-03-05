import psycopg2
import requests
from environs import Env
# from datetime import datetime

env = Env()
env.read_env()
# Trello API credentials
API_KEY = env("TRELLO_KEY")
API_TOKEN = env("TRELLO_TOKEN")

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="trello",
    user="postgres",
    password="12345"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Retrieve the list of boards from the Trello API
url = f"https://api.trello.com/1/members/me/boards?key={API_KEY}&token={API_TOKEN}"
response = requests.get(url)
boards = response.json()

# Iterate over the boards and insert them into the database
for board in boards:
    board_id = board["id"]
    board_name = board["name"]
    # board_created_at = datetime.strptime(board["dateCreated"], "%Y-%m-%dT%H:%M:%S.%fZ")
    # board_updated_at = datetime.strptime(board["dateLastActivity"], "%Y-%m-%dT%H:%M:%S.%fZ")
    cur.execute("""
        INSERT INTO board (id, name)
        VALUES (%s, %s)
    """, [board_id, board_name])

    # Retrieve the lists for the board from the Trello API
    url = f"https://api.trello.com/1/boards/{board_id}/lists?key={API_KEY}&token={API_TOKEN}"
    response = requests.get(url)
    lists = response.json()

    # Iterate over the lists and insert them into the database
    for lst in lists:
        list_id = lst["id"]
        list_name = lst["name"]
        list_board_id = board_id
        # list_created_at = datetime.strptime(lst["dateCreated"], "%Y-%m-%dT%H:%M:%S.%fZ")
        # list_updated_at = datetime.strptime(lst["dateLastActivity"], "%Y-%m-%dT%H:%M:%S.%fZ")
        cur.execute("""
            INSERT INTO list (id, name, board_id)
            VALUES (%s, %s, %s)
        """, [list_id, list_name, list_board_id])

        # Retrieve the cards for the list from the Trello API
        url = f"https://api.trello.com/1/lists/{list_id}/cards?key={API_KEY}&token={API_TOKEN}"
        response = requests.get(url)
        cards = response.json()

        # Iterate over the cards and insert them into the database
        for card in cards:
            card_id = card["id"]
            card_name = card["name"]
            card_description = card.get("desc", "")
            card_list_id = list_id
            # card_created_at = datetime.strptime(card["dateCreated"], "%Y-%m-%dT%H:%M:%S.%fZ")
            # card_updated_at = datetime.strptime(card["dateLastActivity"], "%Y-%m-%dT%H:%M:%S.%fZ")
            cur.execute("""
                INSERT INTO card (id, name, description, list_id)
                VALUES (%s, %s, %s, %s)
            """, [card_id, card_name, card_description, card_list_id])

            # Retrieve the members for the card from the Trello API
            url = f"https://api.trello.com/1/cards/{card_id}/members?key={API_KEY}&token={API_TOKEN}"
            response = requests.get(url)
            members = response.json()

            # Iterate over the members and insert them into the database
            for member in members:
                member_id = member["id"]
                member_full_name = member["fullName"]
                cur.execute("""
                    INSERT INTO member (id, full_name)
                    VALUES (%s, %s)
                """, [member_id, member_full_name])

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection to the database
    cur.close()
    conn.close()
