import psycopg2

DB_NAME = "anicybqt"
DB_USER = "anicybqt"
DB_PASS = "lZ3dcF3RsHvdd-cFVN2LHszOUhWweASb"
DB_HOST = "rogue.db.elephantsql.com"
DB_PORT = "5432"

def initDB():
    try:
        connector = psycopg2.connect(database = DB_NAME,
                                user = DB_USER,
                                password= DB_PASS,
                                host= DB_HOST,
                                port = DB_PORT)
        print("Connection Successfully")
        cursor = connector.cursor()
        cursor.execute(
            """
        DROP TABLE IF EXISTS Squares;
        CREATE TABLE Squares
            (
                square_id INT,
                coordinate_X INT,
                coordinate_X_value decimal,
                coordinate_Y INT,
                coordinate_Y_value decimal
            );
        INSERT INTO Squares (square_id,coordinate_X, coordinate_X_value, coordinate_Y, coordinate_Y_value)
        VALUES (1,0,0,0,0),(2,0,0,1,0),(3,1,0,0,0),(4,1,0,1,0);
        
        DROP TABLE IF EXISTS IDs;
        CREATE TABLE IDs
            (
                square_id INT,
                item_id INT
            );
        
        DROP TABLE IF EXISTS Items;
        CREATE TABLE Items
            (
                item_id INT,
                content JSON
            );
        INSERT INTO Items (item_id, content)
        VALUES (1, '{"title": "ASTERIX", "url": "fzhofehoie","duration": 12.0}');
        
        DROP TABLE IF EXISTS Rank;
        CREATE TABLE Rank
            (
                item_id INT,
                rank INT
            );
        DROP TABLE IF EXISTS Coordinates;
        CREATE TABLE Coordinates
            (
                item_id INT,
                coordinate_x TEXT,
                coordinate_y TEXT
            );
            """
        )
        connector.commit()
        print("Initiation Database Successfully")

    except:
        print("Connection Failed")

import pandas as pd

if __name__ == "__main__":
	initDB()
    