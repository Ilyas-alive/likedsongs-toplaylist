
LIKED2PLAYLIST

A simple Python script to convert your liked songs on Spotify into a private playlist.

Install dependencies:

```
pip install spotipy
```

********************************************************************************************************

Add your Spotify API credentials in the script for extra privacy, as my API won't be available for long.

1. Go to: [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. App name: Whatever you choose
3. App description: Whatever you choose
4. Website: Whatever you choose
5. Redirect URIs: `http://127.0.0.1:8888/callback` (don’t forget to press "Add")
6. APIs used: Web API

After creating the app, take the **Client ID** and **Client Secret**, and replace them in the script.

********************************************************************************************************

Run:

```
python main.py
```
