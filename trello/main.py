import requests
import psycopg2
from environs import Env

env = Env()
env.read_env()
# Trello API credentials
API_KEY = env("TRELLO_KEY")
API_TOKEN = env("TRELLO_TOKEN")
host = env("HOST")
database = env("DATABASE")
user = env("USER")
password = env("PASSWORD")

def update_database():
    # Connect to the database
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    cur = conn.cursor()

    # Retrieve the boards from the Trello API
    url = f"https://api.trello.com/1/members/me/boards?key={API_KEY}&token={API_TOKEN}"
    response = requests.get(url)
    boards = response.json()

    # Loop through each board and insert it into the database
    for board in boards:
        board_id = board["id"]
        board_name = board["name"]
        board_trello_id = board_id
        cur.execute("""
            INSERT INTO boards (name, trello_id)
            VALUES (%s, %s)
            ON CONFLICT (trello_id) DO UPDATE
            SET name = EXCLUDED.name
        """, [board_name, board_trello_id])
        conn.commit()

        # Retrieve the lists for the board from the Trello API
        url = f"https://api.trello.com/1/boards/{board_id}/lists?key={API_KEY}&token={API_TOKEN}"
        response = requests.get(url)
        lists = response.json()

        # Execute a SELECT query to get the id of a row
        cur.execute("SELECT id FROM boards WHERE trello_id = %s", (board_id,))

        # Fetch the result
        result = cur.fetchone()

        # Get the id from the result
        board_id = result[0]

        # Loop through each list and insert it into the database
        for lst in lists:
            list_id = lst["id"]
            list_name = lst["name"]
            list_board_id = board_id
            cur.execute("""
                INSERT INTO lists (name, trello_id, board_id)
                VALUES (%s, %s, %s)
                ON CONFLICT (trello_id) DO UPDATE
                SET name = EXCLUDED.name, board_id = EXCLUDED.board_id
            """, [list_name, list_id, list_board_id])
            conn.commit()

            # Retrieve the cards for the list from the Trello API
            url = f"https://api.trello.com/1/lists/{list_id}/cards?key={API_KEY}&token={API_TOKEN}"
            response = requests.get(url)
            cards = response.json()

            # Execute a SELECT query to get the id of a row
            cur.execute("SELECT id FROM lists WHERE trello_id = %s", (list_id,))

            # Fetch the result
            result = cur.fetchone()

            # Get the id from the result
            list_id = result[0]

            # Loop through each card and insert it into the database
            for card in cards:
                card_id = card["id"]
                card_name = card["name"]
                card_trello_id = card_id
                card_url = card["shortUrl"]
                card_desc = card["desc"]
                card_list_id = list_id
                cur.execute("""
                    INSERT INTO cards (name, trello_id, url, description, list_id)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (trello_id) DO UPDATE
                    SET name = EXCLUDED.name, url = EXCLUDED.url, description = EXCLUDED.description, list_id = EXCLUDED.list_id
                """, [card_name, card_trello_id, card_url, card_desc, card_list_id])
                conn.commit()

                # Retrieve the members assigned to the card from the Trello API
                url = f"https://api.trello.com/1/cards/{card_id}/members?key={API_KEY}&token={API_TOKEN}"
                response = requests.get(url)
                members = response.json()

                # Retrieve the labels associated with the card from the Trello API
                url = f"https://api.trello.com/1/cards/{card_id}/labels?key={API_KEY}&token={API_TOKEN}"
                response = requests.get(url)
                labels = response.json()

                # Execute a SELECT query to get the id of a row
                cur.execute("SELECT id FROM cards WHERE trello_id = %s", (card_id,))

                # Fetch the result
                result = cur.fetchone()

                # Get the id from the result
                card_id = result[0]

                # Insert the labels into the "labels" table and the "cards_labels" table
                for label in labels:
                    label_id = label["id"]
                    label_name = label["name"]
                    label_color = label["color"]
                    label_trello_id = label_id
                    cur.execute("""
                                    INSERT INTO labels (name, color, trello_id, board_id)
                                    VALUES (%s, %s, %s, %s)
                                    ON CONFLICT (trello_id) DO UPDATE
                                    SET name = EXCLUDED.name, color = EXCLUDED.color
                                    RETURNING id
                                """, [label_name, label_color, label_trello_id, board_id])
                    label_row_id = cur.fetchone()[0]
                    conn.commit()

                    # Execute a SELECT query to get the id of a row
                    cur.execute("SELECT id FROM labels WHERE trello_id = %s", (label_id,))

                    # Fetch the result
                    result = cur.fetchone()

                    # Get the id from the result
                    label_id = result[0]

                    cur.execute("""
                                    INSERT INTO cards_labels (card_id, label_id)
                                    VALUES (%s, %s)
                                """, [card_id, label_id])
                    conn.commit()

                # Insert the members assigned to the card into the database
                for member in members:
                    member_id = member["id"]
                    member_fullname = member["fullName"]
                    member_username = member["username"]
                    member_trello_id = member["id"]

                    # Check if the member already exists in the database
                    cur.execute("""
                        SELECT id FROM members WHERE trello_id = %s
                    """, [member_trello_id])
                    result = cur.fetchone()

                    # If the member doesn't exist, insert them into the database
                    if result is None:
                        cur.execute("""
                            INSERT INTO members (fullname, trello_username, trello_id)
                            VALUES (%s, %s, %s)
                            RETURNING id
                        """, [member_fullname, member_username, member_trello_id])
                        member_id = cur.fetchone()[0]
                    else:
                        member_id = result[0]

                    # Associate the member with the card in the database
                    cur.execute("""
                        INSERT INTO cards_members (card_id, member_id)
                        VALUES (%s, %s)
                    """, [card_id, member_id])

                    conn.commit()

    # Close the cursor and connection to the database
    cur.close()
    conn.close()