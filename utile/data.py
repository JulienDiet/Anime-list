import sqlite3

def store_animes_in_db(animes):
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('animes.db')
    # Create a cursor
    c = conn.cursor()
    # Drop the table if it exists and create a new one
    c.execute('''DROP TABLE IF EXISTS animes;''')
    c.execute('''CREATE TABLE IF NOT EXISTS animes (
        rank INTEGER, 
        title TEXT, 
        url TEXT, 
        image_url TEXT, 
        type TEXT, 
        episodes INTEGER, 
        start_date TEXT, 
        members INTEGER, 
        score FLOAT
    )''')
    # Insert each anime into the table
    for anime in animes:
        values = (
            anime['rank'],
            anime['title'],
            anime['myanimelist_url'],
            anime['picture_url'],
            anime['type'],
            anime['type'],
            anime['aired_on'],
            anime['members'],
            anime['score']
        )
        c.execute("INSERT INTO animes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
