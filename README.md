# Anime List Application

This application is a Python-based project that fetches the top 50 animes from MyAnimeList using their API, stores the data in a SQLite database, and displays the information in a GUI using Tkinter.

## Features

- Fetches data from MyAnimeList API.
- Stores the fetched data in a SQLite database.
- Displays the anime data in a GUI.

## Files

- `utile/fetch_api.py`: Contains the function to fetch the top 50 animes from MyAnimeList.
- `database/script_db.py`: Contains the function to fetch the anime data and store it in the database.
- `utile/data.py`: Contains functions to store the fetched anime data in the SQLite database and fetch the stored data from the database.
- `main.py`: Contains the main function that fetches the anime data from the database and displays it in the GUI.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Run the `main.py` file using the command `python main.py`.

## Dependencies

- Python
- Tkinter
- PIL (Pillow)
- requests
- sqlite3
- http.client
- json

## Note

This project is for educational purposes only. The MyAnimeList API key used in this project is a placeholder and will not work. Please replace it with your own API key to fetch data from MyAnimeList.