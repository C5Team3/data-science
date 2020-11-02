# data-science


This project was created with Python Language

## Available Scripts

In the project directory, you can run:

### `main.py <user_id>`
This script creates a suggested playlist based into playback history in the Rokker-app.
The new playlist is saved in the database.

It can be of two types:

1. Playlist for a specific user:  `main.py <user-sample@mail.com>`
2. General Playlist that will be shown to all users: `main.py`

### `history_downloader.py <user_id>`
This script consults the database and returns a csv file.
With the an user playback history or all the playback-history of the application.

1. Playback-history for a specific user:  `history_downloader.py <user-sample@mail.com>`
2. Playback-history for all users: `history_downloader.py`

## Virtual Enviroment and Libraries

This project runs about a virtual environment with these libraries:

 - pandas: `pip install pandas`
 - requests: `pip install requests`
 - dns: `pip install dns`
 - pymongo: `pip install pymongo`

## More Information
You can know more about this project in:

https://www.notion.so/Rokker-cc1801d5d871494caca6dc79bfe4594d
