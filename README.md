# BRSTEAM

Steam is currently the largest platform for digital computer games. Integrated with it is a profile system where users can add each other and share game-related content. In the store, users can purchase products, which are subdivided into Games and Soundtracks; they can also write reviews about the products.

The goal of this project is to model the main data from the store and the database relations with the user, but only for Brazilian users. For this, we used certain openly available data from the Steam store (https://store.steampowered.com/).

We used Python 3.9, the PostgreSQL DBMS, and the psycopg2 library to interact with the PostgreSQL server via Python commands.

## Demo (Brazilian Portuguese)
https://youtu.be/UwriAmFzSCw

## How to run:

- Clone the repository for local execution.
- Run a local instance of PostgreSQL.
- Make sure your Python version is 3.9.
- Run `pip install psycopg2`.
- Run `py instancias.py` to initialize the database.
- Run `py cli.py`.

## Queries

#### 1:Users who spent more than [x] reais

Gathers statistics for the admin to identify which users have invested the most on the platform.

#### 2: Number of users who purchased each game

Gathers statistics for the admin to know which games are the most popular.

#### 3: Products that don't support the [x] system

Important for users to know if a game doesn't support their system.

#### 4: Users who own all games from the publisher [publi]

This query can be used by the system to recommend new games from a certain publisher to potential customers.

#### 5: Games without achievements

Some players care a lot about achievements and might not want to buy games that don't have achievements registered in the system.

#### 6: Messages sent by the user [user]

This can be used by the admin to check the user's message history to verify if there are inappropriate or harmful messages.

User examples:
- william
- alho

#### 7: Purchases made by the user [user], comparison of prices paid with current prices

A query made by the user to analyze their purchase history.

#### 8: Reviews made by the user [user]

Used by the admin to filter the reviews for publication based on what the user has already posted, or by the user themselves to see their own reviews.

#### 9: Ranking of product genres owned by the user [user]

Used to recommend personalized genres to each user.

#### 10: Games with an average rating higher than [rating]

The user can search the store for games with good ratings.

## Details: 

In the database, we modeled:
- The main data from the store (such as products like games and soundtracks).
User relationships with products (such as purchases and the submission of reviews with ratings and text for each product).
- Interactions between users, consolidated through a friendship and messaging system.

We used Python 3.9, PostgreSQL, and psycopg2 to interact with the PostgreSQL server via Python commands.

Additional technical details about the database can be found in the `spec.pdf` file (brazilian portuguese).

## Entity-Relationship Diagram (Brazilian Portuguese)
![image](https://github.com/user-attachments/assets/6ae3bfcb-d203-4881-af0b-a2f31f2b5c39)
