# create tables
```sql
CREATE TABLE "boards" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar,
  "trello_id" varchar UNIQUE NOT NULL
);

CREATE TABLE "lists" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar,
  "trello_id" varchar UNIQUE NOT NULL,
  "board_id" int
);

CREATE TABLE "cards" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar NOT NULL,
  "trello_id" varchar UNIQUE NOT NULL,
  "url" varchar,
  "desc" text,
  "list_id" int
);

CREATE TABLE "members" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "fullname" varchar NOT NULL,
  "trello_username" varchar UNIQUE NOT NULL,
  "trello_id" varchar UNIQUE NOT NULL
);

CREATE TABLE "cards_members" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "card_id" int,
  "member_id" int
);

CREATE TABLE "labels" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar NOT NULL,
  "color" varchar,
  "trello_id" varchar UNIQUE NOT NULL,
  "board_id" int
);

CREATE TABLE "cards_labels" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "card_id" int,
  "label_id" int
);

CREATE TABLE "users" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "chat_id" bigint UNIQUE NOT NULL,
  "full_name" varchar,
  "username" varchar,
  "member_id" int
);

ALTER TABLE "lists" ADD FOREIGN KEY ("board_id") REFERENCES "boards" ("id");

ALTER TABLE "cards" ADD FOREIGN KEY ("list_id") REFERENCES "lists" ("id");

ALTER TABLE "cards_members" ADD FOREIGN KEY ("card_id") REFERENCES "cards" ("id");

ALTER TABLE "cards_members" ADD FOREIGN KEY ("member_id") REFERENCES "members" ("id");

ALTER TABLE "labels" ADD FOREIGN KEY ("board_id") REFERENCES "boards" ("id");

ALTER TABLE "cards_labels" ADD FOREIGN KEY ("card_id") REFERENCES "cards" ("id");

ALTER TABLE "cards_labels" ADD FOREIGN KEY ("label_id") REFERENCES "labels" ("id");

ALTER TABLE "users" ADD FOREIGN KEY ("member_id") REFERENCES "members" ("id");

```

# bot
# /start
result after pressing /start command
![image](https://user-images.githubusercontent.com/122611622/224290172-3156635c-7ace-4974-afb0-098444f694fe.png)

# /register
result after pressing /register command
## first
![image](https://user-images.githubusercontent.com/122611622/224291238-f3e8a812-9232-4908-a93c-33b0fa46bcf8.png)
## second
![image](https://user-images.githubusercontent.com/122611622/224291595-81f08d98-5156-4d3c-9cd5-1827fd32e4da.png)

# boards
result after pressing /boards command
![image](https://user-images.githubusercontent.com/122611622/224291774-e1c84c61-0787-4119-ba4c-8ed554762fc4.png)
![image](https://user-images.githubusercontent.com/122611622/224291939-aae9ac7b-fe41-4313-acd4-4230f4911e3b.png)

# update
result after pressing /update command
![image](https://user-images.githubusercontent.com/122611622/224304014-5a322073-b0df-4fbf-b37f-d5abcb4dd9f9.png)
![image](https://user-images.githubusercontent.com/122611622/224304166-aba02a2c-d242-4e49-82a2-af8eb021b8a4.png)

# update trello username
result after pressing /update_trello_username command
## if exist
![image](https://user-images.githubusercontent.com/122611622/224303610-433e889d-b48e-4d69-979b-e8d498674d82.png)
## else
![image](https://user-images.githubusercontent.com/122611622/224303736-6fa440f5-1331-4d10-83e9-b54acfe7ccae.png)