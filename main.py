import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "https://www.google.com/",
        client_id = "your id",
        client_secret="your id",
        show_dialog=True,
        cache_path="token.txt",
        username= "your id?"
    )
)

user_id = sp.current_user()["id"]

year = input("Enter year you want the songs of: ")

url = "https://popnable.com/india/charts/top-40/year-" + year

header = {"your info here :) again"}
response = requests.get(url = url, headers = header)

soup = BeautifulSoup(response.text, "html.parser")
song_name = soup.select(selector=".chart-song-name")
song_name_lst = []
for song in song_name: # print(song_name) or print(song.get_text()) wont work
    print(song.get_text(strip=True))
    song_name_lst.append(song.get_text(strip=True))

song_urls = []
for song in song_name_lst:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        url = result["tracks"]["items"][0]["uri"]
        song_urls.append(url)
        print(url,song)
    except:
        print("song doesn't exist. skipped:",song)

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard Indian", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)
