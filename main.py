import os
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='a2ff2f313c3542eea4f6573818835a73',
    client_secret='d6a8301f5503409593722541d0e9a3a7',
    redirect_uri='http://127.0.0.1:8888/callback',
    scope='user-library-read playlist-modify-private playlist-modify-public',
    cache_path=os.path.join(os.path.dirname(__file__), ".cache")
))

def liked_to_new_list():
    try:
        stuff = []
        offby = 0
        while True:
            result = sp.current_user_saved_tracks(limit=50, offset=offby)
            got = result['items']
            if len(got) == 0:
                break
            for thing in got:
                tr = thing.get('track')
                if tr and tr.get('uri'):
                    stuff.append(tr['uri'])
            offby += 50
            print("got", len(stuff))
        if len(stuff) == 0:
            print("empty liked")
            return
        me = sp.current_user()
        pl = sp.user_playlist_create(me['id'], "Liked Songs Playlist", public=False)
        count = 0
        for x in range(0, len(stuff), 100):
            chunk = stuff[x:x+100]
            try:
                sp.playlist_add_items(pl['id'], chunk)
                count += len(chunk)
            except:
                print("fail at", x)
            time.sleep(0.2)
        print("added", count)
    except Exception as rip:
        print("error:", rip)

if __name__ == "__main__":
    print("\n1 - Liked songs to playlist")
    print("2 - Exit")
    what = input("Pick (1/2): ").strip()
    if what == "1":
        liked_to_new_list()
    elif what == "2":
        pass
    else:
        print("Invalid input. Pick 1 or 2.")
