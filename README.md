Install dependencies:

nginx
Copy
Edit
pip install spotipy
Add your Spotify API credentials in the script for extra privacy, as my API won't be available for long.

Go to: Spotify Developer Dashboard

App name: Whatever you choose

App description: Whatever you choose

Website: Whatever you choose

Redirect URIs: http://127.0.0.1:8888/callback (don’t forget to press "Add")

APIs used: Web API

After creating the app, take the Client ID and Client Secret, and replace them in the script.

Run:

nginx
Copy
Edit
python liked2playlist.py
